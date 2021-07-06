# Generated by Django 3.2.3 on 2021-07-06 18:54

from django.db import migrations

# Generated by Django 3.2.3 on 2021-06-05 21:53
from django.db import migrations


def add_categories(apps, schema_editor):
    categories = [
        "Arqueologia",
        "Arte e Arquitectura",
        "Astronomia",
        "Biologia",
        "Gestão",
        "Química",
        "Ciência da comunicação",
        "Ciência da computação",
        "Economia",
        "Geografia",
        "História",
        "Línguas",
        "Matemática",
        "Filosofia",
        "Teologia & Estudos Religiosos",
        "Outra",
    ]

    KC = apps.get_model("api", "KnowledgeCategory")
    for category in categories:
        KC.objects.create(description=category)


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [migrations.RunPython(add_categories)]
