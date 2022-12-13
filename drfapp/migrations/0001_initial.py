# Generated by Django 4.1.4 on 2022-12-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('date_enrolled', models.DateField(auto_now=True)),
            ],
        ),
    ]
