# Generated by Django 3.0.2 on 2020-03-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='to_do_list',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
