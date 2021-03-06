# Generated by Django 2.2.3 on 2021-04-09 22:05 Updated by nigga 2021-03-14 14:17

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'verbose_name': 'Menu item', 'verbose_name_plural': 'Menu items'},
        ),
        migrations.AlterModelOptions(
            name='menuitemlanguage',
            options={'verbose_name': 'Menu item language', 'verbose_name_plural': 'Menu item languages'},
        ),
        migrations.AlterModelOptions(
            name='menulanguage',
            options={'verbose_name': 'Menu language', 'verbose_name_plural': 'Menu languages'},
        ),
        migrations.RemoveField(
            model_name='menu',
            name='general',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='page_url',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='slug_url',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='url',
        ),
        migrations.RemoveField(
            model_name='menuitemlanguage',
            name='menu_item_metadata',
        ),
        migrations.RemoveField(
            model_name='menulanguage',
            name='menu_metadata',
        ),
        migrations.AddField(
            model_name='menu',
            name='is_general',
            field=models.BooleanField(default=False, verbose_name='Is a general menu'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='link',
            field=models.CharField(blank=True, max_length=255, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='menuitemlanguage',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AddField(
            model_name='menulanguage',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AddField(
            model_name='menulanguage',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Menu name'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_created_by_set', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Menu name'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_updated_by_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuitem_created_by_set', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menus.Menu', verbose_name='Menu'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Item name'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menus.MenuItem', verbose_name='Menu item parent'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuitem_updated_by_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AlterField(
            model_name='menuitemlanguage',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Languages'),
        ),
        migrations.AlterField(
            model_name='menuitemlanguage',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='menus.MenuItem'),
        ),
        migrations.AlterField(
            model_name='menuitemlanguage',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Item name'),
        ),
        migrations.AlterField(
            model_name='menulanguage',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tools.Language', verbose_name='Languages'),
        ),
        migrations.AlterField(
            model_name='menulanguage',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='menus.Menu'),
        ),
    ]
