import os, json, inspect
import aqt
from .ankiutils import *

CVER = get_version()
NVER = "1.0.0"

DEFAULTS = os.path.join(os.path.dirname(__file__), 'defaults.json')
CONFIG_MD = os.path.join(os.path.dirname(__file__), 'config.md')
INSTR = """Override found shortcuts by adding a key/value pair (see below for identified shortcuts). To unmap a found shortcut add the key with an empty value (`""`) example:

<pre><code>{
  "main window": {
    "action-actionAbout": "Ctrl+Alt+A", // comma between items
    "action-actionAdd_ons": "" // empty string will remove the default shortcut
  }, // comma between windows
  "browser": {
    "action-action_toggle_bury": ""
  }
}</code></pre>

Note that to detect available shortcuts each window has to be opened once. Restart Anki for edits to take effect.

# Identified shortcuts"""

def override(win, obj):
    """Update default shortcuts for the window, set any configured shortcuts"""
    global _new, _config

    def name(prefix, keys, obj, i):
        if oname := obj.objectName():
            return f"{prefix}-{oname}"
        elif keys:
            return f"{prefix}-unnamed-{keys}"
        else:
            i[0] += 1
            return f"{prefix}-unnamed-[{i[0]}]"
    
    def override_(win, key, sequence):
        if (win_ := _config.get(win)) and (oride := win_.get(key)) != sequence:
            return oride
        return None

    if _new.get(win) == None:
        _new[win] = {}
        store = True
    else:
        store = False

    i = [0]
    for oo in obj.findChildren(aqt.QAction):
        sequence = oo.shortcut().toString()
        name_ = name('action', sequence, oo, i)
        if store:
            _new[win][name_] = sequence
        if oride := override_(win, name_, sequence):
            oo.setShortcut(oride)
    
    i = [0]
    for oo in obj.findChildren(aqt.QShortcut):
        sequence = oo.key().toString()
        name_ = name('shortcut', sequence, oo, i)
        if store:
            _new[win][name_] = sequence
        if oride := override_(win, name_, sequence):
            oo.setKey(oride)

    i = [0]
    for oo in obj.findChildren(aqt.QKeySequence):
        sequence = oo.toString()
        name_ = name('sequence', sequence, oo, i)
        if store:
            _new[win][name_] = sequence
        if oride := override_(win, name_, sequence):
            oo.swap(aqt.QKeySequence.fromString(oride))
    
    if store:
        save()

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

aqt.gui_hooks.main_window_did_init.append(lambda: override('main window', aqt.mw))
aqt.gui_hooks.browser_will_show.append(lambda w: override('browser', w))
aqt.gui_hooks.add_cards_did_init.append(lambda w: override('add note', w))
