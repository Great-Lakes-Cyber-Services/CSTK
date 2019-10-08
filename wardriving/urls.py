from django.contrib import admin
from django.urls import path

from . import views

app_name='wardriving'
urlpatterns = [
	path('', views.kismet_config, name='Kismet_Config'),
	path('wardriving/bluetoothconfig/btns', views.bluetooth_config_btns, name='bluetooth_config_btns'),
	path('wardriving/bluetoothconfig/btns', views.wifi_config_btns, name='wifi_config_btns'),
]
