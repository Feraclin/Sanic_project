import os

from web.app import setup_app

if __name__ == "__main__":
    setup_app(config_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.yml"))
