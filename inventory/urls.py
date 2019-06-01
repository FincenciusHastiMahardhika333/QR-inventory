from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^item/create', views.Create_item_Form.as_view(), name="create_item")
]
