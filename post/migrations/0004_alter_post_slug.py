# Generated by Django 5.0.4 on 2024-04-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(editable=False, max_length=255, unique=True),
        ),
    ]