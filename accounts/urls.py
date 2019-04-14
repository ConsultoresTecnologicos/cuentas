from django.urls import path, include

from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()
router.register(r"accounts", views.AccountsViewSet)

urlpatterns = [path("", include(router.urls))]
