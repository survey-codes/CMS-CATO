class Base:

    @staticmethod
    def _validate_field_none(*args):
        fields = ()
        for field in args:
            fields += field if field else ()
        return fields
