import os, json
import aqt
from .ankiutils import *

CVER = get_version()
NVER = "1.0.0"

DEFAULTS = os.path.join(os.path.dirname(__file__), 'defaults.json')
CONFIG_MD = os.path.join(os.path.dirname(__file__), 'config.md')
INSTR = """# Modify shortcuts

Modify found Anki core shortcuts by adding a key/value pair (see below for identified shortcuts). To remove default Anki shortcut add the key with an empty value (`""`) example:

<pre><code>{
  "main window": {    
    "actionAbout": "Ctrl+Alt+A", // comma between items
    "actionAdd_ons": ""   
  },
  "browser": {
    "action_toggle_bury": ""
  }
}</code></pre>

Note that to detect available shortcuts each window has to be opened once. Restart Anki for edits to take effect.

## Identified shortcuts"""

def set_shortcuts(win, obj):
    """Update default shortcuts for the window and save if changed, set any configured shortcuts"""
    global _new, _config

    # If first contact this execution: update found shortcuts
    if _new.get(win) == None:
        _new[win] = {}
        _save = False
        for a in dir(obj.form):
            if a.startswith('action') and\
            (ao := getattr(obj.form, a)) and\
            callable(getattr(ao, 'shortcut')):
                _new[win][a] = ao.shortcut().toString()
                _save = True
        if _save:
            save()
    
    # Set shortcuts
    if _config.get(win):
        for k, v in _config[win].items():
            if a := getattr(obj.form, k, None):
                a.setShortcut(v)

def load(*_):
    """Load previously found defaults, reset _new and load _config"""
    global _defaults, _new, _config
    with open(DEFAULTS) as fh:
        _defaults = json.load(fh)
    _new = {}
    _config = mw.addonManager.getConfig(__name__)

def save(*_):
    """Write combination of previously and newly found key/vals to defaults.json and config.md"""
    global _defaults, _new
    # Completely overwrite previously found sections with new versions (`|` is non-recursive)
    merged = _defaults | _new
    with open(DEFAULTS, "w") as fh:
        json.dump(merged, fh)
    with open(CONFIG_MD, "w") as fh:
        fh.write(f"{INSTR}\n\n<pre><code>{json.dumps(merged, indent=2)}</code></pre>")

if strvercmp(CVER, NVER) < 0:
    set_version(NVER)

_defaults = {}
_new = {}
_config = {}

# Load earlier discovered shortcuts
aqt.gui_hooks.profile_did_open.append(load)

aqt.gui_hooks.main_window_did_init.append(lambda: set_shortcuts('main window', aqt.mw))
aqt.gui_hooks.browser_will_show.append(lambda w: set_shortcuts('browser', w))
aqt.gui_hooks.add_cards_did_init.append(lambda w: set_shortcuts('add note', w))


"""
    mwShortcuts = mw.findChildren(QShortcut)
    if functions.get_version() >= 50:
        for child in mwShortcuts:
            if child.key().toString() in mainShortcutPairs:
                oldScut = child.key().toString()
                newScut = mainShortcutPairs[oldScut]
                child.setKey(newScut)
                mainShortcutPairs.pop(oldScut) # Only replace shortcuts once (the first time would be the main shortcut)

"""