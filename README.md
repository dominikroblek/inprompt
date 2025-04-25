# inprompt

A tiny CLI that prints files or glob patterns as Markdown‐formatted code blocks.
Handy for pasting source into prompts for large language models.

## Usage

From the command line, you can pass files and glob patterns to `inprompt`:

```bash
inprompt pyproject.toml '**/*.py' | pbcopy
```

**Note:** It's important to enclose glob patterns (like `'**/*.py'`) in single or double
quotes. This prevents your shell from expanding the pattern before `inprompt` sees it,
ensuring correct file matching, especially for recursive patterns (`**`).

The `| pbcopy` (or equivalent) then pipes the formatted output directly to your
clipboard:

- **On macOS**, `pbcopy` copies STDOUT to the clipboard.
- **On Ubuntu/Linux**, you can use `xclip`. Define aliases for convenience:

  ```bash
  alias pbcopy='xclip -selection clipboard'
  alias pbpaste='xclip -selection clipboard -o'
  ```

  Then you can use the same `inprompt ... | pbcopy` pattern.

Any matched files will be printed to standard output (and thus copied by `pbcopy`) in
the format:

`````markdown
<filename>
````         ← configurable with --fence / -f
<file contents>
````
`````

## Installation

````bash
pip install inprompt
```

## License

[MIT License](LICENSE)
````
