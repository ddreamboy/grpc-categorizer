"""Application entry point for the gRPC categorizer server."""

import logging

from infrastructure.grpc.server import serve

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

if __name__ == "__main__":
    import anyio

    anyio.run(serve, backend="asyncio")
