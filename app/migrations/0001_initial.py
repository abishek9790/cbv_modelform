# Generated by Django 4.1.4 on 2023-02-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jsp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
