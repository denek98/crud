from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry
import os

DB = PostgresEngine(
    config={
        "port": int(os.getenv("POSTGRES_PORT", "5432")),
        "user": os.getenv("POSTGRES_USER", "user"),
        "password": os.getenv("POSTGRES_PASSWORD", ""),
        "database": os.getenv("POSTGRES_DB", "db"),
        "host": os.getenv("POSTGRES_HOST", "localhost"),
    }
)

APP_REGISTRY = AppRegistry(apps=["home.piccolo_app", "piccolo_admin.piccolo_app"])
