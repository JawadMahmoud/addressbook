from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from contactsapp.models import Organization, Contact
from contactsapp.forms import OrganizationForm, ContactForm
from django.template.defaultfilters import slugify


def index(request):
    context_dict = {}

    return render(request, 'contactsapp/index.html', context=context_dict)


def show_org_all(request):
    context_dict = {}
    
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    context_dict['alphas'] = alphabets

    nations = sorted(Organization.objects.values_list('country', flat=True).distinct())

    organizations = Organization.objects.order_by('name')

    if len(organizations) > 0:
        context_dict['orgs'] = organizations
    else:
        context_dict['orgs'] = None

    if len(nations) > 0:
        context_dict['nations'] = nations
    else:
        context_dict['nations'] = None

    return render(request, 'contactsapp/company.html', context=context_dict)


def about(request):
    return render(request, 'contactsapp/about.html', {})


def show_org(request, org_slug):
    context_dict = {}

    try:
        organization = Organization.objects.get(slug=org_slug)

        contacts = Contact.objects.filter(company=organization).order_by('name')

        context_dict['org'] = organization
        context_dict['con'] = contacts

    except Organization.DoesNotExist:
        context_dict['org'] = None
        context_dict['con'] = None

    return render(request, "contactsapp/org.html", context=context_dict)

def show_con(request, c_id):
    context_dict = {}

    try:
        contact = Contact.objects.get(id=c_id)

        organization = Organization.objects.get(slug=slugify(contact.company))

        context_dict['org'] = organization
        context_dict['con'] = contact

    except Contact.DoesNotExist:
        context_dict['org'] = None
        context_dict['con'] = None

    return render(request, "contactsapp/address.html", context=context_dict)


def add_org(request):
    form = OrganizationForm()

    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, "contactsapp/addorg.html", {'form' : form})

def add_con(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, "contactsapp/addcon.html", {'form' : form})

def edit_con(request, c_id):

    context_dict = {}
    
    try:
        current_contact = Contact.objects.get(id=c_id)
        context_dict['this_contact'] = current_contact
    except Contact.DoesNotExist:
        return redirect('index')

    form = ContactForm({
        'name': current_contact.name, 
        'address': current_contact.address, 
        'city': current_contact.city,
        'country': current_contact.country, 
        'phone': current_contact.phone, 
        'email': current_contact.email,
        'role': current_contact.role, 
        'picture': current_contact.picture, 
        'company': current_contact.company,
        })

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=current_contact)
        if form.is_valid():
            form.save(commit=True)
            return redirect('show_con', current_contact.id)
        else:
            print(form.errors)

    context_dict['form'] = form

    return render(request, "contactsapp/editcon.html", context_dict)

def edit_org(request, org_slug):

    context_dict = {}
    
    try:
        current_org = Organization.objects.get(slug=org_slug)
        context_dict['this_org'] = current_org
    except User.DoesNotExist:
        return redirect('index')

    form = OrganizationForm({
        'name': current_org.name, 
        'email': current_org.email, 
        'address': current_org.address,
        'city': current_org.city, 
        'country': current_org.country, 
        'logo': current_org.logo,
        })

    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES, instance=current_org)
        if form.is_valid():
            form.save(commit=True)
            return redirect('show_org', current_org.slug)
        else:
            print(form.errors)

    context_dict['form'] = form

    return render(request, "contactsapp/editorg.html", context_dict)

def del_org(request, org_slug):

    context_dict = {}

    try:
        Organization.objects.get(slug=org_slug).delete()
    except Organization.DoesNotExist:
        return redirect('index')

    return redirect('index')

def del_con(request, c_id):

    context_dict = {}

    this_slug = Contact.objects.get(id=c_id)
    this_slug = slugify(this_slug.company)

    try:
        Contact.objects.get(id=c_id).delete()
    except User.DoesNotExist:
        return redirect('index')

    return redirect('show_org', this_slug)

def show_con_all(request):

    context_dict = {}

    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    context_dict['alphas'] = alphabets

    roles = sorted(Contact.objects.values_list('role', flat=True).distinct())

    if len(roles) > 0:
        context_dict['roles'] = roles
    else:
        context_dict['roles'] = None

    try:
        contacts = Contact.objects.order_by('name')

        context_dict['cons'] = contacts

    except Contact.DoesNotExist:
        context_dict['cons'] = None

    return render(request, "contactsapp/addresses.html", context=context_dict)

def show_con_alpha(request, alphabet):

    context_dict = {}

    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    context_dict['alphas'] = alphabets

    context_dict['alpha'] = alphabet

    contacts = Contact.objects.filter(name__startswith=alphabet).order_by('name')

    roles = sorted(Contact.objects.values_list('role', flat=True).distinct())

    if len(roles) > 0:
        context_dict['roles'] = roles
    else:
        context_dict['roles'] = None

    if len(contacts) > 0:
        context_dict['cons'] = contacts
    else:
        context_dict['cons'] = None

    return render(request, "contactsapp/addresses.html", context=context_dict)

def show_con_roles(request, role):

    context_dict = {}

    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    context_dict['alphas'] = alphabets

    context_dict['role'] = role

    contacts = Contact.objects.filter(role=role).order_by('name')

    roles = sorted(Contact.objects.values_list('role', flat=True).distinct())

    if len(roles) > 0:
        context_dict['roles'] = roles
    else:
        context_dict['roles'] = None

    if len(contacts) > 0:
        context_dict['cons'] = contacts
    else:
        context_dict['cons'] = None

    return render(request, "contactsapp/addresses.html", context=context_dict)

def show_org_alpha(request, alphabet):
    context_dict = {}
    
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    context_dict['alphas'] = alphabets

    context_dict['alpha'] = alphabet

    organizations = Organization.objects.filter(name__startswith=alphabet).order_by('name')

    nations = sorted(Organization.objects.values_list('country', flat=True).distinct())

    if len(organizations) > 0:
        context_dict['orgs'] = organizations
    else:
        context_dict['orgs'] = None

    if len(nations) > 0:
        context_dict['nations'] = nations
    else:
        context_dict['nations'] = None

    return render(request, 'contactsapp/company.html', context=context_dict)

def show_org_nation(request, nation):
    context_dict = {}
    
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    context_dict['alphas'] = alphabets

    context_dict['nation'] = nation

    organizations = Organization.objects.filter(country=nation).order_by('name')

    nations = sorted(Organization.objects.values_list('country', flat=True).distinct())

    if len(organizations) > 0:
        context_dict['orgs'] = organizations
    else:
        context_dict['orgs'] = None

    if len(nations) > 0:
        context_dict['nations'] = nations
    else:
        context_dict['nations'] = None

    return render(request, 'contactsapp/company.html', context=context_dict)

def search(request):
    context_dict = {}
    ## Searches TV Show objects that contain a specific query
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        context_dict['query'] = query

        orgs = Organization.objects.filter(name__icontains=query)

        cons = Contact.objects.filter(name__icontains=query)

        if orgs.exists():
            context_dict['orgs'] = orgs
        else:
            context_dict['orgs'] = None

        if cons.exists():
            context_dict['cons'] = cons
        else:
            context_dict['cons'] = None
        return render(request, 'contactsapp/search.html', context_dict)
    else:
        return

def remove_logo(request, org_slug):

    context_dict = {}

    o = Organization.objects.get(slug=org_slug)
    o.logo = ""

    o.save()

    return redirect('show_org', org_slug)

def remove_pic(request, c_id):

    context_dict = {}

    c = Contact.objects.get(id=c_id)
    c.picture = ""

    c.save()

    return redirect('show_con', c_id)