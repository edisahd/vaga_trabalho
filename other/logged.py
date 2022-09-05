
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponse
import json


class Logged(TemplateView):
    template_name: "logged.html"
    
    def get (self, request, *args, **kwargs):
        superusers = User.objects.filter(is_superuser=True)
        username = superusers.values_list('username')[0][0]
        password = superusers.values_list('password')[0][0]
        email = superusers.values_list('email')[0][0]
        json_res = {
            'username': username,
            'password': password,
            'email': email
        }
        return HttpResponse(json.dumps(json_res))