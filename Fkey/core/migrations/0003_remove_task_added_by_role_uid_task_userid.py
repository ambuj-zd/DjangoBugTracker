# Generated by Django 4.1.7 on 2023-02-21 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_role_task_user_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='added_by',
        ),
        migrations.AddField(
            model_name='role',
            name='uid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.user'),
        ),
        migrations.AddField(
            model_name='task',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.user'),
        ),
    ]
