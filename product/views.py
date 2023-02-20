from django.shortcuts import render
from product.models import CakePr
# Create your views here.
def pro(request):
    return render(request,'test.html')

def prodetails(request):
    ids=request.GET['id']
    data=CakePr.objects.get(id=ids)
    #return render(request,'single_post.html',{"prodetails":data})
    return render(request,'single-product.html',{"prodetails":data})

def commentarea(request):
    cmd=request.GET['cmt']
    user=request.GET['user']
    pro=request.GET['pro']
    print('hi',cmd,user,pro)
    return render (request,'test.html')

    