from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Integer
from piccolo.columns.column_types import Varchar
from piccolo.columns.indexes import IndexMethod


ID = "2022-06-17T05:42:30:932823"
VERSION = "0.78.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="home", description=DESCRIPTION
    )

    manager.add_table("Car", tablename="car")

    manager.add_table("Gps", tablename="gps")

    manager.add_column(
        table_class_name="Car",
        tablename="car",
        column_name="vin_code",
        db_column_name="vin_code",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 17,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": True,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Car",
        tablename="car",
        column_name="color",
        db_column_name="color",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 20,
            "default": "White",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Car",
        tablename="car",
        column_name="start_mileage",
        db_column_name="start_mileage",
        column_class_name="Integer",
        column_class=Integer,
        params={
            "defualt": 0,
            "default": 0,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Gps",
        tablename="gps",
        column_name="car_vin_code",
        db_column_name="car_vin_code",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 17,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": True,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Gps",
        tablename="gps",
        column_name="latitude",
        db_column_name="latitude",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 10,
            "default": "",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Gps",
        tablename="gps",
        column_name="longitude",
        db_column_name="longitude",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 10,
            "default": "",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    return manager
