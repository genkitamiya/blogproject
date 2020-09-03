from django.contrib import admin
from django.urls import path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', BlogList.as_view()),
    path('detail/<int:pk>', BlogDetail.as_view())
]
