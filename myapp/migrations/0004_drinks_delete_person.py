# Generated by Django 4.2.1 on 2023-06-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_name_person_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
