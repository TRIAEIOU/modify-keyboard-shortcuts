# Modify shortcuts

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

## Identified shortcuts

<pre><code>{
  "main window": {
    "actionAbout": "",
    "actionAdd_ons": "Ctrl+Shift+A",
    "actionCheckMediaDatabase": "",
    "actionCreateFiltered": "F",
    "actionDocumentation": "F1",
    "actionDonate": "",
    "actionEmptyCards": "",
    "actionExit": "Ctrl+Q",
    "actionExport": "Ctrl+E",
    "actionFullDatabaseCheck": "",
    "actionFullScreen": "F11",
    "actionImport": "Ctrl+Shift+I",
    "actionNoteTypes": "Ctrl+Shift+N",
    "actionPreferences": "Ctrl+P",
    "actionRedo": "Ctrl+Shift+Z",
    "actionResetZoom": "Ctrl+0",
    "actionStudyDeck": "/",
    "actionSwitchProfile": "Ctrl+Shift+P",
    "actionUndo": "Ctrl+Z",
    "actionZoomIn": "",
    "actionZoomOut": "",
    "action_create_backup": ""
  },
  "browser": {
    "actionAdd": "Ctrl+E",
    "actionAdd_Tags": "Ctrl+Shift+A",
    "actionBlue_Flag": "Ctrl+4",
    "actionCardList": "Ctrl+Shift+L",
    "actionChangeModel": "Ctrl+Shift+M",
    "actionChange_Deck": "Ctrl+D",
    "actionClear_Unused_Tags": "",
    "actionClose": "Ctrl+W",
    "actionCopy": "Ctrl+Alt+E",
    "actionCreateFilteredDeck": "Ctrl+G",
    "actionDelete": "Ctrl+Del",
    "actionExport": "Ctrl+Shift+E",
    "actionFind": "Ctrl+F",
    "actionFindDuplicates": "",
    "actionFindReplace": "Ctrl+Alt+F",
    "actionFirstCard": "Home",
    "actionFullScreen": "",
    "actionGreen_Flag": "Ctrl+3",
    "actionGuide": "F1",
    "actionInvertSelection": "Ctrl+Alt+S",
    "actionLastCard": "End",
    "actionLayoutAuto": "",
    "actionLayoutHorizontal": "",
    "actionLayoutVertical": "",
    "actionManage_Note_Types": "",
    "actionNextCard": "Ctrl+N",
    "actionNote": "Ctrl+Shift+N",
    "actionOrange_Flag": "Ctrl+2",
    "actionPink_Flag": "Ctrl+5",
    "actionPreviousCard": "Ctrl+P",
    "actionPurple_Flag": "Ctrl+7",
    "actionRed_Flag": "Ctrl+1",
    "actionRedo": "Ctrl+Shift+Z",
    "actionRemove_Tags": "Ctrl+Alt+Shift+A",
    "actionReposition": "Ctrl+Shift+S",
    "actionResetZoom": "Ctrl+0",
    "actionSelectAll": "Ctrl+Alt+A",
    "actionSelectNotes": "",
    "actionSidebar": "Ctrl+Shift+R",
    "actionSidebarFilter": "Ctrl+Shift+F",
    "actionToggle_Mark": "Ctrl+K",
    "actionToggle_Suspend": "Ctrl+J",
    "actionTurquoise_Flag": "Ctrl+6",
    "actionUndo": "Ctrl+Z",
    "actionZoomIn": "",
    "actionZoomOut": "",
    "action_Info": "Ctrl+Shift+I",
    "action_forget": "Ctrl+Alt+N",
    "action_set_due_date": "Ctrl+Shift+D",
    "action_toggle_bury": "Ctrl+Shift+J",
    "action_toggle_mode": "Ctrl+Alt+T",
    "actionbrowsing_toggle_showing_cards_notes": ""
  }
}</code></pre>