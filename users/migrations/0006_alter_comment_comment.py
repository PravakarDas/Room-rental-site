# Generated by Django 4.2.1 on 2023-11-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_comment_dormroom_delete_dormrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
