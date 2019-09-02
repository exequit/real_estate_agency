# Generated by Django 2.2.4 on 2019-09-01 12:46

from django.db import migrations
import phonenumbers


def fill_owner_phone_pure(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if not phonenumbers.is_valid_number(phone):
            continue
        flat.owner_phone_pure = phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(fill_owner_phone_pure),
    ]
