from domain.entity.page import Page


class PageRepository:
    def select(self, lang: str, slug: str) -> [Page]:
        pass

    def select_children_by_pk(self, pk: property) -> [int]:
        pass
