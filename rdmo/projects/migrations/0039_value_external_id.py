# Generated by Django 2.2.13 on 2020-10-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0038_integration_integrationoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='external_id',
            field=models.CharField(blank=True, help_text='External id for this value.', max_length=256, verbose_name='External id'),
        ),
    ]
