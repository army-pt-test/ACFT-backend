from django.urls import path
from . import views

urlpatterns = [
    path('cadet/', views.CadetList.as_view(), name='cadet_list'),
    path('cadet/<int:pk>', views.CadetDetail.as_view(), name='cadet_detail')
]
