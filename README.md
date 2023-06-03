# Modify shortcuts

Anki ([GitHub](https://github.com/ankitects/anki)) addon ([GitHub](https://github.com/TRIAEIOU/modify-shortcuts)) to automatically detect core Anki shortcuts and allow modifcation.

This addon is inspired by [Liresol](https://github.com/Liresol)'s excellent addon [Customize Keyboard Shortcuts](https://ankiweb.net/shared/info/24411424) which is **a more complete addon**.

## Background

This addon tries to automatically detect any core Anki python shortcuts (i.e. not in a WebView/JavaScript-side) and allow you to modify those. The advantage of this approach is that if core Anki adds/changes shortcuts those will be automatically detected without a need for addon update. Note that the detection logic is not infallible, right now it will only detect shortcuts for the main window (although not shortcuts from the toolbar), browser and add note window.

## Use

Open all windows once to allow the addon to try to detect shortcuts, then override/remove shortcut bindings in `Main window → Tools → Add-ons → Modify shortcuts → Config`. The help on the right will list detected shortcuts, add those you want to change to the configuration. Example:

```json
{
  "main window": {    
    "actionAbout": "Ctrl+Alt+A", // comma between items
    "actionAdd_ons": "" // empty string will remove the default shortcut
  },
  "browser": {
    "action_toggle_bury": ""
  }
}
```