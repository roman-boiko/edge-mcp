# Edge MCP Sense HAT Agent

This project provides a cross-platform agent and server for interacting with the Raspberry Pi Sense HAT, supporting both real hardware and a mock interface for development on macOS and other non-Raspberry Pi systems.

## Features

- Query temperature, humidity, and pressure from the Sense HAT (real or mock).
- Display messages on the Sense HAT LED matrix (mock prints to console).
- Interactive agent loop for user prompts.
- Modular structure for easy extension.

## Project Structure

```
main.py
pyproject.toml
README.md
uv.lock
agent/
    sensehatagent.py
sense_hat_mock/
    sense_hat.py
    __init__.py
server/
    sensehatmcp.py
```

## Requirements

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (for dependency management and running Python scripts)
- [pydantic_ai](https://github.com/pydantic/pydantic-ai) and dependencies

## Setup

1. Install dependencies using uv:
    ```bash
    uv pip install -r requirements.txt
    ```
    Or, if using pyproject.toml:
    ```bash
    uv pip install -r pyproject.toml
    ```

2. (Optional) If running on macOS or without a real Sense HAT, the mock will be used automatically.

## Usage

### Start the Agent

```bash
uv run agent/sensehatagent.py
```

You will be prompted to enter commands. Type your prompt (e.g., "get temperature") or type `exit` to quit.

### Start the MCP Server Directly

```bash
uv run server/sensehatmcp.py
```

## Customization

- To add new tools or capabilities, extend `server/sensehatmcp.py` with new `@mcp.tool()` functions.
- The mock implementation in `sense_hat_mock/sense_hat.py` can be modified for more advanced simulation.

## License

MIT License
