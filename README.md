
# AgentGuard AI

AI-powered GitHub Pull Request Security Reviewer.

AgentGuard AI aims to review pull request changes, identify potential
security vulnerabilities, validate findings, and detect possible regressions.

## Project Status

Early development.

## Planned Features

- GitHub pull request integration
- NVIDIA open-source model through Nebius
- AI-assisted code review
- Security checks and finding validation
- Automated regression testing
- Configurable CI review gate
- Evaluation of review quality

## Tech Stack

- Python
- pytest
- Ruff
- Nebius Token Factory
- NVIDIA open-source model
- GitHub Actions

## Development Setup

Python 3.11 or newer is required.

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows CMD:

```bat
.venv\Scripts\activate
```

Install development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run tests:

```bash
python -m pytest
```

## Security

Never commit API keys, access tokens, passwords, or `.env` files.

## License

To be determined.
python -m pip install -e ".[dev]"