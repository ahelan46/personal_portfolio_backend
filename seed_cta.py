import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from portfolio.models import About

def seed():
    about = About.objects.first()
    if about:
        about.cta_text = "Explore My Work"
        about.fr_cta_text = "Découvrir mes projets"
        about.save()
        print("Done seeding CTA text!")

if __name__ == "__main__":
    seed()
