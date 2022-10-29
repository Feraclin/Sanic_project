import os

from web.app import setup_app

app = setup_app(name='api', config_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.yml"))

if __name__ == "__main__":
    app.run(access_log=True, debug=True)
