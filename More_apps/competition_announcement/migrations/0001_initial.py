# Generated by Django 5.1.1 on 2024-10-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Competition",
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
                ("name", models.CharField(default="无标题", max_length=255)),
                ("link", models.URLField(blank=True, max_length=500)),
                ("type", models.CharField(blank=True, max_length=100)),
                ("reg_time_start", models.DateTimeField(blank=True, null=True)),
                ("reg_time_end", models.DateTimeField(blank=True, null=True)),
                ("comp_time_start", models.DateTimeField(blank=True, null=True)),
                ("comp_time_end", models.DateTimeField(blank=True, null=True)),
                ("readmore", models.URLField(blank=True, max_length=500)),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "报名未开始"),
                            (1, "报名进行中"),
                            (2, "报名已结束"),
                            (3, "比赛进行中"),
                            (4, "比赛已结束"),
                        ],
                        default=0,
                    ),
                ),
            ],
        ),
    ]