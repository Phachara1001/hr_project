# Generated by Django 4.2.6 on 2023-11-16 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0002_person_p_contract_person_p_email_person_p_facebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='p_worktear',
            new_name='p_workyear',
        ),
    ]