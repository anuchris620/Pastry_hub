from django.shortcuts import render,redirect
from product.models import CakePr,CommentBox
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
    comment=CommentBox.objects.create(User=user,Comment=cmd,pro_id=pro)  #insert comment in sql, User in models, user we created in commentarea, pro_if since FOREIGNKEY
    comment.save();
    return redirect ('/pro/?id='+pro)

    