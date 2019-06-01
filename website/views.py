from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pyqrcode
from PIL import Image
import numpy as numpy
import pyzbar.pyzbar as pyzbar
from QRinventory import settings
from inventory.models import Item

def homepage(request):
    # text = 'QR Inventory'
    # qr = pyqrcode.create(text)
    # filename = text + '.png'
    # qr.png('media/images/' + filename, scale=7)

    return render(request, 'webs/index.html')

@login_required
def profile(request):
    user = request.user
    items = Item.objects.filter(owner=user)
    return render(request, 'webs/profile.html', {'user': user, 'items': items})

def about(request):
    return render(request, 'webs/about.html')

def contact(request):
    return render(request, 'webs/contact.html')