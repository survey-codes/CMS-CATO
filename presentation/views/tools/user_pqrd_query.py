from graphene import ObjectType, Field, String

from domain.main.common.aggregate.response import Response
from presentation.presenter.tools.user_pqrd_presenter import UserPqrdPresenter


class UserPqrdQuery(ObjectType):
    response = Field(Response, email=String())

    def resolve_response(self, info, email, **kwargs):
        user_pqrd_presenter = UserPqrdPresenter()
        return user_pqrd_presenter.create(email)
