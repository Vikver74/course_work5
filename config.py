class Config(object):
    pass


class DevConfig(Config):
    PATH = 'data/equipments.json'
    SECRET_KEY = b'_5#y2L"F4Q8z'
    STAMINA_PER_TURN = 1
    DEBUG = True


class ProductConfig(Config):
    PATH = 'data/equipments.json'
    SECRET_KEY = b'_5#y2L"F4Q8z'
    STAMINA_PER_TURN = 1
    DEBUG = False