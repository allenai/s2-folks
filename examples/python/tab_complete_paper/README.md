This example creates a command line tool which supports tab completion to turn a partial title
into its page on semanticscholar.org


## Setup ##

Tab completion is implemented through the [click python library].
Click supports tab completion for bash, zsh, and fish.

If you use zsh, this is how to install and activate the tool for the current shell.
```
pip install --editable .
eval "$(_PAPER_URL_COMPLETE=zsh_source paper-url)"
rehash  # needed when new commands are added to the PATH
```

Activating completions for bash or fish is similar. See [click shell completion docs]

[click python library]: https://click.palletsprojects.com/en/8.1.x/
[click shell completion docs]: https://click.palletsprojects.com/en/8.1.x/shell-completion/#enabling-completion


## Example ##

Once the `paper-url` command is available and plugged in for tab completion, here's an example usage

```

```
