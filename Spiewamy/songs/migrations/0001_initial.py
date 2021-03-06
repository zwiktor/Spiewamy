# Generated by Django 2.2 on 2020-09-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(default='This is plain text')),
                ('style', models.CharField(choices=[('P', 'Popularna'), ('R', 'Rock'), ('S', 'Szanty'), ('C', 'Klasyczna'), ('F', 'Biesiada')], max_length=1, null=True)),
                ('play_on', models.CharField(choices=[('G', 'Gitara'), ('A', 'Akordeon'), ('P', 'Pianino')], max_length=1, null=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
