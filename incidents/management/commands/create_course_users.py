"""
Management command : crée les comptes utilisateurs pour la présentation du cours.
Idempotent — ne modifie rien si les comptes existent déjà.
"""
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Crée les comptes utilisateurs requis pour la présentation du cours."

    def handle(self, *args, **options):
        User = get_user_model()

        # --- Compte utilisateur simple ---
        if not User.objects.filter(username="Nazairefabsimple").exists():
            User.objects.create_user(
                username="Nazairefabsimple",
                password="N@zaire2026",
            )
            self.stdout.write(self.style.SUCCESS("✔ Compte créé : Nazairefabsimple"))
        else:
            self.stdout.write("→ Compte déjà existant : Nazairefabsimple")

        # --- Compte administrateur ---
        if not User.objects.filter(username="Nazairefabadmin").exists():
            User.objects.create_superuser(
                username="Nazairefabadmin",
                password="N@zaire2026",
            )
            self.stdout.write(self.style.SUCCESS("✔ Compte admin créé : Nazairefabadmin"))
        else:
            self.stdout.write("→ Compte déjà existant : Nazairefabadmin")
