# Generated by Django 3.0.8 on 2020-08-02 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20200802_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=100)),
                ('value', models.IntegerField(blank=True)),
                ('upper_limit', models.IntegerField(blank=True)),
                ('lower_limit', models.IntegerField(blank=True)),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reports.Report')),
            ],
            options={
                'unique_together': {('report', 'parameter')},
            },
        ),
    ]