# Generated by Django 4.2.1 on 2023-06-11 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appKozmetik', '0012_comment_date_comment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
    ]