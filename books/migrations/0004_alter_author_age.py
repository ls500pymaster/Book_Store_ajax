# Generated by Django 4.1.7 on 2023-03-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_author_age_author_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
