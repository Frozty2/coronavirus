# Generated by Django 3.0.2 on 2020-03-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todo', '0004_delete_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_do_list', models.CharField(max_length=100)),
            ],
        ),
    ]
