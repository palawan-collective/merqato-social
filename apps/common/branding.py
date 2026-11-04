"""White-label brand values, in one place.

Everything a customer can read that names the product lives in
``settings.BRAND``, which is populated from ``BRAND_*`` environment variables.
Templates read it through ``brand_context`` (registered in ``TEMPLATES``), so
re-pointing a deployment at a different brand is a configuration change, not a
find-and-replace across a hundred templates.

Deliberately *not* here: package names, database names, docker tags, the
``X-Brightbean-Email-Class`` routing header, and the AGPL notice in ``LICENSE``.
Those are technical identifiers or legal text; renaming them buys nothing and
breaks things.
"""

from __future__ import annotations

from django.conf import settings

# Fallbacks so the module still answers if a settings file predates BRAND.
_DEFAULTS: dict = {
    "product_name": "MerQato Social",
    "short_name": "MerQato",
    "company_name": "Palawan Collective",
    "company_url": "https://merqato.digital",
    "domain": "social.merqato.digital",
    "support_email": "growpalawan@gmail.com",
    "tagline": "Social media scheduling & approvals",
    "logo": "img/merqato-social-logo.png",
    "logo_mark": "img/merqato-mark.png",
    "favicon_dir": "favicon",
    "legal_url": "/legal/",
    "terms_url": "/legal/#terms",
    "privacy_url": "/legal/#privacy",
    "upstream_name": "BrightBean Studio",
    "upstream_url": "https://github.com/brightbeanxyz/brightbean-studio",
    "license_name": "AGPL-3.0",
    "colors": {
        "brand_50": "#F3F5FF",
        "brand_100": "#E7EBFF",
        "brand_200": "#D0D8FF",
        "brand_300": "#AFBCFF",
        "brand_400": "#8C9BFA",
        "brand_500": "#6675EE",
        "brand_600": "#4F5CD8",
        "brand_700": "#3F49AE",
        "brand_800": "#363E8C",
        "brand_900": "#2E3473",
        "brand_green_100": "#E4FAF3",
        "brand_green_200": "#BFEFE0",
        "brand_green_500": "#4FC9A6",
        "brand_green_600": "#34A98A",
    },
}


def get_brand() -> dict:
    """The brand dictionary for this deployment."""
    brand = dict(_DEFAULTS)
    brand.update(getattr(settings, "BRAND", None) or {})
    if not brand.get("colors"):
        brand["colors"] = dict(_DEFAULTS["colors"])
    return brand


def brand_context(request=None) -> dict:
    """Context processor: exposes ``{{ brand.product_name }}`` and friends."""
    return {"brand": get_brand()}
