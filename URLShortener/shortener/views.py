from django.shortcuts import render, redirect
from django.http import Http404
from .models import Urls
import string, random

def generate_gurl(length=15):
    characters = string.ascii_letters + string.digits
    gurl = ''.join(random.choice(characters) for _ in range(length))
    return gurl

def homepage(request):
    gurl = None
    if request.method == 'POST':
        ourl = request.POST.get('url')
        gurl = generate_gurl()
        while Urls.objects.filter(gurl=gurl).exists():
            gurl = generate_gurl()
        ins = Urls.objects.create(ourl=ourl, gurl=gurl)
        ins.save()
        return render(request, 'index.html', {'gurl': gurl})
    return render(request,'index.html')

def redirect_url(request, gurl):
    urls = Urls.objects.filter(gurl=gurl)
    if not urls.exists():
        raise Http404("URL not found")
    url = urls.first()
    return redirect(url.ourl)
