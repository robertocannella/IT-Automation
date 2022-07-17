# Bash Scripting Resources

This file used for Bash scripting snippets and techniques as well as links to online resources.

* [ryanstutorials](https://ryanstutorials.net/bash-scripting-tutorial/)
* [linuxconfig](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
* [shellscript](https://www.shellscript.sh)
<hr>


## Utilities

Some shell scripting utilities
`zenity <`(https://help.gnome.org/users/zenity/stable/index.html.en) : When you write scripts, you can use Zenity to create simple dialogs that interact graphically with the user, as follows:

    ```
    zenity --file-selection
    zenity --calendary
    zenity --entry
    ```

You can create a dialog to obtain information from the user. For example, you can prompt the user to select a date from a calendar dialog, or to select a file from a file selection dialog.

You can create a dialog to provide the user with information. For example, you can use a progress dialog to indicate the current status of an operation, or use a warning message dialog to alert the user.

When the user closes the dialog, Zenity prints the text produced by the dialog to standard output. [more...](https://help.gnome.org/users/zenity/stable/index.html.en)