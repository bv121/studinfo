 
from django.contrib import admin
from django.urls import path,include
from studentapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('stud',include(('studentapp.urls','studnewapp'),namespace='studnewapp'))

]
