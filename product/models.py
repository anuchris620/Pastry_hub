from django.db import models

class CakePr(models.Model):  #inheritance
    Name=models.CharField(max_length=200)                             #creating field system
    Price=models.IntegerField()
    Img=models.ImageField(upload_to='pic') #create a folder and put the imge else the photo will be save in basedr
    Qty=models.FloatField()
    Discount=models.IntegerField(default=0)
    Discpt=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)     #take the correct date. 
    
class CommentBox(models.Model):
    pro=models.ForeignKey(CakePr,related_name='Comments',on_delete=models.CASCADE)
    User=models.CharField(max_length=200)
    Comment=models.TextField()
    Date=models.DateTimeField(auto_now_add=True)

