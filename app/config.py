import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
#        'postgresql://pergentino:098765@db:5432/gala'
#         'postgresql+psycopg2://neondb_owner:npg_OZt6YRgW7ASF@ep-dry-meadow-adyj4mki-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
        'postgresql+psycopg2://neondb_owner:npg_mUPGMj0O5eyq@ep-green-boat-adjdm91u-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
    )

    # Carpeta para subir recibos
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', '/app/uploads')

    # Configuración de correo (Gmail con App Password)
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "membilambasipergentino@gmail.com"
    MAIL_PASSWORD = "euwnlfxmgfcpseeh"  # App Password de 16 caracteres
    MAIL_DEFAULT_SENDER = ("Gala Tickets", "membilambasipergentino@gmail.com")
#    SERVER_NAME = "192.168.1.11:5000"

