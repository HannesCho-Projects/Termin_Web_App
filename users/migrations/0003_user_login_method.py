# Generated by Django 4.1.1 on 2022-09-23 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('github', 'Github'), ('kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]
