class Config(object):
	pass


class DevelopmentConfig(Config):
    DEBUG=True
    WTF_CSRF_SECRET_KEY = "a very secret key"
