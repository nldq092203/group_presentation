# Generated by Django 5.0.4 on 2024-05-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_member_is_requested'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]