from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import get_csrf_token
from .templatetags import custom_filters

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

ADMIN_ENABLED = False

@ensure_csrf_cookie
def csrf(request):
    return JsonResponse({'message': 'csrf cookie set'})

def block_admin(request):
    return HttpResponseForbidden("Доступ запрещён")

def block_swagger(request):
    return HttpResponseForbidden("Swagger закрыт")

def home(request):
    return HttpResponse("Главная страница сайта. Админка отключена или включена.")

def home(request):
    return HttpResponse("Xush Kelibsiz KRAFTO-AGENCY Admin   - http://127.0.0.1:8000/ <- yonidan admin/ shu sozmi yozing -- http://127.0.0.1:8000/admin/ javob shunday bolishi kerak")

class AdminAccessControlMiddleware:
    ALLOWED_IPS = ['127.0.0.1']  # разрешённые IP для доступа к админке

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.META.get('REMOTE_ADDR') not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Доступ к админке запрещён")
        return self.get_response(request)

schema_view = get_schema_view(
    openapi.Info(
        title="DRF SHOP API",
        default_version='v1',
        description="Tash-Cleaning",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rizotoha1978@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

item_id_param = openapi.Parameter('id', openapi.IN_PATH, description="ID объекта", type=openapi.TYPE_INTEGER, example=123)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/csrf/', csrf),
    path('', home, name='home'),
    path("api/ckeditor5/", include('django_ckeditor_5.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/comment/", include('comment.urls')),
    path("api/junko/", include('junko.urls')),
    path("api/andeli/", include('andeli.urls')),
    path("api/deye/", include('deye.urls')),
    path("api/dyness/", include('dyness.urls')),
    path("api/edison/", include('edison.urls')),
    path("api/growat/", include('growat.urls')),
    path("api/gybrid/", include('gybrid.urls')),
    path("api/hz_solar/", include('hz_solar.urls')),
    path("api/invt/", include('invt.urls')),
    path("api/era_solar/", include('era_solar.urls')),
    path("api/skidka_product/", include('skidka_product.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path("api/category/", include('category.urls')),
    path("api/solnechnye_paneli/", include('solnechnye_paneli.urls')),
    path("api/invertory/", include('invertory.urls')),
    path("api/akkumlyatory/", include('akkumlyatory.urls')),
    path("api/individualnyj_teplovoj_punkt/", include('individualnyj_teplovoj_punkt.urls')),
    path("api/zaryadnyj_stancii/", include('zaryadnyj_stancii.urls')),
    path("api/vetrovaya_elektrostancii/", include('vetrovaya_elektrostancii.urls')),
    path("api/dizel_generatory/", include('dizel_generatory.urls')),
    path("api/colnechnyj_osvesheniya/", include('colnechnyj_osvesheniya.urls')),
    path("api/ctabilizatory/", include('ctabilizatory.urls')),
    path('api/application', include('application.urls')),
    path("api/category_all/", include('category_all.urls')),
    path("api/logo/", include('logo.urls')),
    path("api/shop_category/", include('shop_category.urls')),
    path("api/searchpro/", include('searchpro.urls')),
    path("api/accounts/", include('accounts.urls')),
    path("api/product_services/", include('product_services.urls')),
    path("api/services/", include('services.urls')),
    path("api/myblogyourapp/", include('myblogyourapp.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/shop/auth/', include('djoser.urls')),
    path('api/shop/auth/', include('djoser.urls.jwt')),

    # redirect to swagger
    path('', lambda request: redirect('schema-swagger-ui')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if ADMIN_ENABLED:
    urlpatterns.append(path('admin/', admin.site.urls))