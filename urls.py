
from django.contrib import admin
from django.urls import path
from . import views

#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('',views.index,name='index'),
   # path('about',views.about,name='about'),
#]

#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('',views.index,name='index'),
   # path('removepunc',views.removepunc,name='rempunc'),
    #path('capitalizefirst',views.capfirst,name='capfirst'),
    #path('newlineremove',views.newlineremove,name='newlineremove'),
    #path('spaceremove',views.spaceremove,name='spaceremove'),
    #path('charcount',views.charcount,name='charcount'),
#]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name='analyze'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
]


