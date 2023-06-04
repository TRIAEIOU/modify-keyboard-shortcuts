Override found shortcuts by adding a key/value pair (see below for identified shortcuts). To unmap a found shortcut add the key with an empty value (`""`) example:

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

# Identified shortcuts

<pre><code>{
  "aqt.main.AnkiQt": {
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
  },
  "aqt.browser.browser.Browser": {
    "action-actionSelectAll": "Ctrl+Alt+A",
    "action-actionUndo": "Ctrl+Z",
    "action-actionInvertSelection": "Ctrl+Alt+S",
    "action-actionFind": "Ctrl+F"
  },
  "aqt.addcards.AddCards": {
    "shortcut-unnamed-Ctrl+N": "Ctrl+N",
    "shortcut-unnamed-Ctrl+D": "Ctrl+D",
    "shortcut-unnamed-Ctrl+Alt+M": "Ctrl+Alt+M",
    "shortcut-unnamed-Ctrl+M": "Ctrl+M",
    "shortcut-unnamed-Ctrl+Alt+X": "Ctrl+Alt+X",
    "shortcut-unnamed-Ctrl+PgDown": "Ctrl+PgDown",
    "shortcut-unnamed-Ctrl+PgUp": "Ctrl+PgUp",
    "shortcut-unnamed-Ctrl+Enter": "Ctrl+Enter",
    "shortcut-unnamed-Shift+Esc": "Shift+Esc"
  },
  "aqt.studydeck.StudyDeck": {},
  "aqt.preferences.Preferences": {},
  "aqt.about.ClosableQDialog": {},
  "aqt.qt.qt5_compat._instrument_type.<locals>.QtClassProxy": {}
}</code></pre>