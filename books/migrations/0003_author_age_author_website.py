# Generated by Django 4.1.7 on 2023-03-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_publisher_user_bookinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='website',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
    ]