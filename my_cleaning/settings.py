from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-#o$sxch!@l_6#g3h1s4wq3i)v2ss!f)ac!_nb5)s1-wep=ljot'
DEBUG = True
ALLOWED_HOSTS = [
    '*'
]
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os

from django.contrib import messages
from django.contrib.admin import ModelAdmin
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import gettext_lazy as _



class AdvancedSearchAdmin(ModelAdmin):
    """
        class to add custom filters in django admin
    """
    change_list_template = 'admin/custom_change_list.html'
    advanced_search_fields = {}
    search_form_data = None

    def get_queryset(self, request):
        """
            override django admin 'get_queryset'
        """
        queryset = super().get_queryset(request)
        try:
            return queryset.filter(self.advanced_search_query(request))
        except Exception:  # pylint: disable=broad-except
            messages.add_message(request, messages.ERROR, 'Filter not applied, error has occurred')
            return queryset.none()

    def changelist_view(self, request, extra_context=None):
        """
            Append custom form to page render
        """
        extra_context = extra_context or {}
        if hasattr(self, 'search_form'):
            self.advanced_search_fields = {}
            self.search_form_data = self.search_form(request.GET.dict())
            self.extract_advanced_search_terms(request.GET)
            extra_context.update({'asf': self.search_form_data})

        return super().changelist_view(request, extra_context=extra_context)

    def extract_advanced_search_terms(self, request):
        """
            allow to extract field values from request
        """
        request._mutable = True  # pylint: disable=protected-access

        if self.search_form_data is not None:
            for key in self.search_form_data.fields.keys():
                temp = request.pop(key, None)
                if temp:  # there is a field but it's empty so it's useless
                    self.advanced_search_fields[key] = temp

        request._mutable = False  # pylint: disable=protected-access

    def get_request_field_value(self, field):
        """
            check if field has value passed on request
        """
        if field in self.advanced_search_fields:
            value = self.advanced_search_fields[field][0]
            return bool(value), value

        return False, None

    @staticmethod
    def get_field_value_default(field, form_field, field_value, has_field_value, request):
        """
            mount default field value
        """
        if has_field_value:
            field_name = form_field.widget.attrs.get('filter_field', field)
            field_filter = field_name + form_field.widget.attrs.get('filter_method', '')

            try:
                field_value = utils.format_data(form_field, field_value)  # format by field type
                return Q(**{field_filter: field_value})
            except ValidationError:
                messages.add_message(request, messages.ERROR, _(
                    f"Filter in field `{field_name}` ignored, because value `{field_value}` isn't valid."))
            except Exception:  # pylint: disable=broad-except
                messages.add_message(request, messages.ERROR, _(
                    f"Filter in field `{field_name}` ignored, an error has occurred in filtering."))

        return Q()

    def get_field_value(self, field, form_field, field_value, has_field_value, request):
        """
            allow to override default field query
        """
        if hasattr(self, ('search_' + field)):
            return getattr(self, 'search_' + field)(field, field_value, form_field, request,
                                                    self.advanced_search_fields)

        return self.get_field_value_default(field, form_field, field_value, has_field_value, request)

    def advanced_search_query(self, request):
        """
            Get form and mount filter query if form is not none
        """
        query = Q()

        if self.search_form_data is None:
            return query

        for field, form_field in self.search_form_data.fields.items():
            has_field_value, field_value = self.get_request_field_value(field)
            query &= self.get_field_value(field, form_field, field_value, has_field_value, request)

        return query


class FrontendAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(
                "index.html not found, build your React app first", status=501,
            )

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'application.apps.ApplicationConfig',
    'main',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'category',
    'myblogyourapp',
    'rest_framework.authtoken',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'logo',
    'comment',
    'rest_framework_simplejwt',
    'services',
    'product_services',
    'searchpro',
    'shop_category',
    'category_all',
    'accounts',
    'solnechnye_paneli',
    'invertory',
    'ctabilizatory',
    'akkumlyatory',
    'colnechnyj_osvesheniya',
    'dizel_generatory',
    'individualnyj_teplovoj_punkt',
    'zaryadnyj_stancii',
    'vetrovaya_elektrostancii',
    'django_filters',
    'skidka_product',
    'junko',
    'andeli',
    'deye',
    'dyness',
    'edison',
    'era_solar',
    'growat',
    'gybrid',
    'hz_solar',
    'invt',
]

DJOSER = {
    "USER_ID_FIELD": "id",
    "LOGIN_FIELD": "username",
    'LOGIN_EMAIL': 'email',
    "SERIALIZERS": {
        "user_create": "djoser.serializers.UserCreateSerializer",
        "user": "djoser.serializers.UserSerializer",
    },
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

CLICK_SETTINGS = {
    'service_id': "<Ваш сервис ID>",
    'merchant_id': "<Ваш merchant ID>",
    'secret_key': "<Ваш секретный ключ>",
    'merchant_user_id': "<Ваш merchant user ID>",
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[{levelname}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.server': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

RECAPTCHA_SECRET_KEY = os.getenv('6Lc7ioArAAAAABqG07AEM2vHo3gD2fe7dJOh8DtB')

TELEGRAM_BOT_TOKEN = '7613975897:AAHSzOal47p9jeu62JR1sdI23-mQyb3Sk50'
TELEGRAM_CHAT_ID = '7139975148'

X_FRAME_OPTIONS='SAMEORIGIN'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'rizotoha78@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'rizotoha78@gmail.com'       # 👈 замените
EMAIL_HOST_PASSWORD = 'rt2611931rt'     # 👈 используйте App Password (не обычный пароль!)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'my_cleaning.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "staticfiles"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for admin sidebar
                'django.contrib.auth.context_processors.auth',  # Required for admin
                'django.contrib.messages.context_processors.messages',  # Required for admin
            ],
        },
    },
]

WSGI_APPLICATION = 'my_cleaning.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/


from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = "ru"

LANGUAGES = [
    ('ru', 'Русский'),
    ('uz', 'Oʻzbekcha'),
]

TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_L10N = True
USE_TZ = True

import os
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/staticfiles/'
STATICFILES_DIRS = [ BASE_DIR / 'staticfiles' ]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
                    'code', 'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|', 'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable', ],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side', '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                               'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    "DEFAULT_THROTTLE_RATES": {
    "anon": "5/day",
    "user": "5/day"
    },
}


SESSION_EXPIRE_SECONDS = 3600  # 1 hour
SESSION_COOKIE_AGE = 3600  # 1 hour
SESSION_TIMEOUT_REDIRECT = "/"
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_SECONDS = 604800

from datetime import timedelta
AXES_FAILURE_LIMIT = 5
AXES_RESET_ON_SUCCESS = True
AXES_COOLOFF_TIME = timedelta(seconds=10)


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': True,
}


CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "https://backend-dedd.onrender.com",
]
CORS_ALLOW_CREDENTIALS = True

CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = ["https://solor-energy.vercel.app", "https://backend-dedd.onrender.com"]

CSRF_COOKIE_HTTPONLY = False

CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'x-csrftoken',
    'x-requested-with',
]


CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'applications/static',  # или путь до static, если он глобальный
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

JAZZMIN_SETTINGS = {
    "site_title": "Enerji Project",
    "site_header": "Enerji Project",
    "site_brand": "Enerji Project",
    "site_icon": "../media/assets/img/logo.png",
    "copyright": "Enerji Project",

    "site_logo": "../media/assets/img/12.png",
    "language_chooser": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "welcome_sign": "Xush Kelibsiz Enerji Project",

    "copyright": "Enerji Project-admin",
    "user_avatar": "../media/assets/img/1111.jpg",
    "dashboard": [
        {"type": "link", "title": "Documentation", "url": "http://127.0.0.1:8000/swagger/"},
    ],
    "topmenu_links": [
        {"name": "Xush Kelibsiz Enerji Project Admin", "url": "home", "permissions": ["auth.view_user"]},
        {"name": "СОЛНЕЧНЫЕ ПАНЕЛИ", "url": "http://127.0.0.1:8000/admin/solnechnye_paneli/", "permissions": ["auth.view_user"]},
        {"name": "ИНВЕРТОРЫ", "url": "http://127.0.0.1:8000/admin/invertory/", "permissions": ["auth.view_user"]},
        {"name": "CТАБИЛИЗАТОРЫ", "title": "Swagger", "url": "http://127.0.0.1:8000/admin/ctabilizatory/"},
        {"name": "АККУМЛЯТОРЫ", "title": "Swagger", "url": "http://127.0.0.1:8000/admin/akkumlyatory/"},
        {"name": "CОЛНЕЧНЫЙ ОСВЕЩЕНИЯ", "title": "Swagger", "url": "http://127.0.0.1:8000/admin/colnechnyj_osvesheniya/"},
        {"name": "ДИЗЕЛЬ ГЕНЕРАТОРЫ", "title": "Swagger", "url": "http://127.0.0.1:8000/admin/dizel_generatory/producttype/"},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },
    "usermenu_links": [
        {"name": "Пользователи и группы", "url": "https://backend-dedd.onrender.com/admin/auth/"},
        {"name": "ЗАРЯДНЫЙ СТАНЦИИ", "url": "http://127.0.0.1:8000/admin/zaryadnyj_stancii/"},
        {"name": "ВЕТРОВАЯ ЭЛЕКТРОСТАНЦИИ", "url": "http://127.0.0.1:8000/admin/vetrovaya_elektrostancii/"},
        {"name": "ИНДИВИДУАЛЬНЫЙ ТЕПЛОВОЙ ПУНКТ", "url": "http://127.0.0.1:8000/admin/individualnyj_teplovoj_punkt/producttype/"},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fa-solid fa-headset",
        "auth.user": "fa-solid fa-headset",
        "auth.Group": "fas fa-users",
        "your_app.ModelName": "fa-solid fa-headset",
    },
    "default_icon_parents": "fa-solid fa-headset",
    "default_icon_children": "fa-solid fa-solar-panel",

    "related_modal_active": True,
    "custom_js": True,

    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "your_app_name"],

    "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": True,
    "brand_small_text": True,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "sticky_actions": True,
    "actions_sticky_top": True,
    "theme": "lux",
    'hide_app': True,
    'hide_title': True,
    'show_logout': True,
    'show_user_avatar': True,
    "dark_mode_theme": None,
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=100),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    "SIGNING_KEY": SECRET_KEY,  # Убедитесь, что SECRET_KEY �
}
