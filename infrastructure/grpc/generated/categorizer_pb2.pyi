from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CategoryRequest(_message.Message):
    __slots__ = ("model_name", "texts")
    class Text(_message.Message):
        __slots__ = ("index", "text")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        index: int
        text: str
        def __init__(self, index: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXTS_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    texts: _containers.RepeatedCompositeFieldContainer[CategoryRequest.Text]
    def __init__(self, model_name: _Optional[str] = ..., texts: _Optional[_Iterable[_Union[CategoryRequest.Text, _Mapping]]] = ...) -> None: ...

class CategoryResponse(_message.Message):
    __slots__ = ("categories",)
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_UNSPECIFIED: _ClassVar[CategoryResponse.ErrorCode]
        ERROR_CODE_EMPTY_TEXT: _ClassVar[CategoryResponse.ErrorCode]
        ERROR_CODE_TEXT_TOO_LONG: _ClassVar[CategoryResponse.ErrorCode]
        ERROR_CODE_NOT_CLASSIFIED: _ClassVar[CategoryResponse.ErrorCode]
        ERROR_CODE_INTERNAL: _ClassVar[CategoryResponse.ErrorCode]
    ERROR_CODE_UNSPECIFIED: CategoryResponse.ErrorCode
    ERROR_CODE_EMPTY_TEXT: CategoryResponse.ErrorCode
    ERROR_CODE_TEXT_TOO_LONG: CategoryResponse.ErrorCode
    ERROR_CODE_NOT_CLASSIFIED: CategoryResponse.ErrorCode
    ERROR_CODE_INTERNAL: CategoryResponse.ErrorCode
    class Category(_message.Message):
        __slots__ = ("index", "success", "failure")
        class Success(_message.Message):
            __slots__ = ("category_name", "confidence")
            CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
            CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
            category_name: str
            confidence: float
            def __init__(self, category_name: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...
        class Failure(_message.Message):
            __slots__ = ("code", "details")
            CODE_FIELD_NUMBER: _ClassVar[int]
            DETAILS_FIELD_NUMBER: _ClassVar[int]
            code: CategoryResponse.ErrorCode
            details: str
            def __init__(self, code: _Optional[_Union[CategoryResponse.ErrorCode, str]] = ..., details: _Optional[str] = ...) -> None: ...
        INDEX_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        index: int
        success: CategoryResponse.Category.Success
        failure: CategoryResponse.Category.Failure
        def __init__(self, index: _Optional[int] = ..., success: _Optional[_Union[CategoryResponse.Category.Success, _Mapping]] = ..., failure: _Optional[_Union[CategoryResponse.Category.Failure, _Mapping]] = ...) -> None: ...
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[CategoryResponse.Category]
    def __init__(self, categories: _Optional[_Iterable[_Union[CategoryResponse.Category, _Mapping]]] = ...) -> None: ...
