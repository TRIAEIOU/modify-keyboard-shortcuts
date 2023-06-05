Override found shortcuts by adding a key/value pair (see below for identified shortcuts). To unmap a found shortcut add the key with an empty value (`""`) example:

<pre><code>{
  "AnkiQt": {
    "QtClassProxy: action-actionAbout": "Ctrl+Alt+A", // comma between items
    "QtClassProxy: action-actionAdd_ons": "" // empty string will remove binding
  }, // comma between windows
  "Browser": {
    "QtClassProxy: action_toggle_bury": ""
  }
}</code></pre>

Note that to detect available shortcuts each window has to be opened once. Restart Anki for edits to take effect.

# Identified shortcuts

<pre><code>{
  "AnkiQt": {
    "QtClassProxy: actionExit": "Ctrl+Q",
    "QtClassProxy: actionPreferences": "Ctrl+P",
    "QtClassProxy: actionAbout": "",
    "QtClassProxy: actionUndo": "Ctrl+Z",
    "QtClassProxy: actionCheckMediaDatabase": "",
    "QtClassProxy: actionDonate": "",
    "QtClassProxy: actionFullDatabaseCheck": "",
    "QtClassProxy: actionDocumentation": "F1",
    "QtClassProxy: actionSwitchProfile": "Ctrl+Shift+P",
    "QtClassProxy: actionExport": "Ctrl+E",
    "QtClassProxy: actionImport": "Ctrl+Shift+I",
    "QtClassProxy: actionStudyDeck": "/",
    "QtClassProxy: actionEmptyCards": "",
    "QtClassProxy: actionCreateFiltered": "F",
    "QtClassProxy: actionNoteTypes": "Ctrl+Shift+N",
    "QtClassProxy: actionAdd_ons": "Ctrl+Shift+A",
    "QtClassProxy: actionRedo": "Ctrl+Shift+Z",
    "QtClassProxy: actionFullScreen": "F11",
    "QtClassProxy: actionZoomIn": "",
    "QtClassProxy: actionZoomOut": "",
    "QtClassProxy: actionResetZoom": "Ctrl+0",
    "QtClassProxy: action_create_backup": "",
    "QtClassProxy-1": "",
    "QtClassProxy-2": "",
    "QtClassProxy-3": "",
    "QShortcut (Ctrl+:)": "Ctrl+:",
    "QShortcut (D)": "D",
    "QShortcut (S)": "S",
    "QShortcut (A)": "A",
    "QShortcut (B)": "B",
    "QShortcut (T)": "T",
    "QShortcut (Y)": "Y"
  },
  "Browser": {
    "QtClassProxy: actionSelectAll": "Ctrl+Alt+A",
    "QtClassProxy: actionUndo": "Ctrl+Z",
    "QtClassProxy: actionInvertSelection": "Ctrl+Alt+S",
    "QtClassProxy: actionFind": "Ctrl+F",
    "QtClassProxy: actionNote": "Ctrl+Shift+N",
    "QtClassProxy: actionNextCard": "Ctrl+N",
    "QtClassProxy: actionPreviousCard": "Ctrl+P",
    "QtClassProxy: actionGuide": "F1",
    "QtClassProxy: actionChangeModel": "Ctrl+Shift+M",
    "QtClassProxy: actionSelectNotes": "",
    "QtClassProxy: actionFindReplace": "Ctrl+Alt+F",
    "QtClassProxy: actionSidebarFilter": "Ctrl+Shift+F",
    "QtClassProxy: actionCardList": "Ctrl+Shift+L",
    "QtClassProxy: actionFindDuplicates": "",
    "QtClassProxy: actionReposition": "Ctrl+Shift+S",
    "QtClassProxy: actionFirstCard": "Home",
    "QtClassProxy: actionLastCard": "End",
    "QtClassProxy: actionClose": "Ctrl+W",
    "QtClassProxy: action_Info": "Ctrl+Shift+I",
    "QtClassProxy: actionAdd_Tags": "Ctrl+Shift+A",
    "QtClassProxy: actionRemove_Tags": "Ctrl+Alt+Shift+A",
    "QtClassProxy: actionToggle_Suspend": "Ctrl+J",
    "QtClassProxy: actionDelete": "Ctrl+Del",
    "QtClassProxy: actionAdd": "Ctrl+E",
    "QtClassProxy: actionChange_Deck": "Ctrl+D",
    "QtClassProxy: actionRed_Flag": "Ctrl+1",
    "QtClassProxy: actionOrange_Flag": "Ctrl+2",
    "QtClassProxy: actionGreen_Flag": "Ctrl+3",
    "QtClassProxy: actionBlue_Flag": "Ctrl+4",
    "QtClassProxy: actionSidebar": "Ctrl+Shift+R",
    "QtClassProxy: actionClear_Unused_Tags": "",
    "QtClassProxy: actionManage_Note_Types": "",
    "QtClassProxy: actionToggle_Mark": "Ctrl+K",
    "QtClassProxy: actionExport": "Ctrl+Shift+E",
    "QtClassProxy: actionCreateFilteredDeck": "Ctrl+G",
    "QtClassProxy: action_set_due_date": "Ctrl+Shift+D",
    "QtClassProxy: action_forget": "Ctrl+Alt+N",
    "QtClassProxy: action_toggle_mode": "Ctrl+Alt+T",
    "QtClassProxy: actionRedo": "Ctrl+Shift+Z",
    "QtClassProxy: actionPink_Flag": "Ctrl+5",
    "QtClassProxy: actionTurquoise_Flag": "Ctrl+6",
    "QtClassProxy: actionPurple_Flag": "Ctrl+7",
    "QtClassProxy: actionCopy": "Ctrl+Alt+E",
    "QtClassProxy: actionFullScreen": "",
    "QtClassProxy: actionZoomIn": "",
    "QtClassProxy: actionZoomOut": "",
    "QtClassProxy: actionResetZoom": "Ctrl+0",
    "QtClassProxy: actionLayoutAuto": "",
    "QtClassProxy: actionLayoutVertical": "",
    "QtClassProxy: actionLayoutHorizontal": "",
    "QtClassProxy: actionbrowsing_toggle_showing_cards_notes": "",
    "QtClassProxy: action_toggle_bury": "Ctrl+Shift+J",
    "QShortcut (Ctrl+Alt+M)": "Ctrl+Alt+M",
    "QShortcut (Ctrl+M)": "Ctrl+M",
    "QShortcut (Ctrl+Alt+X)": "Ctrl+Alt+X",
    "QShortcut (Ctrl+PgDown)": "Ctrl+PgDown",
    "QShortcut (Ctrl+PgUp)": "Ctrl+PgUp",
    "QShortcut (Shift+Home)": "Shift+Home",
    "QShortcut (Shift+End)": "Shift+End",
    "QShortcut (Shift+Esc)": "Shift+Esc",
    "QShortcut (Ctrl+Shift+P)": "Ctrl+Shift+P"
  },
  "AddonsDialog": {},
  "ConfigEditor": {},
  "DebugConsole": {
    "QShortcut (Ctrl+Return)": "Ctrl+Return",
    "QShortcut (Ctrl+Shift+Return)": "Ctrl+Shift+Return",
    "QShortcut (Ctrl+L)": "Ctrl+L",
    "QShortcut (Ctrl+Shift+L)": "Ctrl+Shift+L",
    "QShortcut (Ctrl+S)": "Ctrl+S",
    "QShortcut (Ctrl+O)": "Ctrl+O",
    "QShortcut (Ctrl+D)": "Ctrl+D"
  },
  "WidgetGallery": {},
  "QComboBoxPrivateContainer": {},
  "AddCards": {
    "QShortcut (Ctrl+N)": "Ctrl+N",
    "QShortcut (Ctrl+D)": "Ctrl+D",
    "QShortcut (Ctrl+Alt+M)": "Ctrl+Alt+M",
    "QShortcut (Ctrl+M)": "Ctrl+M",
    "QShortcut (Ctrl+Alt+X)": "Ctrl+Alt+X",
    "QShortcut (Ctrl+PgDown)": "Ctrl+PgDown",
    "QShortcut (Ctrl+PgUp)": "Ctrl+PgUp",
    "QShortcut (Ctrl+Enter)": "Ctrl+Enter",
    "QShortcut (Shift+Esc)": "Shift+Esc"
  }
}</code></pre>