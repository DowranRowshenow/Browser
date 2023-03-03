from django.views.generic import View, TemplateView, FormView
from django.shortcuts import redirect, HttpResponseRedirect, render, HttpResponse
from django.urls import reverse, reverse_lazy
import requests


class HomePageView(TemplateView):
    template_name = 'home.html'


class ReturnPageView(View):

    def post(self, request):
        search = self.request.POST['search']
        r = requests
        rndr = str()
        try: 
            r = requests.get(url = "https://www." + search + "/", headers={})
            rndr = r.text
        except: 
            print(search, "is not exists!")
            rndr = search + " is not exists!"
        #return render(request, 'return.html', {'search': search, 'render': rndr})
        return HttpResponse(rndr)