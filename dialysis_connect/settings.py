"""
Django settings for dialysis_connect project.
"""

from pathlib import Path
import os
import dj_database_url
import environ

# ✅ Define BASE_DIR at the top before using it
BASE_DIR = Path(__file__).resolve().parent.parent  

# ✅ Load environment variables
env = environ.Env()
environ.Env.read_env()

# ✅ Security settings
SECRET_KEY = env("SECRET_KEY", default="django-insecure-co=%pxti!caco9fy!@j-2away)*&gadx17rh)iu(jaangcd5xh")
DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = [
    ".herokuapp.com",
    "127.0.0.1",
    "localhost",
]

# ✅ Database Configuration (Fixing the TypeError issue)
DATABASE_URL = os.environ.get("DATABASE_URL", "")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    print("⚠️ DATABASE_URL not set. Using default SQLite for local development.")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ✅ Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "pages",
    "users",
    "community",
    "records",
    "calendar_app",
    "uploads",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dialysis_connect.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dialysis_connect.wsgi.application"

# ✅ Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ✅ Localization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ✅ Static and media files settings
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ✅ Authentication settings
LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "/users/dashboard/"

# ✅ Google Calendar API settings
GOOGLE_CALENDAR_CREDENTIALS = BASE_DIR / "calendar_app/credentials.json"
GOOGLE_REDIRECT_URI = "http://localhost:8000/calendar/oauth/callback/"


# ✅ Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
