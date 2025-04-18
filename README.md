# inprompt

A tiny CLI for outputting files or glob patterns as Markdown code blocks. Useful when
you need to copy code into prompts for large language models (e.g., ChatGPT).

## Usage

From the command line, you can do something like:

```bash
inprompt pyproject.toml '**/*.py' | pbcopy
```

- **On macOS**, `pbcopy` copies STDOUT to the clipboard.
- **On Ubuntu/Linux**, you can define aliases to replicate `pbcopy` and `pbpaste`:

  ```bash
  alias pbcopy='xclip -selection clipboard'
  alias pbpaste='xclip -selection clipboard -o'
  ```

  Then you can use the same `inprompt ... | pbcopy` pattern.

Any matched files will be printed in the format:

````markdown
<filename>
```
<file contents>
```
````

You can then paste those code blocks into an LLM prompt.

## Installation

### Option 1: With pip

```bash
pip install inprompt
```

This installs the `inprompt` command on your system or in your virtual environment.

### Option 2: With [pipx](https://pypa.github.io/pipx/)

```bash
pipx install inprompt
```

This installs `inprompt` globally, isolated from your system's site packages.

## License

[MIT License](LICENSE)
