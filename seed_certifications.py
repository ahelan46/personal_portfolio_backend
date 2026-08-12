import os
import django
import json

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from portfolio.models import Certification

CERTS = [
  {
    "no": "2.1",
    "issuer": "Microsoft",
    "logo": { "src": "/images/issuers/microsoft.png", "aspect": 2110 / 540 },
    "title": "Power Platform — Power BI & Power Virtual Agents",
    "year": None,
    "credentialId": None,
    "verified": False,
    "skills": [
      "Dashboard development & KPI design",
      "Data storytelling for non-technical users",
      "Conversational agent flows",
    ],
    "metric": { "value": "Power BI", "label": "Applied curriculum" },
    "fr": {
      "skills": [
        "Développement de tableaux de bord & design de KPI",
        "Data storytelling pour des publics non techniques",
        "Parcours d’agents conversationnels",
      ],
      "metricLabel": "Cursus appliqué",
    },
  },
  {
    "no": "2.2",
    "issuer": "Google",
    "logo": { "src": "/images/issuers/google.png", "aspect": 10000 / 3382 },
    "title": "Attract & Engage Customers with Digital Marketing",
    "year": None,
    "credentialId": None,
    "verified": False,
    "skills": [
      "Customer acquisition funnels",
      "Positioning & messaging",
      "Campaign measurement",
    ],
    "metric": { "value": "B2B / B2C", "label": "Funnel scope" },
    "fr": {
      "title": "Attirer & engager les clients par le marketing digital",
      "skills": [
        "Tunnels d’acquisition client",
        "Positionnement & discours de marque",
        "Mesure de campagnes",
      ],
      "metricLabel": "Périmètre du tunnel",
    },
  },
  {
    "no": "2.3",
    "issuer": None,
    "title": "SEO & Content Marketing",
    "year": None,
    "credentialId": None,
    "verified": False,
    "skills": [
      "Technical & on-page SEO",
      "Content architecture",
      "Search-intent research",
    ],
    "metric": { "value": "35%", "label": "Organic growth delivered" },
    "fr": {
      "title": "SEO & marketing de contenu",
      "skills": [
        "SEO technique & on-page",
        "Architecture de contenu",
        "Analyse de l’intention de recherche",
      ],
      "metricLabel": "Croissance organique obtenue",
    },
  },
  {
    "no": "2.4",
    "issuer": None,
    "title": "Business Analysis Fundamentals",
    "year": None,
    "credentialId": None,
    "verified": False,
    "skills": [
      "Requirements gathering",
      "Gap & root-cause analysis",
      "Process mapping",
    ],
    "metric": { "value": "12%", "label": "Workflow efficiency gain" },
    "fr": {
      "title": "Fondamentaux de l’analyse métier",
      "skills": [
        "Recueil des besoins",
        "Analyse d’écarts & de causes racines",
        "Cartographie des processus",
      ],
      "metricLabel": "Gain d’efficacité des flux",
    },
  },
  {
    "no": "2.5",
    "issuer": "IBM",
    "logo": { "src": "/images/issuers/ibm.png", "aspect": 4464 / 1944 },
    "title": "Artificial Intelligence — Foundations & Applied Use Cases",
    "year": None,
    "credentialId": None,
    "verified": False,
    "skills": [
      "Applied generative AI",
      "Prompt engineering",
      "Human-in-the-loop validation",
    ],
    "metric": { "value": "HITL", "label": "Validation practice" },
    "fr": {
      "title": "Intelligence artificielle — fondamentaux & cas d’usage",
      "skills": [
        "IA générative appliquée",
        "Ingénierie de prompts",
        "Validation avec humain dans la boucle",
      ],
      "metricLabel": "Pratique de validation",
    },
  },
]

def run():
    print("Deleting all existing certifications...")
    Certification.objects.all().delete()
    
    print(f"Ingesting {len(CERTS)} certifications...")
    for idx, cert in enumerate(CERTS):
        c = Certification(
            no=cert.get("no", ""),
            issuer=cert.get("issuer"),
            title=cert.get("title", ""),
            year=cert.get("year"),
            credential_id=cert.get("credentialId"),
            credential_url=cert.get("credentialUrl"),
            verified=cert.get("verified", False),
            skills=cert.get("skills", []),
            order=idx,
        )
        
        metric = cert.get("metric")
        if metric:
            c.metric_value = metric.get("value")
            c.metric_label = metric.get("label")
            
        logo = cert.get("logo")
        if logo:
            c.logo_image = logo.get("src")
            c.logo_aspect = logo.get("aspect")
            
        fr = cert.get("fr")
        if fr:
            c.fr_title = fr.get("title")
            c.fr_skills = fr.get("skills", [])
            c.fr_metric_label = fr.get("metricLabel")
            
        c.save()
        print(f"Saved: {c.title}")
    
    print("Done!")

if __name__ == '__main__':
    run()
