# Generated by Django 2.2.4 on 2021-03-05 11:25

from django.db import migrations

def write_new_building_or_not(apps, schema_editor):
    flat = apps.get_model('property', 'Flat')
    for flat in flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(write_new_building_or_not),
    ]


