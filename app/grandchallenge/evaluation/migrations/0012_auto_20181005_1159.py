# Generated by Django 2.0.9 on 2018-10-05 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("evaluation", "0011_auto_20181004_1008")]

    operations = [
        migrations.RenameField(
            model_name="config",
            old_name="new_results_are_public",
            new_name="auto_publish_new_results",
        ),
        migrations.RenameField(
            model_name="result", old_name="public", new_name="published"
        ),
    ]
