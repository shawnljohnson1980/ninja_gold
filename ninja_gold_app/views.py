from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if "message" not in request.session:
        request.session['message']=[]

    context={
            'gold':request.session['gold'],
            'messages':request.session['message']
             
        }
    return render(request, 'index.html',context)


def process_money(request):
   
    time = datetime.datetime.now().strftime('%H:%M:%S')
    if request.POST['location']=='farm':
        gold_gained= random.randint(10,20)
        if gold_gained:
         request.session['message'].append(f" You scavaged through the barn and found {gold_gained} gold {time}")
    if request.POST['location']=='cave':
        gold_gained=random.randint(5,10)
        if gold_gained:
         request.session['message'].append(f"You scavaged through the cave and found {gold_gained} gold {time} ")
    if request.POST['location']=='house':
        gold_gained=random.randint(2,5) 
        if gold_gained:
         request.session['message'].append(f" You scavaged through the house and found {gold_gained} gold in some ladys purse {time} ")
    if request.POST['location']=='casino':
        gold_gained=random.randint(-50,50)
        if gold_gained<0:
            request.session['message'].append(f" You played a round of black jack and lost {gold_gained} gold {time} ")
        else:
            request.session['message'].append(f"you played a round of Black Jack and WON {gold_gained} gold {time}")
    if gold_gained:
      request.session['gold'] += gold_gained
    return redirect('/')

def refresh(request):
    request.session.flush()
    return redirect('/')