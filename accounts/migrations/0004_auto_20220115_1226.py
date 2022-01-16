# Generated by Django 3.1 on 2022-01-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_proposal_val'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='val',
        ),
        migrations.AddField(
            model_name='job',
            name='jobCode',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='proposal',
            name='jobCode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
