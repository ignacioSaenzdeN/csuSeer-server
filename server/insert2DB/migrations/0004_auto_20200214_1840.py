# Generated by Django 2.2.10 on 2020-02-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insert2DB', '0003_markovmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='markovModel',
        ),
        migrations.AddField(
            model_name='data',
            name='markovModel',
            field=models.IntegerField(null=True),
        ),
    ]