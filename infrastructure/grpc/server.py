"""gRPC server lifecycle management."""

import logging
import signal

import anyio
import grpc

from infrastructure.grpc.generated.categorizer_pb2_grpc import (
    add_CategorizerServiceServicer_to_server,
)
from infrastructure.grpc.servicer import CategorizerServicer

logger = logging.getLogger(__name__)


async def serve() -> None:
    """Start the gRPC server and stop it after a termination signal."""
    server = grpc.aio.server()

    add_CategorizerServiceServicer_to_server(
        CategorizerServicer(),
        server,
    )

    port = server.add_insecure_port("[::]:50051")
    if port == 0:
        raise RuntimeError("Failed to bind gRPC server port")

    await server.start()
    logger.info("gRPC server started on port %s", port)

    with anyio.open_signal_receiver(signal.SIGINT, signal.SIGTERM) as signals:
        try:
            async for signum in signals:
                logger.info("Received signal %s, shutting down", signum)
                break
        finally:
            with anyio.CancelScope(shield=True):
                await server.stop(grace=5)

    logger.info("gRPC server stopped")
