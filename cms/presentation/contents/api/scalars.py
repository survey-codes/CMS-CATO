from graphene.types import Scalar
from graphql.language import ast


class JSONCustom(Scalar):
    """
    JSONCustom Scalar
    """

    @staticmethod
    def serialize(dt):
        return dt

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return node.value

    @staticmethod
    def parse_value(value):
        return value
