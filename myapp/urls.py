from django.urls import path
from .views import classroomqs, home, root_page, temp_inherit,portfolio,classroom

urlpatterns = [
    path('home/', home),
    path('temp-inherit-home/',temp_inherit,name="temp_inherit"),
    path("portfolio/",portfolio, name="portfolio"),
    path("classroom/",classroom,name="classroom"),
    path("classroom-qs/",classroomqs,name="classroom_qs"),
    path("",root_page, name='root_page')
]

