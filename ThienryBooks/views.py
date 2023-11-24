from django.shortcuts import render, redirect
from ThienryBooks.forms import HiringForm, PurchaseForm,ParentForm
from django.http import HttpResponseRedirect
from ThienryBooks.models import Hiring
from django.contrib.auth.models import User,auth


def parent(request):
    submitted = False
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "client_login.html")
        else:
            form = ParentForm
            if 'submitted' in request.GET:
                submitted = True
            return render(request, 'parent_form.html', {'form': form, 'submitted': submitted})

    form = ParentForm
    return render(request, 'parent_form.html', {'form': form})


def login_client(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard_client')
    return render(request, "client_login.html")


def dashboard(request):
    return render(request, "client_dashboard.html")


def purchase(request):
    submitted = False
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/purchase?submitted=True')
    else:
        form = PurchaseForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'bookshop_form.html', {'form': form, 'submitted': submitted})

    form = PurchaseForm
    return render(request, 'bookshop_form.html', {'form': form})


def hire(request):
    submitted = False
    if request.method == "POST":
        form = HiringForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "client_dashboard.html")
    else:
        form = HiringForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'hiring.html', {'form': form, 'submitted': submitted})

    form = HiringForm
    return render(request, 'hiring.html', {'form': form})


def books_hire(request):
    show_books = Hiring.objects.all()
    return render(request, "books_list.html", {'show_books': show_books})


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "classes.html")


def contact(request):
    return render(request, "contact.html")

