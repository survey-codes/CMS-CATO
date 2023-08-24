from graphene import ObjectType, Int, String, List


class PostDto(ObjectType):
    pk = Int()
    title = String()
    logo = String()
    icon = String()
    link = String()
    slug = String()
