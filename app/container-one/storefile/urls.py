from django.urls import path

from storefile.views import StoreFileView

urlpatterns = [
    path('store-file', StoreFileView.as_view()),
]
