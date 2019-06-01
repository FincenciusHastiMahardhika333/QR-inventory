from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pyqrcode
from PIL import Image
import numpy as numpy
import pyzbar.pyzbar as pyzbar
from QRinventory import settings

def homepage(request):
    return render(request, 'webs/index.html')

@login_required
def profile(request):
    user = request.user
    qr = pyqrcode.create(user.username)
    filename = user.username + '.png'
    qr.png('media/temp/' + filename, scale=7)
    im = Image.open(settings.MEDIA_ROOT + "/temp/" + filename)
    text = pyzbar.decode(im)
    text = text[0].data.decode("utf-8")
    return render(request, 'webs/profile.html', {'user': user, 'text': text})
