from environs import Env

env = Env()
env.read_env()


def create_config_obj(env_setting):
    new_config = Config()
    with env.prefixed(env_setting):
        new_config.DEBUG = env.bool("DEBUG", default=False)
        new_config.TESTING = env.bool("TESTING", default=False)
    return new_config


class Config(object):
    # Flask Settings
    SECRET_KEY = env.str("FLASK_SECRET_KEY")


DevelopmentConfig = create_config_obj("DEV_")
# TestingConfig = create_config_obj("TESTING_")
# ProductionConfig = create_config_obj("PROD_")
