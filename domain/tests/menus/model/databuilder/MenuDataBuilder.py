from domain.main.menus.entity.menu import Menu


class MenuDataBuilder:
    __pk = 1
    __name = "Home"
    __metadata = ""
    __is_general = True

    def with_pk(self, pk: property) -> 'MenuDataBuilder':
        self.__pk = pk
        return self

    def with_name(self, name: str) -> 'MenuDataBuilder':
        self.__name = name
        return self

    def build(self) -> Menu:
        return Menu(
            pk=self.__pk,
            name=self.__name,
            metadata=self.__metadata,
            is_general=self.__is_general,
        )
