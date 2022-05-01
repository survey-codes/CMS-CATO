from enum import Enum


class  TypeResponse(Enum):
    SUCCESS = (200, "Success")
    FAIL = (2, "We have problems saving the information")

    def __new__(cls, code: int, message:str):
        type_response = object.__new__(cls)
        type_response._value_ = code
        type_response.message = message
