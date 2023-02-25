from django.shortcuts import render,redirect
from product.models import CakePr,CommentBox
# Create your views here.
def pro(request):
    return render(request,'test.html')

def prodetails(request):
    if 'id' in request.GET:
        ids=request.GET['id']
    elif 'nam' in request.GET:
        nam=request.GET['nam']
        namobj=CakePr.objects.get(Name=nam)
        ids=namobj.id

    data=CakePr.objects.get(id=ids) #id is database id compare with ids to take the product
    if "recent_views" in request.session:           #another area in cookies
        if ids in request.session["recent_views"]:
            request.session["recent_views"].remove(ids)

        
        if len(request.session["recent_views"])>4:
            request.session["recent_views"].pop()
        print('hiiiii', request.session["recent_views"])
        recent=[]
        for i in request.session["recent_views"]:
            recent.append(CakePr.objects.get(id=i))
        request.session["recent_views"].insert(0,ids)
        request.session.modified=True
        
        return render(request,'single-product.html',{"prodetails":data,"recent":recent})

        #recent=CakePr.objects.filter(id__in=request.session["recent_views"]) #id__in to take multiple values
        #print("hello", recent) 
    else:
        request.session["recent_views"]=[ids]  #is the list method for creating empty list
        request.session.modified=True

        #return render(request,'single_post.html',{"prodetails":data})
        return render(request,'single-product.html',{"prodetails":data})


def commentarea(request):
    cmd=request.GET['cmt']
    user=request.GET['user']
    pro=request.GET['pro']
    comment=CommentBox.objects.create(User=user,Comment=cmd,pro_id=pro)  #insert comment in sql, User in models, user we created in commentarea, pro_if since FOREIGNKEY
    comment.save();
    return redirect ('/pro/?id='+pro)

    