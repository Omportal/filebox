# Generated by Django 4.1.1 on 2022-09-28 08:09

import apps.content_app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('upload', models.FileField(upload_to=apps.content_app.models.user_directory_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='content', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
