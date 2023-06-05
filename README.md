# Override shortcuts

Anki ([GitHub](https://github.com/ankitects/anki)) addon ([GitHub](https://github.com/TRIAEIOU/override-shortcuts)) to automatically detect shortcuts and allow overriding.

This addon is inspired by [Liresol](https://github.com/Liresol)'s excellent addon [Customize Keyboard Shortcuts](https://ankiweb.net/shared/info/24411424) which is **a much more complete addon**. Among other things [Customize Keyboard Shortcuts](https://ankiweb.net/shared/info/24411424) allows editing of some WebView shortcuts (the editor toolbar buttons) which `Override shortcuts` does not do.

## Background

This addon tries to automatically detect any "python side" shortcuts (i.e. not in a WebView/JavaScript-side) and allow overriding. This will include some shortcuts installed by other addons. This approach will automatically detect any new/modified shortcuts without a need for addon update. Note that the detection logic is not infallible, nor does it always output user friendly values. Example: `"AnkiQt": {"QShortcut (A): "A"}` is in fact the shortcut to open the "Add note" window from the "Main" window, the user needs to figure out what to change.

## Use

Open all windows once to allow the addon to try to detect shortcuts (QAction and QShortcut), then override/remove bindings in `Main window → Tools → Add-ons → Override shortcuts → Config`. The help on the right will list detected shortcuts, add those to the configuration to override. Example:

```json
{
  "AnkiQt": {
    "QtClassProxy: action-actionAbout": "Ctrl+Alt+A", // comma between items
    "QtClassProxy: action-actionAdd_ons": "" // empty string will remove binding
  }, // comma between windows
  "Browser": {
    "QtClassProxy: action_toggle_bury": ""
  }
}
```

A few remarks regading the naming to facilitate identifying which entry to override:

- The firt part is the class (for some reason Qt returns `QtClassProxy` for the `QAction` class).
- `<class>: <name>`: Shortcut of `class` with `name` (often fairly descriptive)
- `<class> (<key sequence>)`: Shortcut of `class` without name and `key sequence` registered (i.e. possible to look up in documentation what that sequence does).
- `<class>-<number>`: Shortcut of `class` without name nor "default", `number` is a sequence identifier, the only way to find out what it does is to map it to a key and try (prefer doing this on a test profile).

## Important

The addon only detects actions and shortcuts and allow you to override them, it makes no assurances that this is suitable. Adding a shortcut to something like `"QtClassProxy-1": ""` may result in unwanted effects when activated (there may be a reason no key sequence is connected to the action). It is recommended to try out such things in a separate test profile to avoid deck corruption.