import secrets

class Config:
    secrets.token_urlsafe(32)
    FLASK_ENV='production'