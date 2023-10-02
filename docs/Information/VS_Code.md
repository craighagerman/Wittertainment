# VS Code Notes
(TODO:  Move file away elsewhere)

VS Code uses TextMate rules for syntax highlighting. Markdown syntax highlighting can be altered by using this in user settings.


see:  (TextMateRules)[https://github.com/gwenzek/sublime-syntax-manifesto/blob/master/TextMateRules.md]


Shift-CMD-P > select "Preferences Open User Settings (Json)" search for "editor.tokenColorCustomizations"

Edit like this (for the Dark+ theme):

```json
  "editor.tokenColorCustomizations": {
    "comments": "#778899",
    "[Default Dark+]": {
      "textMateRules": [
        {
          "scope": "markup.inline.raw.string.markdown",
          "settings": {
            "foreground": "#aaff00"
          },
          "scope": "markup.quote.markdown",
          "settings": {
            "foreground": "#b5f4c3",
            "fontStyle": "bold"
          }
        }
      ]
    }
  },
```