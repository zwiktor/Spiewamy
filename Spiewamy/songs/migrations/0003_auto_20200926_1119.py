# Generated by Django 2.2 on 2020-09-26 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0002_auto_20200918_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='song',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]