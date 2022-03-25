
from django.urls import path

from myproject import views

app_name = 'myproject'

urlpatterns = [
    path('',views.demo2,name='demo2'),
    path('cake/<int:cake_id>',views.detail,name='detail'),
    path('add/',views.add_cake,name='add_cake'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
