from django.urls import path
from .views import Index , applianceDetail

urlpatterns = [ 
    path('', Index.as_view(), name='home'),
    path('/<slug:pk>/', applianceDetail.as_view(), name='appliance-detail'),
]
