import json
import os


class BaseConfig(object):
    cur_dir = os.path.join(*os.path.abspath(__file__).split('/')[:-1])
    conf_file_path = os.path.join('/', cur_dir, 'conf.json')
    data = json.loads(open(conf_file_path).read())

    SECRET_KEY = 'very secret key'
    SERVER_NAME = data['server']


class DevelopmentConfig(BaseConfig):
    DEBUG = BaseConfig.data['debug']
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://sogues:123@180.76.239.229:3306/{}?charset=utf8'.format(BaseConfig.data['database'])


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
        }

if __name__ == "__main__":
    print(configs['development'].SERVER_NAME)
    print(configs['development'].SECRET_KEY)
    print(configs['development'].DEBUG)
    print(configs['development'].SQLALCHEMY_DATABASE_URI)
