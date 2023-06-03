import os, json
import aqt
from .ankiutils import *

CONFIG_JSON = os.path.join(os.path.dirname(__file__), 'config.json')
META_JSON = os.path.join(os.path.dirname(__file__), 'meta.json')
DEPRECATED = 'deprecated'

def set_scuts(win, obj):
    global _new, _meta

    # If first contact this execution: update found shortcuts
    if _new.get(win) == None:
        _new[win] = {}
        for a in dir(obj.form):
            if a.startswith('action') and\
            (ao := getattr(obj.form, a)) and\
            callable(getattr(ao, 'shortcut')):
                _new[win][a] = ao.shortcut().toString()
    
    # Set shortcuts
    if _meta.get(win):
        for k, v in _meta[win].items():
            getattr(obj.form, k).setShortcut(v)
            print(f"Added {k}: {v}")

def reduce_config():
    """Load _meta from file, deprecate keys not found and remove default values →
returns meta with only valid changed keys."""
    # Deprecate keys not found, remove default values
    meta = {DEPRECATED: {}}
    for k, v in mw.addonManager.getConfig(__name__).items():
        if k == DEPRECATED:
            if type(k) == dict:
                for kk, vv in k.items():
                    meta[DEPRECATED][kk] |= vv # if meta[DEPRECATED].get(kk) else vv
        elif _old.get(k) == None:
            meta[DEPRECATED][k] = v
        else:
            for kk, vv in v.items():
                if _old[k].get(kk) == None:
                    meta[DEPRECATED][k][kk] = vv
                elif _old[k][kk] != vv:
                    if not meta.get(k):
                        meta[k] = {}
                    meta[k][kk] = vv
    return meta

def edit_config(text: str, addon: str):


def load(*_):
    """Load previously found values, setup config to only contain changes from default"""
    global _old, _new, _meta

    with open(CONFIG_JSON) as fh:
        _old = json.load(fh)
    _new = {}
    _meta = load_meta()

def save(*_):
    """Write combination of previously and newly found key/vals"""
    global _old, _new

    merged = {k: v for k, v in _new.items()}
    for k, v in _old.items():
        if _new.get(k, -1) == -1:
            merged[k] = v

    with open(CONFIG_JSON, "w") as fh:
        json.dump(merged, fh)  
    mw.addonManager.writeConfig(__name__, _meta)
   

_old = {}
_new = {}
_meta = {}

# Load earlier discovered shortcuts
aqt.gui_hooks.profile_did_open.append(load)
# Save all discovered shortcuts
aqt.gui_hooks.profile_will_close.append(save)
# Reduce meta.json to only contain differences from default
aqt.gui_hooks.addon_config_editor_will_update_json.append(reduce_config)

aqt.gui_hooks.main_window_did_init.append(lambda: set_scuts('main', aqt.mw))
aqt.gui_hooks.browser_will_show.append(lambda w: set_scuts('browser', w))
aqt.gui_hooks.add_cards_did_init.append(lambda w: set_scuts('add', w))
#aqt.gui_hooks.editor_did_init.append(lambda w: set_scuts('editor', w))


"""
# All QAction instances version import gc
from aqt import QAction

scs = {}

def find(*_):
    for obj in gc.get_objects():
        try:
            if not (isinstance(obj, QAction) and obj.associatedObjects()):
                continue

            parent_ = obj.associatedObjects()[0]
            while p := parent_.parent():
                print(f"parent: {parent_}, p.parent(): {p.parent()}")
                parent_ = p
            parent = parent_.objectName()
            if not scs.get(parent):
                scs[parent] = {}
            scs[parent][obj.objectName()] = obj.shortcut().toString()

        except ReferenceError:
            pass
    print("----------------------------------------------------")
    print(json.dumps(scs))
            
aqt.gui_hooks.main_window_did_init.append(find)
aqt.gui_hooks.browser_will_show.append(find)
aqt.gui_hooks.add_cards_did_init.append(find)
aqt.gui_hooks.editor_did_init.append(find)
"""
