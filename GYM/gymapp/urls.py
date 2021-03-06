from django.urls import path
# from .import views
from .views import *
from gym.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('index', index, name = 'index'),
    path('upload/', upload, name = 'sachin'),
    path('update/<int:gym_id>', update_form),
    path('delete/<int:gym_id>', delete_form),
    #path('search/', search_hai),
    path('search/', search_function_hai, name="khadka"),
    # path('search/search/', search_function_hai),


]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)