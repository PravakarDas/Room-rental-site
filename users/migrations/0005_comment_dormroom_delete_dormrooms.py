# Generated by Django 4.2.1 on 2023-11-17 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_dormrooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.register')),
            ],
        ),
        migrations.CreateModel(
            name='DormRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('popularity', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('link', models.URLField()),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.comment')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.register')),
            ],
        ),
        migrations.DeleteModel(
            name='DormRooms',
        ),
    ]
