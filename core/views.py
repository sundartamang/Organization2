from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,View, CreateView
from django.core.paginator import Paginator, EmptyPage
from .forms import ContactMessageForm, DonationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
import json
from django.http import JsonResponse
from .models import (
    AboutUs,
    Activity,
    BankInformation,
    Carasoul,
    Cause,
    Contact,
    ContactMessage,
    Donor,
    Donation,
    Gallery,
    GalleryTitle,
    Member,
    Program   
)

# Create your views here.
def HomeView(request):
    carosoulList = Carasoul.objects.all()
    # for cuase section
    causeList    = Cause.objects.all().order_by('-timestamp')
    paginator    = Paginator(causeList, 3) 
    page_number  = request.GET.get('page')
    page_obj     = paginator.get_page(page_number)
    # for Activity link
    activity = Activity.objects.all()
    #for program 
    programList  = Program.objects.all().order_by('-timestamp')
    paginator    = Paginator(programList, 4) 
    page_number  = request.GET.get('page')
    page_obj2    = paginator.get_page(page_number)
    # to fetch donors
    donorList    = Donor.objects.all().order_by('-timestamp')
    paginator    = Paginator(donorList, 3) 
    page_number  = request.GET.get('page')
    page_obj3    = paginator.get_page(page_number)

    context = {
        'carosoulList'  : carosoulList,
        'page_obj'      : page_obj,
        'activity'      : activity,
        'page_obj2'     : page_obj2,
        'page_obj3'     : page_obj3
        
    }
    return render(request,'index.html',context)


def AboutUsView(request):
    # To fetch aboutus data
    aboutus = AboutUs.objects.all()
    # To fetch donor data
    member  = Member.objects.all()
    context = {
        'aboutus' : aboutus,
        'member'  : member,
    }
    return render(request,'aboutus.html',context)


class GalleryView(ListView):
    model          = Gallery
    paginate_by    = 24
    template_name  = 'gallaries.html'
    

def ProgramView(request):
    programList    = Program.objects.all().order_by('-timestamp')
    paginator      = Paginator(programList, 12) 
    page_number    = request.GET.get('page')
    page_obj       = paginator.get_page(page_number)
    context        = {
        'page_obj' : page_obj,
    }
    return render(request,'programs.html',context)


def ProgramDetailView(request, pk):
    program        = get_object_or_404(Program, pk=pk)
    programList    = Program.objects.all().order_by('-timestamp')
    paginator      = Paginator(programList, 3) 
    page_number    = request.GET.get('page')
    page_obj       = paginator.get_page(page_number)
    context = {
        'object' : program,
        'page_obj' : page_obj,
    }
    return render(request,'programdetail.html',context)


def ContributeView(request):
    # To fetch contact data
    infoList = BankInformation.objects.all()
    context  = {
        'infoList' : infoList,
    }
    return render(request,'contribute.html',context)


def ContactUsView(request):
    # To fetch contact data
    contactList = Contact.objects.all()
    context     = {
        'contactList' : contactList,
    }
    return render(request,'contactus.html',context)


class postMessage(View):
    def post(self, *args,**kwargs):
        form = ContactMessageForm(self.request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get('fullname')
            email    = form.cleaned_data.get('email')
            subject  = form.cleaned_data.get('subject')
            message  = form.cleaned_data.get('message')
            try:
                contact_obj          = ContactMessage()
                contact_obj.fullname = fullname
                contact_obj.email    = email
                contact_obj.subject  = subject
                contact_obj.message  = message
                contact_obj.save()
                return JsonResponse({'status':'ok'})
            except ObjectDoesNotExist:
                return JsonResponse({'status':'error'})
        else:
            return JsonResponse({'status':'error'})


class postDonation(View):
    def post(self, *args,**kwargs):
        form = DonationForm(self.request.POST)
        if form.is_valid():
            first_name      = form.cleaned_data.get('first_name')
            last_name       = form.cleaned_data.get('last_name')
            contact         = form.cleaned_data.get('contact')
            email           = form.cleaned_data.get('email')
            amount          = form.cleaned_data.get('amount')
            transcition_id  = form.cleaned_data.get('transcition_id')
            message         = form.cleaned_data.get('message')
            try:
                donation_obj                 = Donation()
                donation_obj.first_name      = first_name
                donation_obj.last_name       = last_name
                donation_obj.contact         = contact
                donation_obj.email           = email
                donation_obj.amount          = amount
                donation_obj.transcition_id  = transcition_id
                donation_obj.message         = message
                donation_obj.save()
                return JsonResponse({'status':'ok'})
            except ObjectDoesNotExist:
                return JsonResponse({'status':'error'})
        else:
            return JsonResponse({'status':'error'})