# Override shortcuts

Anki ([GitHub](https://github.com/ankitects/anki)) addon ([GitHub](https://github.com/TRIAEIOU/override-shortcuts)) to automatically detect shortcuts and allow overriding.

This addon is inspired by [Liresol](https://github.com/Liresol)'s excellent addon [Customize Keyboard Shortcuts](https://ankiweb.net/shared/info/24411424) which is **a much more complete addon**. Among other things [Customize Keyboard Shortcuts](https://ankiweb.net/shared/info/24411424) allows editing of some WebView shortcuts (the editor toolbar buttons) which `Override shortcuts` does not do.

## Background

This addon tries to automatically detect any "python side" shortcuts (i.e. not in a WebView/JavaScript-side) and allow overriding. This will include some shortcuts installed by other addons, as long as that addon is loaded before `Override shortcuts`. This approach will automatically detect any new/modified core Anki shortcuts without a need for addon update. Note that the detection logic is not infallible, nor does it always output user friendly values. Example: `"aqt.main.AnkiQt": {"shortcut-unnamed-A": "A"}` is in fact the shortcut to open the "Add note" window from the "Main" window, the user needs to figure out what to change.

## Use

Open all windows once to allow the addon to try to detect shortcuts, then override/remove shortcut bindings in `Main window → Tools → Add-ons → Override shortcuts → Config`. The help on the right will list detected shortcuts, add those to the configuration to override. Example:

```json
{
  "aqt.main.AnkiQt": {    
    "action-actionAbout": "Ctrl+Alt+A", // comma between items
    "action-actionAdd_ons": "" // empty string will remove the default shortcut
  }, // comma between windows
  "aqt.browser.browser.Browser": {
    "action-action_toggle_bury": ""
  }
}
```

## Important

The addon only detects actions and shortcuts and allow you to override them, it makes no assurances that this is suitable. Adding a shortcut to something like `"action-unnamed-[1]": ""` may result in unwanted effects when activated (there may be a reason no shortcut is connected to the action). It is recommended to try out such things in a separate test profile to avoid deck corruption.