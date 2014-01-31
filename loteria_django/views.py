from django.http import HttpResponse
from django.shortcuts import render
#from django.template import Context, Template
import os, random, sys

#Variables
img_dir = '/home/mmatus/Dropbox/MIT/SidPac/Mexican_coffee_hour/loteria/loteria_django_dir/loteria_django/static/img/'

cards = os.listdir(img_dir)

#Functions
def draw_random():
    random.shuffle(cards)
    try:
        call = cards.pop() #Random sample is given as a one-element list, so I take the first element to get the filename as string
    except IndexError:
        call = None
    #cards.remove(call) #Remove this file name (card) from the list (deck)
    return call

def show_card(request):
    call = draw_random()
    if call is None:
        return HttpResponse("No more cards!")
    return render(request, 'show_card.html', {'imgfile': call})