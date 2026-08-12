import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from portfolio.models import JourneyChapter

CHAPTERS = [
  {
    "id": "foundation",
    "year": "2024",
    "title": "The Foundation",
    "place": "University",
    "story": "Started formal education in Computer Science. Discovered a deep passion for coding and building things from scratch, learning the fundamentals of programming, algorithms, and software engineering.",
    "bridge": "The classroom taught me the concepts, but building real projects taught me the craft.",
    "fr": {
      "title": "Les Fondations",
      "place": "Université",
      "story": "Début de ma formation en informatique. Découverte d'une passion pour le code et la création à partir de zéro, apprentissage des bases de la programmation, des algorithmes et du génie logiciel.",
      "bridge": "La salle de classe m'a appris les concepts, mais ce sont les projets réels qui m'ont appris le métier.",
    },
  },
  {
    "id": "toolkit",
    "year": "2025",
    "title": "Building the Toolkit",
    "place": "Internships & Projects",
    "story": "Spent the year diving deep into web development. Built multiple full-stack applications, mastered modern frameworks like React and Node.js, and completed a software engineering internship.",
    "bridge": "Writing code was one thing; designing scalable systems for actual users was another.",
    "fr": {
      "title": "Construire la boîte à outils",
      "place": "Stages & Projets",
      "story": "Une année passée à plonger dans le développement web. Création de multiples applications full-stack, maîtrise de frameworks modernes comme React et Node.js, et réalisation d'un stage en ingénierie logicielle.",
      "bridge": "Écrire du code est une chose ; concevoir des systèmes évolutifs pour de vrais utilisateurs en est une autre.",
    },
  },
  {
    "id": "developer",
    "year": "2026",
    "title": "Professional Developer",
    "place": "Current Role",
    "story": "Transitioned into a full-time software developer role. Currently focused on building robust, scalable web applications, optimizing performance, and consistently delivering clean, maintainable code.",
    "bridge": "The journey from student to professional developer is complete, but the learning never stops.",
    "fr": {
      "title": "Développeur Professionnel",
      "place": "Poste Actuel",
      "story": "Transition vers un rôle de développeur logiciel à temps plein. Actuellement concentré sur la création d'applications web robustes et évolutives, l'optimisation des performances et la livraison d'un code propre et maintenable.",
      "bridge": "Le voyage d'étudiant à développeur professionnel est terminé, mais l'apprentissage ne s'arrête jamais.",
    },
  },
]

def seed():
    print("Seeding Journey Chapters...")
    JourneyChapter.objects.all().delete()
    
    for i, c in enumerate(CHAPTERS):
        JourneyChapter.objects.create(
            year=c["year"],
            title=c["title"],
            place=c["place"],
            story=c["story"],
            bridge=c["bridge"],
            fr_title=c["fr"]["title"],
            fr_place=c["fr"]["place"],
            fr_story=c["fr"]["story"],
            fr_bridge=c["fr"]["bridge"],
            order=i
        )
    print("Done seeding Journey data!")

if __name__ == "__main__":
    seed()
