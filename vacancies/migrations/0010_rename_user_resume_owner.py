# Generated by Django 3.2.2 on 2021-06-10 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0009_alter_resume_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='user',
            new_name='owner',
        ),
    ]
