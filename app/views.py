from django.contrib import messages
from django.shortcuts import redirect, render
from.models import Games, News, Tranding , Orders
from django.contrib.auth.models import User,auth
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.views.decorators.csrf import csrf_exempt
from .PayTm import Checksum
MERCHANT_KEY = 'uUXHfPG3u7Y5tV43'


# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    games=Games.objects.all()
    return render(request,'home.html', {'games': games})
def store(request):
    return render(request,'store.html')
def discover(request):
    games=Games.objects.all()
    return render(request,'discover.html', {'games': games })
def gameproduct(request,myid ):
    if request.method == "POST":
        name = request.POST.get('name', '')
        download = request.POST.get('download', '')
        email = request.POST.get('email', '')
        phone = request.POST.get("phone", '')
        message = request.POST.get('message', '')
        games = request.POST.get('games', '')
        price = request.POST.get('price', '')
        order = Orders(name=name, email=email, message=message, phone=phone ,games=games ,price=price,download=download)
        order.save()
        id = order.id;
        subject = "congralation for buying the game"  
        html_message = render_to_string('bill.html',{'name': name, 'id':id, 'phone': phone,'email': email,'games': games,'price': price,'download': download})
        plain_message = strip_tags(html_message)
        to      =  email
        mail.send_mail(subject, plain_message, settings.EMAIL_HOST_USER,[to], html_message=html_message)
        param_dict = {
            'MID': 'pZYwlH74777163240584',
            'ORDER_ID': str(id),
            'TXN_AMOUNT': str(price),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
       
        return render(request, 'paytm.html', {'param_dict':param_dict})

    games = Games.objects.filter(id=myid)
    return render(request,'gameproduct.html', {'games': games[0]})
def tg1(request):
    tranding = Tranding.objects.all()
    return render(request,'tg1.html', {'tranding': tranding})
def tg2(request):
    tranding = Tranding.objects.all()
    return render(request,'tg2.html', {'tranding': tranding})
def tg3(request):
    tranding = Tranding.objects.all()
    return render(request,'tg3.html', {'tranding': tranding})
def tg4(request):
    tranding = Tranding.objects.all()
    return render(request,'tg4.html', {'tranding': tranding})
def tg5(request):
    tranding = Tranding.objects.all()
    return render(request,'tg5.html', {'tranding': tranding})
def news(request):
    news = News.objects.all()
    return render(request,'news.html', {'news': news})
def action(request):
    games = Games.objects.all()
    return render(request,'action.html', {'games': games})
def adventure(request):
    games = Games.objects.all()
    return render(request,'adventure.html', {'games': games})
def roleplay(request):
    games = Games.objects.all()
    return render(request,'roleplay.html', {'games': games})
def Sports(request):
    games = Games.objects.all()
    return render(request,'Sports.html', {'games': games})
def Simulation(request):
    games = Games.objects.all()
    return render(request,'Simulation.html', {'games': games})
def Strategy(request):
    games = Games.objects.all()
    return render(request,'Strategy.html', {'games': games})   
def search(request):
    if request.method == "POST":
        search = request.POST['search']
        games = Games.objects.filter(name__contains=search)
        return render(request, 'search.html', {'search':search,'product':games})
    else:
        return render(request, 'search.html')   
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid crentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
       username = request.POST['username']
       password1 = request.POST['password1']
       password2 = request.POST['password2']
       email = request.POST['email']

       if password1 == password2:
           if User.objects.filter(username=username).exists():
               messages.info(request,'name Taken')
               return redirect('login')
           elif User.objects.filter(email=email).exists():
               messages.info(request,'Email Taken')
               return redirect('login')
           else:
               user = User.objects.create_user(username=username, password=password1, email=email)
               user.save();
               subject = "Greetings"  
               msg     = "hii nice of you to join "  
               to      = user.email
               res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
               
               print('user created')
               return redirect('login')
       else:
           messages.info(request, 'password not matching')
           return redirect('home')

       return redirect('/')

    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def account(request):
    user = request.user
    return render(request, 'account.html',{'user' : user})
def bill(request):
    return render(request, 'bill.html')
def status(request):
    tranding = Tranding.objects.all()
    return render(request,'status.html',{'tranding': tranding})    
@csrf_exempt
def handlerequest(request):
    #paytm send request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order Successfull')
        else:
            print('order was not success full' + response_dict['RESPMSG'])
    return render(request,'paymentstatus.html',{'response': response_dict})

