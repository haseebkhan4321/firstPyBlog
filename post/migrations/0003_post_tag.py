# Generated by Django 5.0.4 on 2024-04-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_category'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='tag.tag'),
        ),
    ]