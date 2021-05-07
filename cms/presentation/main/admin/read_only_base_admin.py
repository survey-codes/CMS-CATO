from cms.presentation.main.admin.audit_admin import AuditAdmin

VALUE_TRUE = True
VALUE_FALSE = False
SHOW_SAVE_AND_CONTINUE = "show_save_and_continue"


class ReadOnlyBaseAdmin(AuditAdmin):

    def has_add_permission(self, request):
        return VALUE_FALSE

    def has_change_permission(self, request, obj=None):
        return VALUE_TRUE

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            SHOW_SAVE_AND_CONTINUE: VALUE_FALSE
        })
        return super(ReadOnlyBaseAdmin, self).render_change_form(request, context, add, change, form_url, obj)
