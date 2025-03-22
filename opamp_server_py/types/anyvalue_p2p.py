# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.1.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.4 
# Pydantic Version: 2.10.6 
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator
import typing


class ArrayValue(BaseModel):
    """
     ArrayValue is a list of AnyValue messages. We need ArrayValue as a message
 since oneof in AnyValue does not allow repeated fields.
    """

# Array of values. The array may be empty (contain 0 elements).
    values: typing.List["AnyValue"] = Field(default_factory=list)

class KeyValue(BaseModel):
    """
     KeyValue is a key-value pair that is used to store Span attributes, Link
 attributes, etc.
    """

    key: str = Field(default="")
    value: "AnyValue" = Field(default_factory=lambda : AnyValue())

class KeyValueList(BaseModel):
    """
     KeyValueList is a list of KeyValue messages. We need KeyValueList as a message
 since `oneof` in AnyValue does not allow repeated fields. Everywhere else where we need
 a list of KeyValue messages (e.g. in Span) we use `repeated KeyValue` directly to
 avoid unnecessary extra wrapping (which slows down the protocol). The 2 approaches
 are semantically equivalent.
    """

# A collection of key/value pairs of key-value pairs. The list may be empty (may
# contain 0 elements).
    values: typing.List[KeyValue] = Field(default_factory=list)

class AnyValue(BaseModel):
    """
     AnyValue is used to represent any type of attribute value. AnyValue may contain a
 primitive value such as a string or integer or it may contain an arbitrary nested
 object containing arrays, key-value lists and primitives.
    """

    _one_of_dict = {"AnyValue.value": {"fields": {"array_value", "bool_value", "bytes_value", "double_value", "int_value", "kvlist_value", "string_value"}}}
    one_of_validator = model_validator(mode="before")(check_one_of)
    string_value: str = Field(default="")
    bool_value: bool = Field(default=False)
    int_value: int = Field(default=0)
    double_value: float = Field(default=0.0)
    array_value: ArrayValue = Field(default_factory=ArrayValue)
    kvlist_value: KeyValueList = Field(default_factory=KeyValueList)
    bytes_value: bytes = Field(default=b"")
