from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, request
from .models import *
from .forms import *
from django.contrib import messages
import string
import random
from django.db.models import Q
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string


def myindex(request):	
	po = Post.objects.filter()
	context = {'show':po}
	return render(request,'index/index.html',context)

def mycard(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		fname = request.POST.get('name')
		sex = request.POST.get('sex')
		address = request.POST.get('add')
		phone = request.POST.get('phone')
		country = request.POST.get('con')
		randompin = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
		cre = Card(email=email,name=fname,sex=sex,country=country,phone=phone,address=address,pin=randompin)
		cre.save()
		messages.success(request, 'Thank you for applying for fan card.Please contact us via live chat for further instrustions.')
	return render(request,'index/card.html')


def myabout(request,slug):
	title = 'About'
	a = get_object_or_404(Post, slug=slug)
	if request.method == 'POST':
		email = request.POST.get('email')
		name = request.POST.get('name')
		type_event = request.POST.get('event')
		date = request.POST.get('date')
		message = request.POST.get('message')
		price = request.POST.get('price')
		job = request.POST.get('job')
		home = request.POST.get('home')
		sex = request.POST.get('sex')
		air = request.POST.get('air')
		phone = request.POST.get('phone')
		location = request.POST.get('location')
		cre = Booking.objects.create(post=a,email=email,name=name,type_event=type_event,date=date,price=price,message=message,job=job,sex=sex,location=location,phone=phone,air=air,home=home)
		msg = EmailMessage(
		'Ticket request',
		cre.name + " Has requested for Ticket NO. " + cre.email + " , check your dashboard for more info",
		settings.DEFAULT_FROM_EMAIL,
		['bookmyfavceleb@gmail.com'],
		)
		msg.send()
		messages.success(request, 'Your Booking request has been submitted. A representative will go through your application and get in touch with you via live chat as soon as possible.<br><br>Thank you for making us your Booking Agency.Please contact us via live chat.')
	context = {'title':title,'data':a}
	return render(request,'index/book.html',context)


def myservices(request):
	po = Post.objects.filter()
	context = {'po':po}
	return render(request,'index/list.html',context)

def tic(request):
	qs = Ticket.objects.all()
	if request.method == 'POST':
		email = request.POST.get('email')
		ticket = request.POST.get('tic')
		tic_obj = Ticket.objects.get()
		randompin = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
		create = Ticbooking.objects.create(ticket=tic_obj,pin=randompin,email=email)
		msg = EmailMessage(
		'Pin request',
		create.email + " Has requested for pin NO. " + create.pin + " , contact admin via live chat  for more info",
		settings.DEFAULT_FROM_EMAIL,
		[email],
		)
		msg.send()
		messages.success(request, 'Check your email for ticket pin')
	context = {'qs':qs} 
	return render(request, "index/tic.html",context)
def mycontact(request):
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thanks for your message we will repyl you shortly')
			return redirect('indexurl:contact')
	else:
		form = Contactform()
	title = 'Contact-us'
	context = {'title':title}
	return render(request,'index/contact.html',context)

def mytrack(request):
	title = 'Track'
	if request.method == 'POST':
		pin = request.POST.get('pin')
		fillid = Ticbooking.objects.filter(pin=pin)
		if fillid.exists():
			qs = Ticbooking.objects.get(pin=pin)
			context = {'data':qs}
			return render(request,'index/far.html',context)
		else:
			messages.error(request, 'invalid ID')
	context = {'title':title}
	return render(request,'index/tic.html',context)

def myquote(request):
	if request.method == 'POST':
		pin = request.POST.get('pin')
		fillid = Card.objects.filter(pin=pin)
		if fillid.exists():
			qs = Card.objects.get(pin=pin)
			context = {'data':qs}
			return render(request,'index/IDCard.html',context)
		else:
			messages.error(request, 'invalid ID contact Admin')
	context = {}
	return render(request, 'index/card.html',context)


def dash(request):
	# qs=Quote.objects.get()
	# context = {'data':qs}
	return render(request, 'index/faq.html')

def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(name__contains=query)

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'index/pos.html', context)

        else:
            return render(request, 'index/pos.html')

    else:
        return render(request, 'index/pos.html')
