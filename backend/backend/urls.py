from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path

from webapp.views import QuestionView, UserView, RankView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/', csrf_exempt(QuestionView.as_view())),
    path('user/', csrf_exempt(UserView.as_view())),
    path('rank/', csrf_exempt(RankView.as_view()))
]
