# Generated by Django 5.0.2 on 2024-04-03 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_customer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="card_name",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="card_number",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="ccv",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="purchase_history",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="user",
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.CreateModel(
            name="Purchase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("purchase_date", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchases",
                        to="store.customer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
            ],
        ),
    ]
