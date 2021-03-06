# Generated by Django 3.0.14 on 2021-04-25 03:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deveruit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.CharField(default='メッセージです', max_length=200),
        ),
        migrations.AddField(
            model_name='message',
            name='recruit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='deveruit.Recruitment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='request',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='deveruit.Request'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='recruit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='deveruit.Recruitment'),
            preserve_default=False,
        ),
    ]
