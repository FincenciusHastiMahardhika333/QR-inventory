from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import FormView
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from .models import Item
from QRinventory import settings
import pyqrcode
from PIL import Image

def get_qrcode(tag):
    qr = pyqrcode.create(tag)
    filename = tag + '.png'
    qr.png('media/temp/' + filename, scale=7)
    
    return filename

class ItemForm(forms.Form):
    name = forms.CharField()
    itemtype = forms.CharField()
    desc = forms.CharField()

class Create_item_Form(FormView):
    template_name = "item/create_item.html"
    form_class = ItemForm
    success_url = '/'

    def form_valid(self, form):
        try:
            newly_created_item = Item()
            newly_created_item.owner = User.objects.get(id=1)
            newly_created_item.name = form.cleaned_data['name']
            newly_created_item.type = form.cleaned_data['itemtype']
            newly_created_item.desc = form.cleaned_data['desc']
            tag = form.cleaned_data['name'] + form.cleaned_data['itemtype']
            filename = get_qrcode(tag)
            qrcode = Image.open(settings.MEDIA_ROOT + "/temp/" + filename)
            newly_created_item.qrcode = qrcode
            newly_created_item.tag = tag
            newly_created_item.save()
            return HttpResponseRedirect('accounts/profile')
        except IntegrityError as e:
            return redirect('accounts/profile')

