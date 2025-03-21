# Generated by Django 5.1.6 on 2025-03-08 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_repo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password_hash',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=' ', max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=35),
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('user_activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('last_login', models.DateTimeField(blank=True, default=None, null=True)),
                ('ip_address', models.CharField(max_length=50)),
                ('state', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='Web_repo.user')),
            ],
        ),
    ]
