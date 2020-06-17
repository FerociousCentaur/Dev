from django.shortcuts import render
from .models import member, rovers
#from .templates import show



def mem(request):
    memb = member.objects.all().order_by('superiority')
    rove = rovers.objects.all().order_by('year')
    return render(request, 'nav.html', {'member': memb, 'rover': rove})
