from typing import TypeVar, Generic

Model = TypeVar('Model')
Domain = TypeVar('Domain')


class BaseAcl(Generic[Model, Domain]):
    def from_model_to_domain(self, model: Model) -> Domain:
        pass

    def from_models_to_domains(self, models: [Model]) -> [Domain]:
        pass
