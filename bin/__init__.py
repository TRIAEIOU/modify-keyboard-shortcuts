import os, json
import aqt
from .ankiutils import *

CVER = get_version()
NVER = "1.0.0"

OSC_DONE = "_overrideshortcut_addon_done_"
WINDOW_CLOSE = "window close"
DEFAULTS = os.path.join(os.path.dirname(__file__), 'defaults.json')
CONFIG_MD = os.path.join(os.path.dirname(__file__), 'config.md')
INSTR = """Override found shortcuts by adding a key/value pair (see below for identified shortcuts). To unmap a found shortcut add the key with an empty value (`""`) example:

<pre><code>{
  "window close": "Escape",
  "AnkiQt": {
    "QtClassProxy: action-actionAbout": "Ctrl+Alt+A", // comma between items
    "QtClassProxy: action-actionAdd_ons": "" // empty string will remove binding
  }, // comma between windows
  "Browser": {
    "QtClassProxy: action_toggle_bury": ""
  }
}</code></pre>

Note that to detect available shortcuts each window has to be opened once. Restart Anki for edits to take effect.

# Identified shortcuts"""


# Finder ######################################################################
class Finder(aqt.QObject):
    """Class to find top level windows and read/override shortcuts"""
    defaults = {}
    discovered = {}
    cfg = mw.addonManager.getConfig(__name__)
    windows = {}
    i = {}
    escape = False

    def __init__(self, app: aqt.QApplication):
        with open(DEFAULTS) as fh:
            self.defaults = json.load(fh)
        super().__init__()
        app.focusChanged.connect(self.onfocus)

    def eventFilter(self: object, obj: aqt.QObject, evt: aqt.QEvent):
        """Used when instance installed as event filter to unmap `Escape` from window close"""
        evt_type = evt.type()
        if evt_type == aqt.QEvent.Type.ShortcutOverride and \
        evt.keyCombination() == aqt.QKeyCombination(aqt.Qt.Key.Key_Escape):
            self.escape = True
            evt.accept()
            return True # block event
        elif self.escape:
            if evt_type == aqt.QEvent.Type.Close:
                self.escape = False
                evt.ignore()
                return True # block event
            elif evt_type == aqt.QEvent.Type.KeyPress and \
            evt.keyCombination() == aqt.QKeyCombination(aqt.Qt.Key.Key_Escape):
                return False # don't block event (self.escape still True)
        self.escape = False
        return False
  
    @aqt.pyqtSlot(aqt.QWidget, aqt.QWidget)
    def onfocus(self, _old_widget: aqt.QWidget, widget: aqt.QWidget):
        """Slot for QApplication.focusChanged signal. If first encounter of top level
        widget for this app instance, discover all shortcuts. If firs encounter this
        app instance of this object **instance** override shortcuts as appropriate."""

        if not widget:
            return
        while not widget.isWindow():
            widget = widget.parent()
        # Type and instance seen
        if getattr(widget, OSC_DONE, False):
            return

        win_name = widget.metaObject().className()
        win_cfg = self.cfg.get(win_name, {})
        # Type (and instance seen) not seen - find shortcuts and override
        if self.discovered.get(win_name, None) == None:
            self.discovered[win_name] = {}
            discovery = True
        else:
            discovery = False
        
        def find(widget: aqt.QWidget, class_, get, set):
            """Find all children of class_, store if first widget first encounter,
            override if appropriate. Requires functions to get and set key sequence."""
            for obj in widget.findChildren(class_):
                class_name = class_.staticMetaObject.className()
                sequence = get(obj)

                if oname := obj.objectName():
                    seq_name = f"{class_name} {oname}"
                elif sequence:
                    seq_name = f"{class_name} ({sequence})"
                else:
                    self.i[class_name] = self.i.get(class_name, 0) + 1
                    seq_name = f"{class_name} [{self.i[class_name]}]"

                if discovery:
                    self.discovered[win_name][seq_name] = sequence
                if (oride := win_cfg.get(seq_name, None)) != None and oride != sequence:
                    set(obj, oride)

        # Find all actions and shortcuts, store or override as needed
        find(widget, aqt.QAction, lambda o: o.shortcut().toString(), lambda o, s: o.setShortcut(aqt.QKeySequence(s)))
        find(widget, aqt.QShortcut, lambda o: o.key().toString(), lambda o, s: o.setKey(aqt.QKeySequence(s)))
        
        # Unmap escape for window close
        if (s := self.cfg.get(WINDOW_CLOSE, 'Escape')) != 'Escape':
            widget.installEventFilter(self)

        # Completely overwrite previously found sections with new versions (`|` is non-recursive)
        if discovery:
            merged = self.defaults | self.discovered
            with open(DEFAULTS, "w") as fh:
                json.dump(merged, fh)
            with open(CONFIG_MD, "w") as fh:
                fh.write(f"{INSTR}\n\n<pre><code>{json.dumps(merged, indent=2)}</code></pre>")

        # Instance now seen
        setattr(widget, OSC_DONE, True)


# main ######################################################################
if strvercmp(CVER, NVER) < 0:
    set_version(NVER)

# Start finding top level windows
finder = Finder(aqt.mw.app)
