import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from portfolio.models import Experience

roles = [
  {
    "company": "Heeding Climate Solutions",
    "role": "Product Designer & UX Consultant",
    "type": "Internship",
    "location": "Sophia Antipolis, France",
    "period": "May – Oct 2026",
    "summary": "Owning the UX of a sustainable-fuel marketplace — research to hi-fi production mock-ups, every screen tied to a conversion KPI.",
    "achievements": [
      "Ran stakeholder interviews & segmentation workshops; shipped persona-specific Figma prototypes for fleet operators, suppliers and public-sector buyers",
      "Partnered with the Product Owner on roadmap, backlog and design-system governance",
      "Instrumented acquisition→activation→retention funnels (GA4); weekly insights fed the design backlog",
    ],
    "outcome": "Product targeting 1B+ tonnes of avoided CO₂ by 2050",
    "skills": ["Figma", "UX Research", "Design Systems", "GA4", "Agile"],
    "color": "#0072E3",
    "fg": "light",
    "logo_variant": "plate",
    "logo_aspect": 1199 / 330,
    "logo_placement": "right",
    "fr_role": "Product Designer & consultant UX",
    "fr_summary": "Responsable de l’UX d’une marketplace de carburants durables — de la recherche aux maquettes de production, chaque écran lié à un KPI de conversion.",
    "fr_outcome": "Produit visant 1 Md+ de tonnes de CO₂ évitées d’ici 2050",
    "fr_achievements": [
        "Entretiens avec les parties prenantes et ateliers de segmentation ; prototypes Figma dédiés aux transporteurs, fournisseurs et acheteurs publics",
        "Collaboration avec le Product Owner sur la roadmap, le backlog et la gouvernance du design system",
        "Instrumentation des tunnels acquisition→activation→rétention (GA4) ; insights hebdomadaires nourrissant le backlog design",
    ]
  },
  {
    "company": "UNBIAS Innovation Hackathon",
    "role": "Product & AI Innovation Lead",
    "type": "Hackathon",
    "location": "Sophia Antipolis, France",
    "period": "Mar 2026",
    "summary": "End-to-end product design of an AI venture in one sprint — value proposition, UX, monetisation logic and three live prototypes.",
    "achievements": [
      "Designed the interaction model for an offline, privacy-first AI assistant",
      "Built three functional prototype websites demonstrating concept, AI workflow and commercial framework",
      "Delivered a live jury walkthrough of architecture, user flow and unit economics",
    ],
    "outcome": "🏆 1st place — LockAI, offline secure on-device AI",
    "skills": ["Product Strategy", "Prototyping", "UX/UI", "AI", "HTML/CSS"],
    "color": "#6D3BF5",
    "fg": "light",
    "logo_variant": "plate",
    "logo_aspect": 685 / 226,
    "logo_placement": "below",
    "fr_role": "Responsable produit & innovation IA",
    "fr_summary": "Conception produit de bout en bout d’une start-up IA en un sprint — proposition de valeur, UX, modèle de revenus et trois prototypes en ligne.",
    "fr_outcome": "🏆 1re place — LockAI, IA sécurisée hors-ligne",
    "fr_achievements": [
        "Conception du modèle d’interaction d’un assistant IA hors-ligne, axé sur la confidentialité",
        "Trois sites prototypes fonctionnels démontrant le concept, le workflow IA et le cadre commercial",
        "Présentation live au jury : architecture, parcours utilisateur et économie unitaire",
    ]
  },
  {
    "company": "V Raise",
    "role": "Business & Process Analyst",
    "type": "Internship",
    "location": "Paris, France",
    "period": "Apr – Oct 2025",
    "summary": "Mapped and redesigned logistics workflows across operations, finance, IT and external 3PL partners.",
    "achievements": [
      "Business-process mapping, gap analysis and root-cause analysis to surface inefficiencies",
      "Designed steering-committee dashboards that made operational health legible at a glance",
    ],
    "outcome": "12% end-to-end logistics workflow efficiency gain",
    "skills": ["Process Mapping", "Dashboard Design", "KPI Design", "Stakeholders"],
    "color": "#FFFFFF",
    "fg": "dark",
    "logo_variant": "tile",
    "logo_aspect": 1,
    "fr_role": "Analyste métier & processus",
    "fr_summary": "Cartographie et refonte des flux logistiques entre les opérations, la finance, l’IT et les partenaires 3PL externes.",
    "fr_outcome": "+12 % d’efficacité sur le flux logistique de bout en bout",
    "fr_achievements": [
        "Cartographie des processus, analyse des écarts et des causes racines pour révéler les inefficacités",
        "Conception des tableaux de bord du comité de pilotage, rendant la santé opérationnelle lisible d’un coup d’œil",
    ]
  },
  {
    "company": "Oigetit.ai",
    "role": "Human-in-the-Loop AI Analyst",
    "type": "Internship",
    "location": "Los Gatos, USA · Remote",
    "period": "Jan – May 2025",
    "summary": "Improved an AI misinformation filter's accuracy and translated its verification engine into user-facing explanations — the UX of trust.",
    "achievements": [
      "Pattern recognition, data validation and edge-case identification across the AI pipeline",
      "Contributed to Responsible AI initiatives; wrote simplified user-focused explanations",
    ],
    "outcome": "Improved AI classification accuracy",
    "skills": ["Responsible AI", "Data Validation", "UX Writing"],
    "color": "#FF2E0F",
    "fg": "light",
    "logo_variant": "tile",
    "logo_aspect": 1,
    "fr_role": "Analyste IA « human-in-the-loop »",
    "fr_summary": "Amélioration de la précision d’un filtre anti-désinformation et traduction de son moteur de vérification en explications destinées aux utilisateurs — l’UX de la confiance.",
    "fr_outcome": "Précision de classification de l’IA améliorée",
    "fr_achievements": [
        "Reconnaissance de motifs, validation des données et identification des cas limites dans le pipeline IA",
        "Contribution aux initiatives d’IA responsable ; rédaction d’explications simplifiées",
    ]
  },
  {
    "company": "Site Web & Co",
    "role": "SEO & Digital Marketing",
    "type": "Internship",
    "location": "Montpellier, France",
    "period": "Jan – Apr 2025",
    "summary": "Audited and optimised web experiences across a B2B/B2C client portfolio — design decisions driven by measurement.",
    "achievements": [
      "On-page & technical SEO fixes; rewrote meta architecture and internal-linking logic for the highest-traffic templates",
      "Produced performance dashboards and growth insights for client stakeholders",
    ],
    "outcome": "35% organic traffic growth across the portfolio",
    "skills": ["Analytics", "CRO", "Web Performance", "SEO"],
    "color": "#FF6A00",
    "fg": "light",
    "fr_role": "SEO & marketing digital",
    "fr_summary": "Audit et optimisation d’expériences web sur un portefeuille de clients B2B/B2C — des décisions de design guidées par la mesure.",
    "fr_outcome": "+35 % de trafic organique sur le portefeuille",
    "fr_achievements": [
        "SEO technique et on-page ; refonte de l’architecture des métadonnées et du maillage interne des gabarits les plus consultés",
        "Tableaux de bord de performance et recommandations de croissance pour les clients",
    ]
  },
  {
    "company": "Sage Finance",
    "role": "Operations & Business Development Lead",
    "type": "Full-time",
    "location": "Telangana, India",
    "period": "Sep 2022 – Aug 2024",
    "summary": "Owned sales strategy and client acquisition for a financial-consulting practice — where my instincts about customers were forged.",
    "achievements": [
      "Built the inbound-to-close playbook adopted by the broader sales team",
      "Market analysis, customer segmentation and pipeline management against tracked KPIs",
    ],
    "outcome": "$20K+ sales in one week → promoted to Marketing Team Lead",
    "skills": ["Strategy", "Segmentation", "Pipeline", "Leadership"],
    "color": "#FFB200",
    "fg": "dark",
    "logo_variant": "tile",
    "logo_aspect": 1,
    "fr_role": "Responsable opérations & développement commercial",
    "fr_summary": "Pilotage de la stratégie commerciale et de l’acquisition client d’un cabinet de conseil financier — là où s’est forgé mon instinct client.",
    "fr_outcome": "20 000 $+ de ventes en une semaine → promu responsable marketing",
    "fr_achievements": [
        "Création du playbook inbound-to-close adopté par toute l’équipe commerciale",
        "Analyse de marché, segmentation client et gestion du pipeline face aux KPI suivis",
    ]
  },
  {
    "company": "Tutorac",
    "role": "Business Development Executive",
    "type": "Full-time",
    "location": "Telangana, India",
    "period": "Nov 2021 – Aug 2022",
    "summary": "Go-to-market and retention analysis for a subscription e-learning platform across the South-Indian market.",
    "achievements": [
      "Analysed subscription trends and customer feedback to support retention",
      "Expanded the client portfolio through outbound and partnership channels",
    ],
    "outcome": "$50K+ subscription sales in one month",
    "skills": ["Go-to-Market", "Growth", "Retention"],
    "color": "#171429",
    "fg": "light",
    "logo_variant": "tile",
    "logo_aspect": 1,
    "fr_role": "Chargé de développement commercial",
    "fr_summary": "Go-to-market et analyse de rétention pour une plateforme d’e-learning par abonnement sur le marché sud-indien.",
    "fr_outcome": "50 000 $+ de ventes d’abonnements en un mois",
    "fr_achievements": [
        "Analyse des tendances d’abonnement et des retours clients pour soutenir la rétention",
        "Élargissement du portefeuille clients via des canaux outbound et partenariats",
    ]
  }
]

Experience.objects.all().delete()
for i, data in enumerate(roles):
    Experience.objects.create(**data, order=i)

print("Successfully seeded Experience data!")
