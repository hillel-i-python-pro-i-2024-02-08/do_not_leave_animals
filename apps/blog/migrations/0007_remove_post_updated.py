# Generated by Django 5.0.6 on 2024-07-05 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
    ]
