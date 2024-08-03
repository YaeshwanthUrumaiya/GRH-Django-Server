# Generated by Django 4.2.14 on 2024-07-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameUserData',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=100)),
                ('GameName', models.CharField(max_length=100)),
                ('DateTime', models.DateField()),
                ('Values', models.JSONField(default={})),
            ],
        ),
    ]
