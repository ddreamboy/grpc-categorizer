"""gRPC client for the categorizer service."""

import grpc

from infrastructure.grpc.generated.categorizer_pb2 import (
    CategoryRequest,
    CategoryResponse,
)
from infrastructure.grpc.generated.categorizer_pb2_grpc import (
    CategorizerServiceStub,
)


def run() -> None:
    """Send a sample categorization request and print the results."""
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CategorizerServiceStub(channel)
        response: CategoryResponse = stub.Categorize(
            CategoryRequest(
                model_name='FastText',
                texts=[
                    {'index': index, 'text': 'dummy_text'} for index in range(5)
                ],
            )
        )

        for category in response.categories:
            result_type = category.WhichOneof('result')

            if result_type == 'success':
                print(
                    category.index,
                    category.success.category_name,
                    category.success.confidence,
                )
            elif result_type == 'failure':
                print(
                    category.index,
                    category.failure.code,
                    category.failure.details,
                )


if __name__ == '__main__':
    run()
