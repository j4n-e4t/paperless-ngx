from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1068_alter_document_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="storage_class",
            field=models.CharField(
                verbose_name="storage class",
                max_length=12,
                choices=[
                    ("default", "Default"),
                    ("deep_archive", "Deep archive"),
                ],
                default="default",
                db_index=True,
            ),
        ),
    ]
