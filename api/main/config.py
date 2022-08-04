"""
main.config
~~~~~~~~~~
This module contains default configuration for Flask app.
Configuration for specific deployment environment should be overridden.
:copyright: (c) 2022 by Mohammad Abudayyeh.
:license: All Rights Reserved, see LICENSE for more details.
"""

import os
import secrets
from pathlib import Path


def get_instance_path(parent_dir=""):
    """Get path to instance folder (will be created if not exist).
    :param parent_dir: Parent directory of instance folder (default to users' home directory).
    :return: Absolute path to instance folder.
    """

    parent_dir = parent_dir or Path.home()
    instance_path = Path(parent_dir).joinpath(".secrets")
    instance_path.mkdir(parents=True, exist_ok=True)
    return instance_path.resolve()


class BaseConfig:
    """
    Sets and/or gets the basic environment configuration.
    This class is not supposed to be used directly, use the subclasses instead.
    """

    ENV = ""
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MySQL Settings
    SQLALCHEMY_DATABASE_URI_FILEPATH = os.getenv("SQLALCHEMY_DATABASE_URI_FILEPATH", "/sql_secrets/uri")
    with open(SQLALCHEMY_DATABASE_URI_FILEPATH) as f:
        # "mysql+pymysql://user:password@host:port/db?charset=utf8"
        SQLALCHEMY_DATABASE_URI = f.read()
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("\n", "")

    SECRET_KEY = secrets.token_urlsafe(32)
    # Used in hashing passwords
    SECRET_SALT = secrets.token_urlsafe(32)

    # OpenAPI
    API_TITLE = "Favorite Tree API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_YAML_PATH = "favorite-tree-swagger.yaml"
    OPENAPI_URL_PREFIX = "/api"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    API_SPEC_OPTIONS = {
        "security": [{"bearerAuth": []}],
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            }
        },
    }
    DEFAULT_PAGINATION_PARAMETERS = {"page": 1, "page_size": 10,
                                     "max_page_size": 100}

    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300


class DevelopmentConfig(BaseConfig):
    """
    Sets and/or gets the development environment configuration.
    The uppercase attributes can be override in ``$HOME/.cloud/development_config_override.py``.
    """

    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    """
    Sets and/or gets the testing environment configuration.
    The uppercased attributes can be overriden in ``$HOME/.cloud/testing_config_override.py``.
    """

    ENV = "testing"
    TESTING = True


class StagingConfig(BaseConfig):
    """
    Sets and/or gets the staging environment configuration.
    The uppercased attributes can be overriden in ``$HOME/.cloud/staging_config_override.py``.
    """

    ENV = "staging"
    DEBUG = False


class ProductionConfig(BaseConfig):
    """
    Sets and/or gets the production environment configuration.
    The uppercased attributes can be overriden in ``$HOME/.cloud/production_config_override.py``.
    """

    ENV = "production"
    DEVELOPMENT = False
    DEBUG = True
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
    "default": TestingConfig,
}


class ConfigLoader:
    """
    Sets config from passed argument, env environment and defaults to the default set in config dictionary.
    """

    @staticmethod
    def check_config_name(config_env):
        """
        Returns true or false checking the validity of the config_env variable
        :param config_env: the config_env that should match the provided keys in config dictionary
        :return:
        """
        return config_env in config

    @staticmethod
    def set_config(args):
        """
        Sets config from argument passed if failed tries from env environmental variable and
         lastly defaults to the default inside config dictionary
        :param args: list of arguments passed
        :return:
        """
        try:
            if ConfigLoader.check_config_name(args[1]):
                # TODO: Add logger info that env was passed through argument
                return config.get(args[1])
        except IndexError:
            # TODO: Add logger warning that env was not passed through argument
            pass

        # TODO: Add logger info that an attempt to get the env through the env environmental variable
        # Check os env var
        env = os.environ.get("FLASK_ENV")
        if ConfigLoader.check_config_name(env):
            # TODO: Add logger info that config was set through the env environmental variable
            return config.get(env)
        # TODO: Add logger warning  that no matching env was found for loading config.
        # TODO: Add logger info that configs were set to the default in config dict.
        # Nothing worked, return default config
        return config.get("default")
