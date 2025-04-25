# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/) and
the project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

- _Details of upcoming changes go here (if any)._

## [1.3.0] - 2025-04-25

### Added

- `--fence / -f` flag to let users choose an arbitrary Markdown fence
  delimiter (e.g. `--fence "~~~"`).

### Changed

- Minor wording corrections in documentation and log messages.

## [1.2.0] - 2025-04-21

### Changed

- Use four backticks (````) for code fences instead of three, to avoid delimiter collisions when source contains triple backticks.

## [1.1.0] - 2025-04-08

### Added

- Support for recursive glob patterns (e.g., `**/*.py`) by setting `recursive=True` in
  `glob.glob`.
- Logging added to show which file is currently being formatted (`Formatting file:
...`).

### Changed

- Updated `README.md` to clarify the importance of quoting glob patterns.

## [1.0.6] - 2025-03-22

### Changed

- Updated `README.md` file.

## [1.0.5] - 2025-03-13

### Added

- Initial release with CLI entry point.
