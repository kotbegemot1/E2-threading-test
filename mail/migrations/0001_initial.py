# Generated by Django 3.0.4 on 2020-04-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(db_index=True, max_length=50)),
                ('text', models.TextField()),
                ('mail_adress', models.EmailField(max_length=254)),
                ('delay', models.SmallIntegerField()),
                ('is_send', models.BooleanField()),
            ],
        ),
    ]
