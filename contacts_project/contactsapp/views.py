from django.shortcuts import render
from django.http import HttpResponse
from contactsapp.models import Organization, Contact


def index(request):
    context_dict = {}
    
    organizations = Organization.objects.order_by('name')

    context_dict['orgs'] = organizations

    return render(request, 'contactsapp/index.html', context=context_dict)


def about(request):
    return HttpResponse("Contacts App for Assignment <br/> <a href='/contacts/'>Index</a>")


def show_org(request, org_slug):
    context_dict = {}

    try:
        organization = Organization.objects.get(slug=org_slug)

        contacts = Contact.objects.filter(company=organization)

        context_dict['org'] = organization
        context_dict['con'] = contacts

    except Organization.DoesNotExist:
        context_dict['org'] = None
        context_dict['con'] = None

    return render(request, "contactsapp/org.html", context=context_dict)

def show_con(request, org_slug, c_id):
    context_dict = {}

    try:
        organization = Organization.objects.get(slug=org_slug)

        contact = Contact.objects.get(id=c_id, company=organization)

        context_dict['org'] = organization
        context_dict['con'] = contact

    except Contact.DoesNotExist:
        context_dict['org'] = None
        context_dict['con'] = None

    return render(request, "contactsapp/address.html", context=context_dict)