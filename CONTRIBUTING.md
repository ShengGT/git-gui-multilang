# Contributing

Thanks for helping make Git GUI usable in more languages.

## Report a bad translation

Please include:

- locale code (for example fr, zh_tw, my);
- the English source string;
- what Git GUI currently shows;
- what it should say;
- a screenshot if possible.

Open an issue with the title: [locale] short description.

## Fix a translation

1. Edit the matching file in msgs/<locale>.msg.
2. Keep every printf placeholder exactly: %s, %d, %i, %1$s, %*i, %%.
3. Escape Tcl special characters in the destination string: quote, backslash, dollar, square brackets.
4. Keep the file UTF-8 without BOM.
5. Test it:

       set LANG=<locale>
       git gui

6. Open a pull request with the locale code in the title.

## Add a new locale

1. Copy an existing .msg file to msgs/<locale>.msg.
2. Replace the locale token in every ::msgcat::mcset line.
3. Translate the strings.
4. Add the locale to languages.json and 语言覆盖与质量.md.
5. Test with Tcl msgcat or with git gui.

## Quality bar

- No broken placeholders.
- No mixed scripts unless the target language legitimately uses them.
- Technical terms should stay consistent with the rest of the file.
- When unsure, leave the English source and comment the line with ## instead of guessing.
