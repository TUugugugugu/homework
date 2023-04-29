from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name="register"),
    path('homeworks/', views.homeworks, name="homeworks"),
    path('homework/add', views.homework_add, name="homework_add"),
    path('homework/edit/<int:id>', views.homework_edit, name="homework_edit"),
    path('homework/delete/<int:id>', views.homework_delete, name="homework_delete"),
    path('homework/done/<int:id>', views.homework_done, name="homework_done"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
