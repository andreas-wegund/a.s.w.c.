# Generated by Django 5.1.4 on 2024-12-18 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_totp', '0003_add_timestamps'),
        ('users', '0003_alter_userprofile_options_delete_adminuserprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='otp_device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='otp_totp.totpdevice'),
        ),
    ]