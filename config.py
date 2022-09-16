class Config(object):
    pass


class DevConfig(Config):
    SECRET_KEY = b'_5#y2L"F4Q8z'
    DEBUG = True


class ProductConfig(Config):
    SECRET_KEY = b'_5#y2L"F4Q8z'
    DEBUG = False
