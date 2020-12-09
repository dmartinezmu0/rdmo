# Generated by Django 2.2.16 on 2020-12-09 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0043_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='option',
            field=models.ForeignKey(blank=True, help_text='The option stored for this value.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='values', to='options.Option', verbose_name='Option'),
        ),
    ]
