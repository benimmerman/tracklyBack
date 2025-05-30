# Generated by Django 5.1.7 on 2025-05-02 14:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist_app', '0006_rename_user_lists_username_listitems_isdone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitems',
            name='createdBy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='listitems',
            name='createdWhen',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='listitems',
            name='lastModified',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='listitems',
            name='lastModifiedBy',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='lists',
            name='createdWhen',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='lists',
            name='lastModified',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='lists',
            name='lastModifiedBy',
            field=models.IntegerField(null=True),
        ),
    ]
