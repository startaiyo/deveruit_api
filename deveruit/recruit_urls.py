from django.urls import path, include
from deveruit import views
from rest_framework.routers import DefaultRouter

app_name = 'recruit'

router = DefaultRouter()
router.register('recruit', views.RecruitmentViewSet, basename="recruit")
router.register('myrecruit', views.MyRecruitmentViewSet, basename="myrecruit")
router.register('request', views.RequestViewSet, basename="request")
router.register('message', views.MessageViewSet, basename="message")
router.register('request/<int:msg_id>',views.RequestToMessageViewSet,basename="requestmsg")

urlpatterns = [
    path('', include(router.urls))
]
