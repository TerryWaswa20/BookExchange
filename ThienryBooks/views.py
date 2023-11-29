from django.shortcuts import render, redirect
from ThienryBooks.forms import HiringForm, ExchangeForm, ParentForm
from ThienryBooks.models import Hiring, Exchange


def parent(request):
    if request.method == "POST":
        user_form = ParentForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('c_login')
    else:
        user_form = ParentForm
    return render(request, 'parent_form.html', {'user_form': user_form})


def dashboard(request):
    return render(request, "client_dashboard.html")


def exchange(request):
    submitted = False
    if request.method == "POST":
        form = ExchangeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "client_dashboard.html")
    else:
        form = ExchangeForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'exchangeform.html', {'form': form, 'submitted': submitted})

    form = ExchangeForm
    return render(request, 'exchangeform.html', {'form': form})


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


def login_client(request):
    return render(request, "client_login.html")


def exchange_list(request):
    for_exchange = Exchange.objects.all()
    return render(request, "exchange_list.html", {'for_exchange': for_exchange})

