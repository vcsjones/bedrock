# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.db import migrations, models

import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ("security", "0003_halloffamer"),
    ]

    operations = [
        migrations.CreateModel(
            name="MitreCVE",
            fields=[
                ("id", models.CharField(max_length=15, serialize=False, primary_key=True, db_index=True)),
                ("year", models.SmallIntegerField()),
                ("order", models.SmallIntegerField()),
                ("title", models.CharField(max_length=200, blank=True)),
                ("impact", models.CharField(max_length=100, blank=True)),
                ("reporter", models.CharField(max_length=100, blank=True)),
                ("description", models.TextField()),
                ("products", django_extensions.db.fields.json.JSONField(default="[]")),
                ("bugs", django_extensions.db.fields.json.JSONField(default="[]")),
            ],
            options={
                "ordering": ("-year", "-order"),
            },
        ),
    ]
