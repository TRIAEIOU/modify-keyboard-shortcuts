# Override shortcuts

Anki ([GitHub](https://github.com/ankitects/anki)) addon ([GitHub](https://github.com/TRIAEIOU/modify-shortcuts)) to automatically detect shortcuts and allow overriding.

This addon is inspired by [Liresol](https://github.com/Liresol)'s excellent addon [Customize Keyboard Shortcuts](https://ankiweb.net/shared/info/24411424) which is **a much more complete addon**. Among other things [Customize Keyboard Shortcuts](https://ankiweb.net/shared/info/24411424) allows editing of some WebView shortcuts (the editor toolbar buttons) which `Override shortcuts` does not do.

## Background

This addon tries to automatically detect any "python side" shortcuts (i.e. not in a WebView/JavaScript-side) and allow you to overriding them. This will include some shortcuts installed by other addons, as long as that addon is loaded before `Override shortcuts`. The advantage of this approach is that any new/modified core Anki shortcuts will be automatically detected without a need for addon update. Note that the detection logic is not infallible, nor does it always output user friendly values. Example: `"main window": {"shortcut-unnamed-A": "A"}` is in fact the shortcut to open the "Add note" window from the "Main" window, you will have to figure what you want to change.

## Use

Open all windows once to allow the addon to try to detect shortcuts, then override/remove shortcut bindings in `Main window → Tools → Add-ons → Override shortcuts → Config`. The help on the right will list detected shortcuts, add those you want to change to the configuration. Example:

```json
{
  "main window": {    
    "action-actionAbout": "Ctrl+Alt+A", // comma between items
    "action-actionAdd_ons": "" // empty string will remove the default shortcut
  }, // comma between windows
  "browser": {
    "action-action_toggle_bury": ""
  }
}
```

## Important

The addon only detects actions and shortcuts and allow you to override them, it makes no assurances that this is suitable. Adding a shortcut to something like `"action-unnamed-[1]": ""` may result in unwanted effects when activated (there may be a reason no shortcut is connected to the action), I suggest trying out such things on a separate test profile to avoid deck corruption.