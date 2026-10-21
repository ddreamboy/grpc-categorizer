# gRPC Categorizer

A mock text categorization service built with gRPC and Protocol Buffers

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- GNU Make (for running development commands)
- Git (for pre-commit hooks)

## Installation

Install project dependencies, including development tools:

```bash
uv sync
```

To install only production dependencies, without development tools:

```bash
uv sync --no-dev
```

## Generate gRPC Code

Generate Python code from the `.proto` definition:

```bash
uv run python -m grpc_tools.protoc -Iinfrastructure/grpc/generated=protos --python_out=. --pyi_out=. --grpc_python_out=. infrastructure/grpc/generated/categorizer.proto
```

The command generates the following files:

- `categorizer_pb2.py`- Protocol Buffers message classes.
- `categorizer_pb2.pyi`- type stubs for static analysis.
- `categorizer_pb2_grpc.py`- gRPC client and service classes.

## Running the Service

### 1. Start the server

In the first terminal, run:

```bash
uv run python main.py
```

### 2. Run the client

In a second terminal, run:

```bash
uv run python client.py
```

The client sends a request to the running gRPC server and receives the categorization results.

## Development

The project uses Ruff for linting and formatting, mypy for static type checking, and pre-commit to run checks before each commit.

### Run checks

```bash
make check
```

This runs:
- Ruff lint checks
- Ruff formatting checks
- mypy type checks

### Format code

```bash
make format
```

This automatically fixes supported lint issues, sorts imports, and formats Python files.

### Install pre-commit hooks

```bash
uv run pre-commit install
```

After installation, `make check` runs automatically before each commit. Commits are rejected if checks fail.

## Project Structure

```text
├── protos/
│   └── categorizer.proto
├── infrastructure/
│   └── grpc/
│       ├── generated/
│       │   ├── categorizer_pb2.py
│       │   ├── categorizer_pb2.pyi
│       │   └── categorizer_pb2_grpc.py
│       ├── servicer.py
│       └── server.py
├── main.py
├── client.py
├── Makefile
├── .pre-commit-config.yaml
├── pyproject.toml
└── uv.lock
```