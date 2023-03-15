from domain.main.tools.entity.user_pqrd import UserPqrd as UserPqrdDomain
from infrastucture.tools.models.user_pqrd import UserPqrd as UserPqrdModel


class UserPqrdAcl:
    @staticmethod
    def from_model_to_domain(model: UserPqrdModel) -> UserPqrdDomain:
        return UserPqrdDomain(model.email)

    def from_models_to_domains(self, models) -> [UserPqrdDomain]:
        users: [UserPqrdDomain] = []
        for model in models:
            users.append(self.from_model_to_domain(model))
        return users
