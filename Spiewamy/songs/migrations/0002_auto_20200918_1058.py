# Generated by Django 2.2 on 2020-09-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='play_on',
            field=models.CharField(choices=[('G', 'Gitara'), ('A', 'Akordeon'), ('P', 'Pianino')], default='G', max_length=1),
        ),
        migrations.AlterField(
            model_name='song',
            name='style',
            field=models.CharField(choices=[('P', 'Popularna'), ('R', 'Rock'), ('S', 'Szanty'), ('C', 'Klasyczna'), ('F', 'Biesiada')], default='P', max_length=1),
        ),
    ]