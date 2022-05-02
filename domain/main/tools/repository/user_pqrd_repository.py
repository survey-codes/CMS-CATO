from domain.main.tools.entity.user_pqrd import UserPqrd


class UserPqrdRepository:

    def select(self) -> [UserPqrd]:
        pass

    def select_by_ids(self, ids: list):
        pass

    def there_are_active_users(self):
        pass

    # def create(self, email: str) -> Response:
    #     pass
