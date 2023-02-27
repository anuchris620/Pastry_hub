from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from product.models import CakePr
from django.urls import reverse

class cakeupdate(Feed):
    title="Pastry_hub"
    link="/drcomments/"
    discription="A gorgeous selection of our favorites cakes for our client as a gift."
    def items(self):
        return CakePr.objects.all()[:4]
    def item_title(self, item):
        return item.Name
    def item_description(self, item):
        return truncatewords(item.Discpt,20) #for cutting words
    def item_link(self, item):
        return reverse('home')
    

