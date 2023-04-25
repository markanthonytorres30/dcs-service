from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TodoRequest(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: str
    def __init__(self, request: _Optional[str] = ...) -> None: ...

class TodoResponse(_message.Message):
    __slots__ = ["deleted", "done", "id", "task"]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    deleted: str
    done: str
    id: str
    task: str
    def __init__(self, id: _Optional[str] = ..., task: _Optional[str] = ..., done: _Optional[str] = ..., deleted: _Optional[str] = ...) -> None: ...
