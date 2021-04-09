from import_export import resources
# from import_export.fields import Field

from domain.entities.contents.models import Post, PostLanguage


class ExportPostResource(resources.ModelResource):
    # parent = Field(attribute='parent__id', column_name='parent')
    class Meta:
        model = Post
        fields = (
            'id',
            'created_by__username',
            'updated_by__username',
            'active',
            'title_post',
            'logo',
            'parent',
            'slug_post',
            'section',
        )
        export_order = fields


class PostLanguageResource(resources.ModelResource):
    class Meta:
        model = PostLanguage
        skip_unchanged = True
        report_skipped = True


class ImportPostResource(resources.ModelResource):
    class Meta:
        model = Post
        skip_unchanged = True
        report_skipped = True
        fields = ('id', 'active', 'title_post', 'section')
