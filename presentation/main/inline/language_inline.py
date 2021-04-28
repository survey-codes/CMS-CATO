from presentation.main.inline.audit_inline import AuditInline


class LanguageInline(AuditInline):
    __LANGUAGE_KEY = "language"

    __fields_default = (__LANGUAGE_KEY,)

    def get_fields(self, request, obj=None):
        fields = super(LanguageInline, self).get_fields(request, obj)
        return self._validate_field_none(self.__fields_default, self.fields, fields)
