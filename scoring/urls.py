from django.conf.urls import url
from .views import home
#from .views import HomeListView

urlpatterns = [

    #path('', HomeListView.as_view(), name='home'),
    url('', home, name='home'),
]
