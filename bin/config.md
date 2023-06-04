Override found shortcuts by adding a key/value pair (see below for identified shortcuts). To unmap a found shortcut add the key with an empty value (`""`) example:

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

# Identified shortcuts

<pre><code>{
  "main window": {
    "action-actionExit": "Ctrl+Q",
    "action-actionPreferences": "Ctrl+P",
    "action-actionAbout": "",
    "action-actionUndo": "Ctrl+Z",
    "action-actionCheckMediaDatabase": "",
    "action-actionDonate": "",
    "action-actionFullDatabaseCheck": "",
    "action-actionDocumentation": "F1",
    "action-actionSwitchProfile": "Ctrl+Shift+P",
    "action-actionExport": "Ctrl+E",
    "action-actionImport": "Ctrl+Shift+I",
    "action-actionStudyDeck": "/",
    "action-actionEmptyCards": "",
    "action-actionCreateFiltered": "F",
    "action-actionNoteTypes": "Ctrl+Shift+N",
    "action-actionAdd_ons": "Ctrl+Shift+A",
    "action-actionRedo": "Ctrl+Shift+Z",
    "action-actionFullScreen": "F11",
    "action-actionZoomIn": "",
    "action-actionZoomOut": "",
    "action-actionResetZoom": "Ctrl+0",
    "action-action_create_backup": "",
    "action-unnamed-[1]": "",
    "action-unnamed-[2]": "",
    "action-unnamed-[3]": "",
    "shortcut-unnamed-Ctrl+:": "Ctrl+:",
    "shortcut-unnamed-D": "D",
    "shortcut-unnamed-S": "S",
    "shortcut-unnamed-A": "A",
    "shortcut-unnamed-B": "B",
    "shortcut-unnamed-T": "T",
    "shortcut-unnamed-Y": "Y"
  }
}</code></pre>