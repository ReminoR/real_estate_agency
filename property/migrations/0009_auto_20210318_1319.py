# Generated by Django 2.2.4 on 2021-03-18 10:19

from django.db import migrations
import phonenumbers

def convert_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        try:
            parsed_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
            if phonenumbers.is_valid_number(parsed_phone):
                flat.owner_pure_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
                flat.save()
        except phonenumbers.phonenumberutil.NumberParseException:
            pass

        

def clean_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20210318_1315'),
    ]

    operations = [
        migrations.RunPython(convert_phonenumbers, clean_pure_phone),
    ]
