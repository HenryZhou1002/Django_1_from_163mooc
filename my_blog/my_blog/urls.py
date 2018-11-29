"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from my_blog.my_blog.views import hello
from my_blog.my_blog import views
# 导入包module一直提示出错，或者是没有这个module。。。。很奇怪
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',views.hello),

]




if __name__=="__main__":
    print("----------------------------")

