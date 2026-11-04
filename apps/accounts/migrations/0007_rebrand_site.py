from django.conf import settings
from django.db import migrations


def rebrand_site(apps, schema_editor):
    """Point the django.contrib.sites row at this deployment.

    ``Site`` is what allauth and the notification templates call the product, so
    leaving it as the upstream name leaks it into mail headers and any template
    that uses ``{{ site.name }}``. Reads ``settings.BRAND`` rather than hardcoding
    the new name, so a differently-branded deployment migrates correctly too.
    """
    brand = getattr(settings, "BRAND", {}) or {}
    Site = apps.get_model("sites", "Site")
    Site.objects.update_or_create(
        id=1,
        defaults={
            "domain": brand.get("domain", "social.merqato.digital"),
            "name": brand.get("product_name", "MerQato Social"),
        },
    )


def restore_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.filter(id=1).update(domain="studio.brightbean.xyz", name="Brightbean")


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_remove_user_review_banner_dismissed_at"),
        ("sites", "0002_alter_domain_unique"),
    ]
    operations = [migrations.RunPython(rebrand_site, restore_site)]
