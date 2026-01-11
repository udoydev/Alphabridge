from django.shortcuts import render
from django.http import HttpResponse, Http404

# Service details data
SERVICE_DETAILS = {
    "business-strategy": {
        "title": "Business Strategy & Digital Transformation",
        "items": [
            "Business Strategy & Roadmapping",
            "Growth Plans & Market Expansion",
            "Cost-Cutting & Efficiency Programs",
            "Market Research & Competitive Intelligence",
            "ESG Strategy & Carbon Accounting",
            "Scenario Planning & Risk Modeling",
            "Political & Government Advisory",
            "M&A Due Diligence & Integration",
            "Digital Transformation (Executive Roadmap)",
            "HR Policy & Team Development",
            "Talent Acquisition & Employer Branding",
            "Remote-First Operations Design",
        ],
    },
    "ai-data": {
        "title": "AI & Data-Driven Business Growth",
        "items": [
            "AI Readiness Assessment & ROI Calculator",
            "AI Use-Case Discovery & Prioritization",
            "AI Ethics & Governance Framework",
            "Data-Stack Audit & Modernization",
            "Predictive Analytics (Sales, Demand, Churn)",
            "Generative-AI Copilots (Ops, CX, Content)",
            "Custom AI Model Fine-Tuning",
            "Synthetic Data Generation",
            "KPI Dashboards & OKR Tracking",
            "Performance Marketing Automation (SEO, SEM, Social)",
            "Price Optimization & Dynamic Pricing",
        ],
    },
    "business-analysis": {
        "title": "Business Analysis & Startup Development",
        "items": [
            "Idea Validation & Problem-Solution Fit",
            "Business Model Design (Canvas, Lean, BMG)",
            "No-Code MVP Development",
            "Product-Market Fit Testing",
            "Brand Building (Identity, Positioning, Messaging)",
            "Financial Modeling & Unit Economics",
            "Cap Table & Equity Structuring",
            "Legal Compliance (Entity, IP, SAFE, Contracts)",
            "Team Structuring & Hiring Roadmap",
            "Sales Process Design & Playbook",
            "Customer Success Framework",
            "Pitch Deck Creation & Storytelling",
            "Fundraising Strategy & Investor Relations",
            "Data Room Preparation",
            "Business Process Mapping (BPM)",
        ],
    },
    "it-cyber": {
        "title": "IT & Cyber Resilience",
        "items": [
            "IT Infrastructure Setup (Cloud Landing Zone)",
            "Custom Software Development (Web, Mobile, APIs)",
            "Penetration Testing & Security Audits",
            "Cybersecurity Posture Review & Zero-Trust Design",
            "GDPR/Privacy Compliance Automation",
            "Cloud Services (Migration, FinOps, Serverless)",
            "DevSecOps & Secure SDLC",
            "ISO 27001 / SOC 2 / PCI-DSS / HIPAA Fast-Track",
            "Incident-Response Retainer & Playbook",
            "Virtual CISO (vCISO) Services",
            "Backup & Disaster Recovery (BDRaaS)",
            "Third-Party Risk Management",
        ],
    },
    "marketing-growth": {
        "title": "Marketing & Growth Engineering",
        "items": [
            "Brand Strategy & Storytelling",
            "Content Creation (Video, Blog, Interactive, Podcast)",
            "SEO/SEM & Performance Copywriting",
            "Hyper-Personalization & AI Content",
            "Social-Media Growth (Organic + Paid)",
            "LinkedIn Thought Leadership",
            "Short-Form Video Strategy (TikTok, Reels)",
            "Marketing Automation & CRM Integration",
            "CRO & Funnel Analytics (A/B, Heatmaps)",
            "Landing Page Psychology Audits",
            "Account-Based Marketing (ABM)",
            "Influencer/KOL Campaigns",
            "Growth-Hacking Experiments (ICE Scoring)",
            "Community-Led Growth (Discord, WhatsApp, FB)",
            "Multi-Touch Attribution Modeling",
            "Privacy-First Analytics",
        ],
    },
}


def home(request):
    return render(request, "dashboard.html")


def service(request):
    return render(request, "service.html")


def service_detail(request, service_type):
    service_data = SERVICE_DETAILS.get(service_type)
    if not service_data:
        raise Http404("Service not found")

    context = {
        "service_title": service_data["title"],
        "service_items": service_data["items"],
    }
    return render(request, "service_detail.html", context)


def contact(request):
    return render(request, "contact.html")
