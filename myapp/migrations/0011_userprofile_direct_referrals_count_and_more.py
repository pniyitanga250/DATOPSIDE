# Generated by Django 5.1.6 on 2025-03-07 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_userprofile_placement_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='direct_referrals_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='generations_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='left_leg_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='right_leg_count',
            field=models.IntegerField(default=0),
        ),
    ]
