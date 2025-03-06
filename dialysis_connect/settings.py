import dj_database_url
from pathlib import Path
import os
import environ
import cloudinary

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent  

# Load environment variables
env = environ.Env()
environ.Env.read_env()

# Cloudinary settings
cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"),
    api_key=env("CLOUDINARY_API_KEY"),
    api_secret=env("CLOUDINARY_API_SECRET"),
)
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": env("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": env("CLOUDINARY_API_KEY"),
    "API_SECRET": env("CLOUDINARY_API_SECRET"),
}

# Load environment variables
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost") or "*"
ALLOWED_HOSTS = ALLOWED_HOSTS.split(",") if ALLOWED_HOSTS != "*" else ["*"]


DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
    }
else:
    print("⚠️ Warning: DATABASE_URL is missing. Using default PostgreSQL settings.")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("PGDATABASE", "dialysis_diary"),
            "USER": os.getenv("PGUSER", "postgres"),
            "PASSWORD": os.getenv("PGPASSWORD", ""),
            "HOST": os.getenv("PGHOST", "127.0.0.1"),
            "PORT": os.getenv("PGPORT", "5432"),
        }
    }    
# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "cloudinary_storage",
    "cloudinary",
    "dialysis_connect",
    "pages",
    "users",
    "community",
    "records",
    "calendar_app",
    "uploads",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Templates
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

# WSGI application
WSGI_APPLICATION = "dialysis_connect.wsgi.application"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Localization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "calendar_app/static",
    BASE_DIR / "community/static",
    BASE_DIR / "records/static",
    BASE_DIR / "pages/static",
    BASE_DIR / "uploads/static",
    BASE_DIR / "users/static",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files settings
MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Authentication settings
LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "/users/dashboard/"

# Google Calendar API settings
GOOGLE_CALENDAR_CREDENTIALS = BASE_DIR / "calendar_app/credentials.json"
GOOGLE_REDIRECT_URI = "http://localhost:8000/calendar/oauth/callback/"
GOOGLE_CREDENTIALS_PATH = env("GOOGLE_CREDENTIALS_PATH", default="calendar_app/credentials.json")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "dialysis_connect.urls"