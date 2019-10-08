from django.shortcuts import render

# Create your views here.
def kismet_config(request, error=None, info=None, success=None, warning=None):
	context = {'title':'Wardriving Config', 'description': 'Wardriving Config for Kismet'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'wardriving/base.html', {'context': context})

def bluetooth_config_btns(request, error=None, info=None, success=None, warning=None):
	context = {'title':'Wardriving Config', 'description': 'Wardriving Config for Kismet'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'wardriving/base.html', {'context': context})

def wifi_config_btns(request, error=None, info=None, success=None, warning=None):
	context = {'title':'Wardriving Config', 'description': 'Wardriving Config for Kismet'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'wardriving/base.html', {'context': context})