from .common import *

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     'prj_db',                  # DB 이름
        'USER':     'root',                # DB 사용자 이름
        'PASSWORD': 'mysql1229',                # DB 비밀번호
        'HOST':     '127.0.0.1',               # DB 서버 주소
    }
}