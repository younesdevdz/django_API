# Generated by Django 4.2.1 on 2023-05-14 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app_one', '0013_remove_breakdown_report_alter_breakdown_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakdown',
            name='report',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='report', to='django_app_one.reporting'),
            preserve_default=False,
        ),
    ]
