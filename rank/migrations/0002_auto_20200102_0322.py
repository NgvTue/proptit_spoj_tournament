# Generated by Django 3.0 on 2020-01-02 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lastrank',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='solved_list',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='target',
            field=models.IntegerField(default=1),
        ),
    ]
