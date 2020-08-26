from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from api.views import PlayaViewSet, TopPlayaViewSet

router = DefaultRouter()
#router2 = DefaultRouter()
router.register(r'api',PlayaViewSet)
router.register(r'apiTop6',TopPlayaViewSet)

urlpatterns = router.urls

#urlpatterns += router2.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls)
]
