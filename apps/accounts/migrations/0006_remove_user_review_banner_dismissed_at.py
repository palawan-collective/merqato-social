from django.db import migrations


class Migration(migrations.Migration):
    """Drops the sidebar review-banner state; the banner itself is gone."""

    dependencies = [
        ("accounts", "0005_add_review_banner_dismissed_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="review_banner_dismissed_at",
        ),
    ]
