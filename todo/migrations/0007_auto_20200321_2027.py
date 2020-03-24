# Generated by Django 3.0.2 on 2020-03-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20200321_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_do_list', models.CharField(max_length=100)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]