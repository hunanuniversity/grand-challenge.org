# Generated by Django 2.0.6 on 2018-06-07 12:50

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import grandchallenge.core.models
import grandchallenge.evaluation.validators
import social_django.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(help_text='Tar archive of the container image produced from the command `docker save IMAGE > IMAGE.tar`. See https://docs.docker.com/engine/reference/commandline/save/', upload_to=grandchallenge.core.models.docker_image_path, validators=[grandchallenge.evaluation.validators.ExtensionValidator(allowed_extensions=('.tar',))])),
                ('image_sha256', models.CharField(editable=False, max_length=71)),
                ('ready', models.BooleanField(default=False, editable=False, help_text='Is this image ready to be used?')),
                ('status', models.TextField(editable=False)),
                ('description_html', ckeditor.fields.RichTextField(blank=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'The task is waiting for execution'), (1, 'The task has been started'), (2, 'The task is to be retried, possibly because of failure'), (3, 'The task raised an exception, or has exceeded the retry limit'), (4, 'The task executed successfully'), (5, 'The task was cancelled')], default=0)),
                ('status_history', social_django.fields.JSONField(default=dict)),
                ('output', models.TextField()),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algorithms.Algorithm')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.Case')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('output', social_django.fields.JSONField(default=dict)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algorithms.Job')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
