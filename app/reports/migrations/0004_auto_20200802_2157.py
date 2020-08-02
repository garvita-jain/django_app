# Generated by Django 3.0.8 on 2020-08-02 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_reportinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportinfo',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='param', to='reports.Report'),
        ),
    ]
