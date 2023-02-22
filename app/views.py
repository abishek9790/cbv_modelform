from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.views.generic import FormView

# Create your views here.
class cbv_modelform(FormView):
    template_name='cbv_modelform.html'
    form_class=jspform

    def form_valid(self, form):
        form.save()
        return HttpResponse("inserted data successfully")
