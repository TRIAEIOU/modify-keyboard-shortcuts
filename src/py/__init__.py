import os, json
import aqt
from .ankiutils import *

CVER = get_version()
NVER = "1.0.0"

DEFAULTS = os.path.join(os.path.dirname(__file__), 'defaults.json')
CONFIG_MD = os.path.join(os.path.dirname(__file__), 'config.md')
INSTR = """Override found shortcuts by adding a key/value pair (see below for identified shortcuts). To unmap a found shortcut add the key with an empty value (`""`) example:

<pre><code>{
  "aqt.main.AnkiQt": {
    "action-actionAbout": "Ctrl+Alt+A", // comma between items
    "action-actionAdd_ons": "" // empty string will remove the default shortcut
  }, // comma between windows
  "aqt.browser.browser.Browser": {
    "action-action_toggle_bury": ""
  }
}</code></pre>

Note that to detect available shortcuts each window has to be opened once. Restart Anki for edits to take effect.

# Identified shortcuts"""

class Finder(aqt.QObject):
    """Class to connect focusChanged signal to identify top level windows and read/override shortcuts"""
    windows = {}

    @aqt.pyqtSlot(aqt.QWidget, aqt.QWidget)
    def onfocus(self, old: aqt.QWidget, new: aqt.QWidget):
        """Slot called each time focus changes"""

        def window_name(window):
            """Return suitable name for window object"""
            return str(type(window))[8:-2]

        def sequence_name(prefix, sequence, obj):
            """Return suitable name for shortcut sequence"""
            if oname := obj.objectName():
                return f"{prefix}-{oname}"
            elif sequence:
                return f"{prefix}-unnamed-{sequence}"
            else:
                sequence_name.i[prefix] = sequence_name.i.get(prefix, 0) + 1
                return f"{prefix}-unnamed-[{sequence_name.i[prefix]}]"
        sequence_name.i = {}

        def override_(win_name, key, sequence):
            """Override default shortcut if config has other than"""
            if (win_ := _config.get(win_name)) and (oride := win_.get(key)) != sequence:
                return oride
            return None

        if new:
            while new and not new.isWindow():
                new = new.parent()
            win_name = window_name(new)
            if _new.get(win_name) == None:
                _new[win_name] = {}
                store = True
            else:
                store = False

            #print(f"::{win_name}")
            # Find all actions, store or override as needed
            for oo in new.findChildren(aqt.QAction):
                sequence = oo.shortcut().toString()
                seq_name = sequence_name('action', sequence, oo)
                if store:
                    _new[win_name][seq_name] = sequence
                if (oride := override_(win_name, seq_name, sequence)) != None:
                    oo.setShortcut(oride)
                    #print(f"overriding action {seq_name} with {oride}")
                #print(f"{sequence_name('action', sequence, oo)}: {sequence}")
            
            # Find all shortcuts, store or override as needed
            for oo in new.findChildren(aqt.QShortcut):
                sequence = oo.key().toString()
                seq_name = sequence_name('shortcut', sequence, oo)
                if store:
                    _new[win_name][seq_name] = sequence
                if (oride := override_(win_name, seq_name, sequence)) != None:
                    oo.setKey(oride)
                    #print(f"overriding shortcut {seq_name} with {oride}")
                #print(f"{sequence_name('shortcut', sequence, oo)}: {sequence}")
        
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

# Hook on application level focus change to detect new windows
_finder = Finder()
aqt.gui_hooks.main_window_did_init.append(lambda: aqt.mw.app.focusChanged.connect(_finder.onfocus))
