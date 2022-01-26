from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="home"),
    path('home',views.index,name="home"),
    path('company_login',views.company_login,name="company_login"),
    path('company1',views.companylog,name="company1"),
    path('addjob',views.addjob,name="addjob"),
    path('reg_comp',views.reg_comp,name="reg_comp"),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('studentlog',views.studentlog,name="studentlog"),
    path('apply',views.student_apply,name="apply"),
    path('studentregister',views.studentregister,name="studentregister"),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)