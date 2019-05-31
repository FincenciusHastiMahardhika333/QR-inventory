from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pyqrcode
from PIL import Image

def homepage(request):
    return render(request, 'webs/index.html')

@login_required
def profile(request):
    user = request.user
    qr = pyqrcode.create(user.username)
    qr.png('static/username.png', scale=7)
    return render(request, 'webs/profile.html', {'user': user})
