"""inprompt: CLI to output files as Markdown code blocks for LLM prompts.

It uses four backticks (````) for code fences instead of three, to avoid delimiter
collisions when source contains triple backticks.

Example usage:
    inprompt path/to/file.py '**/*.py' | pbcopy
"""

import glob
from pathlib import Path

from absl import app
from loguru import logger


def print_usage() -> None:
    """Log usage info."""
    logger.info("Usage: inprompt <files or patterns> [<files or patterns> ...]")
    logger.info("Example: inprompt my_script.py '**/*.py' | pbcopy")


def match_file_patterns(patterns: list[str]) -> list[str]:
    """Glob patterns and return sorted, unique matches.

    Args:
        patterns: Glob patterns.

    Returns:
        De-duplicated, sorted filenames.
    """
    filenames = []
    for pattern in patterns:
        matched_files = sorted(glob.glob(pattern, recursive=True))
        if not matched_files:
            logger.warning("No files matched pattern: {}", pattern)
        filenames.extend(matched_files)
    # Preserve order while removing duplicates
    return list(dict.fromkeys(filenames))


def read_and_format_source_code(filename: str) -> str:
    """Return file contents as a Markdown code fence.

    Args:
        filename: Path to the file.

    Returns:
        Markdown code fence string.

    Raises:
        FileNotFoundError: If filename does not exist.
    """
    path = Path(filename)
    try:
        content = path.read_text(encoding="utf-8").rstrip()
    except FileNotFoundError:
        logger.error("File not found: {}", filename)
        raise

    logger.info("Formatting file: {}", filename)
    return f"{filename}\n````\n{content}\n````"


def main(argv: list[str]) -> int:
    """CLI entry point.

    Args:
        argv: Command-line arguments (argv[0] is the program name).

    Returns:
        Exit code.
    """
    if len(argv) < 2:
        logger.error("No files or file patterns specified.")
        print_usage()
        return 2

    file_patterns = argv[1:]
    filenames = match_file_patterns(file_patterns)

    if not filenames:
        logger.error("No matching files found.")
        return 3

    formatted_contents = [read_and_format_source_code(fname) for fname in filenames]

    # Emit the markdown to STDOUT.
    print("\n\n".join(formatted_contents))

    logger.info("Formatted and outputted {} files.", len(filenames))
    return 0


def run() -> None:
    """Console script entry point."""
    app.run(main)


if __name__ == "__main__":
    run()
