# Generated by Django 5.1.6 on 2025-03-09 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_userprofile_direct_referrals_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('TOTAL_EARNINGS', 'Total earnings'), ('TOTAL_WITHDRAWALS', 'Total Withdrawals'), ('REFERRAL_EARNINGS', 'Referral earnings'), ('RETAIL_BONUS', 'Retail Bonus'), ('LEADERSHIP_BONUS', 'Leadership bonus'), ('MATCHING_BONUS', 'Matching bonus'), ('TOTAL_EXPENSES', 'Total expenses'), ('DEPOSIT', 'Deposit'), ('WITHDRAWAL', 'Withdrawal')], max_length=20),
        ),
    ]
