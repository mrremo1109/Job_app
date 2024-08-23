# Generated by Django 5.1 on 2024-08-20 23:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_message_delete_chat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_rooms', to='App.job_post')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_chat_rooms', to=settings.AUTH_USER_MODEL)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recruiter_chat_rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='chat_room',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='App.chatroom'),
            preserve_default=False,
        ),
    ]
