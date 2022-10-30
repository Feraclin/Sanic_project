from dataclasses import dataclass
from typing import TYPE_CHECKING

import yaml

if TYPE_CHECKING:
    from sanic import Sanic


@dataclass(slots=True)
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    database: str


@dataclass(slots=True)
class DefaultAdminConfig:
    name: str
    password: str


def setup_config(app: "Sanic", config_path: str):
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)

    app.config.db_config = DatabaseConfig(**raw_config["database"])
    app.config.default_admin = DefaultAdminConfig(**raw_config["default_admin"])
    app.config.private_key = raw_config["private_key"]
    app.config.secret = raw_config["secret"]
