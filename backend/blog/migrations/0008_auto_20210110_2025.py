# Generated by Django 3.1.5 on 2021-01-10 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_ahtuor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ahtuor',
            new_name='author',
        ),
    ]
