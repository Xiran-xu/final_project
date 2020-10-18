# Generated by Django 3.1.2 on 2020-10-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.CharField(help_text='latitude of squirrel', max_length=100)),
                ('Longitude', models.CharField(help_text='longitude of squirrel', max_length=100)),
                ('Unique_Squirrel_ID', models.CharField(help_text='unique squirrel id of squirrel', max_length=100)),
                ('Shift', models.CharField(help_text='shift of squirrel', max_length=100)),
                ('Date', models.DateField(help_text='date of squirrel')),
                ('Age', models.CharField(help_text='age of squirrel', max_length=100)),
            ],
        ),
    ]
