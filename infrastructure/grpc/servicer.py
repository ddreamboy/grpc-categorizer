"""gRPC service implementation for text categorization."""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from infrastructure.grpc.generated.categorizer_pb2 import (
    CategoryRequest,
    CategoryResponse,
)

if TYPE_CHECKING:
    import grpc

from infrastructure.grpc.generated.categorizer_pb2_grpc import (
    CategorizerServiceServicer,
)


class CategorizerServicer(CategorizerServiceServicer):
    """Implement the categorizer gRPC service."""

    @override
    def Categorize(
        self, request: CategoryRequest, context: grpc.ServicerContext
    ) -> CategoryResponse:
        """Return a dummy category for every requested text.

        Args:
            request: Categorization request containing the input texts.
            context: gRPC context for the current request.

        Returns:
            A response containing one dummy category per input text.
        """
        return CategoryResponse(
            categories=[
                CategoryResponse.Category(
                    index=text.index,
                    success=CategoryResponse.Category.Success(
                        category_name='dummy_category', confidence=0.0
                    ),
                )
                for text in request.texts
            ]
        )
