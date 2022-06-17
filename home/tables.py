from ast import For
from piccolo.table import Table
from piccolo.columns import Varchar, Boolean, ForeignKey, Integer, UUID


class Gps(Table):
    """
    An example table.
    """

    car_vin_code = Varchar(17, unique=True)
    latitude = Varchar(10, null=True)
    longitude = Varchar(10, null=True)


class Car(Table):
    """
    Car table
    """

    vin_code = Varchar(17, unique=True)
    color = Varchar(20, default='White', null=True)
    start_mileage = Integer(defualt=0, null=True)
