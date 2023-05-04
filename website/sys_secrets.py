databases = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'django_users',  
        'USER': 'root',  
        'PASSWORD': '1234',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}  

secret_key = 'django-insecure-94s*wpl)lrv&6=eo8u$=xd*p_04q1&=m-egu=3p@n^oz3%q2vf'