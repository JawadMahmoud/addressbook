import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contacts_project.settings')

import django
django.setup()
from contactsapp.models import Organization, Contact

def populate():

    google_contacts = [
        {"name": "Charles J Jones", 
        "address" : "3559 Davis Court",
        "city" : "Harrisburg",
        "country" : "USA",
        "phone" : "618-969-4143",
        "email" : "brody1994@gmail.com",
        "role" : "CFO",},
        {"name": "Norma W Bellman", 
        "address" : "657 Byers Lane",
        "city" : "Yuba City",
        "country" : "USA",
        "phone" : "530-755-3284",
        "email" : "rosemary1985@yahoo.com",
        "role" : "CTO",},
        {"name": "Paul L Currie", 
        "address" : "305 Limer Street",
        "city" : "Hogansville",
        "country" : "USA",
        "phone" : "706-523-7027",
        "email" : "heloise1984@yahoo.com",
        "role" : "CEO",}
        ]

    amazon_contacts = [
        {"name": "Kristina E Thompson", 
        "address" : "3174 Dennison Street",
        "city" : "Modesto",
        "country" : "USA",
        "phone" : "209-524-6266",
        "email" : "owen_armstro@hotmail.com",
        "role" : "CFO",},
        {"name": "Eddie B Villarreal", 
        "address" : "1579 Park Boulevard",
        "city" : "Oskaloosa",
        "country" : "USA",
        "phone" : "641-676-3956",
        "email" : "florida1997@hotmail.com",
        "role" : "CTO",},
        {"name": "Margaret M Mikels", 
        "address" : "2965 Evergreen Lane",
        "city" : "Los Angeles",
        "country" : "USA",
        "phone" : "323-561-8108",
        "email" : "prince2001@hotmail.com",
        "role" : "CEO",}
    ]

    orgs = {
        "Google" : {
        "contacts" : google_contacts, 
        "email" : "google@random.com", 
        "address" : "100 Google Avenue",
        "city" : "Mountain View", 
        "country" : "USA", 
        }, 
        "Amazon" : {
        "contacts" : amazon_contacts, 
        "email" : "amazon@random.com", 
        "address" : "550 Amazon Road",
        "city" : "Seattle", 
        "country" : "USA", 
        }, 
    }

    for org, org_data in orgs.items():
        o = add_org(org, org_data["email"], org_data["address"], org_data["city"], org_data["country"])
        for p in org_data["contacts"]:
            add_contact(o, p["name"], p["address"], p["city"], p["country"], p["phone"], p["email"], p["role"])

    for o in Organization.objects.all():
        for p in Contact.objects.filter(company=o):
            print("- {0} - {1}".format(str(o), str(p)))

def add_contact(company, name, address, city, country, phone, email, role):
    c = Contact.objects.get_or_create(company=company, name=name, email=email)[0]
    c.address = address
    c.city = city
    c.country = country
    c.phone = phone
    c.role = role
    c.save()
    return c

def add_org(name, email, address, city, country):
    o = Organization.objects.get_or_create(name=name)[0]
    o.email = email
    o.address = address
    o.city = city
    o.country = country
    o.save()
    return o

if __name__ == '__main__':
    print("Starting Rango population script...")
populate()