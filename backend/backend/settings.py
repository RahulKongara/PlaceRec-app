from pathlib import Path


import secrets
import string

# chars = string.ascii_letters + string.digits + string.punctuation
# secret_key = ''.join(secrets.choice(chars) for _ in range(50))


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = ",1j0]DZkc\rGT:>r4BxL)=`}76N003gqCj[G<hL*#ziYzNnICY"          # replace in prod!
DEBUG = True

ALLOWED_HOSTS = [
    "https://placerec-app.onrender.com", 
    "localhost",
    ]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "landmarks",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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
# default from startproject
WSGI_APPLICATION = "backend.wsgi.application"
ASGI_APPLICATION = "backend.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",   # React/Vite dev server
    "http://127.0.0.1:5173",
    "https://place-rec-app.vercel.app/",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"


# … plus AUTH_PASSWORD_VALIDATORS, LANGUAGE_CODE, TIME_ZONE, etc.
