from django.urls import path, include
from deveruit import views
from rest_framework.routers import DefaultRouter

app_name = 'recruit'

router = DefaultRouter()
router.register('recruit', views.RecruitmentViewSet, basename="recruit")
router.register('request', views.RequestViewSet, basename="request")
router.register('message', views.MessageViewSet, basename="message")

urlpatterns = [
    path('', include(router.urls))
]
