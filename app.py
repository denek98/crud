import typing as t

from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from piccolo_admin.endpoints import create_admin
from piccolo_api.crud.serializers import create_pydantic_model
from piccolo.engine import engine_finder
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from home.endpoints import HomeEndpoint
from home.piccolo_app import APP_CONFIG
from home.tables import Car, Gps
import asyncpg


app = FastAPI(
    routes=[
        # Route("/", HomeEndpoint),
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes,
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
        Mount("/static/", StaticFiles(directory="static")),
    ],
)


CarModelIn: t.Any = create_pydantic_model(table=Car, model_name="CarModelIn")
CarModelOut: t.Any = create_pydantic_model(table=Car, include_default_columns=True, model_name="CarModelOut")
CarModelPatch: t.Any = create_pydantic_model(table=Car, all_optional=True, model_name="CarModelPatch")

GpsModelIn: t.Any = create_pydantic_model(table=Gps, model_name="GpsModelIn")
GpsModelOut: t.Any = create_pydantic_model(table=Gps, include_default_columns=True, model_name="GpsModelOut")
GpsModelPatch: t.Any = create_pydantic_model(table=Gps, all_optional=True, model_name="GpsModelPatch")


@app.get("/", include_in_schema=False)
async def redirect():
    response = RedirectResponse(url='/docs')
    return response


@app.get("/cars/", response_model=t.List[CarModelOut], tags=['Cars'])
async def get_cars():
    '''
    Retrieving last 100 cars
    '''
    try:
        cars = await Car.select().order_by(Car.id, False).limit(100)
        if not cars:
            return JSONResponse(status_code=404, content="There is no car added")
        return cars
    except:
        return JSONResponse(status_code=404, content="404 - No items avaliable")


@app.get("/coordinates_by_id/{car_id}", response_model=t.List[GpsModelOut], tags=['Cars'])
async def get_coordinates_by_id(car_id: int):
    '''
    Get car coordinates from external table by it's ID
    '''
    try:
        vin_code = await Car.select(Car.vin_code).where(Car.id == car_id).first()
        if not vin_code:
            return JSONResponse(status_code=404, content="There is no car with this id")
        vin_code = vin_code['vin_code']
        car_coordinates = await Gps.select().where(Gps.car_vin_code == vin_code)
        if not car_coordinates:
            return JSONResponse(status_code=404, content="There is no info about coordinates for this car id")
    except:
        return JSONResponse(status_code=404, content="404 - No items avaliable")
        


@app.post("/cars/", response_model=CarModelOut, tags=['Cars'])
async def create_car(car_model: CarModelIn):
    '''
    Creating a new car
    '''
    car = Car(**car_model.dict())
    await car.save()
    return car.to_dict()


@app.patch("/cars/{car_id}/", response_model=CarModelOut, tags=['Cars'])
async def update_cars(car_id: int, task_model: CarModelPatch):
    car = await Car.objects().get(Car.id == car_id)
    if not car:
        return JSONResponse('404 - No items with this id avaliable', status_code=404)
    for key, value in task_model.dict().items():
        if value is not None:
            setattr(car, key, value)
    try:
        await car.save()
        return car.to_dict()
    except asyncpg.exceptions.UniqueViolationError:
        return JSONResponse('403 - Duplicated vin code found', status_code=403)


@app.delete("/cars/{car_id}/", tags=['Cars'])
async def delete_car(car_id: int):
    car = await Car.objects().get(Car.id == car_id)
    if not car:
        return JSONResponse('404 - No items with this id avaliable', status_code=404)

    await car.remove()

    return JSONResponse('Successfully deleted')


@app.get("/gps/", response_model=t.List[GpsModelOut], tags=['GPS'])
async def get_gps():
    '''
    Retrieving last 100 cars coordinates
    '''
    try:
        return await Gps.select().order_by(Gps.id, False).limit(100)
    except:
        return JSONResponse(status_code=404, content="404 - No items avaliable")


@app.post("/gps/", response_model=GpsModelOut, tags=['GPS'])
async def create_gps(gps_model: GpsModelIn):
    '''
    Creating a new gps
    '''
    gps = Gps(**gps_model.dict())
    await gps.save()
    return gps.to_dict()


@app.patch("/gps/{gps_id}/", response_model=GpsModelOut, tags=['GPS'])
async def update_gps(car_id: int, gps_model: GpsModelPatch):
    gps = await Gps.objects().get(Gps.id == car_id)
    if not gps:
        return JSONResponse('404 - No items with this id avaliable', status_code=404)
    for key, value in gps_model.dict().items():
        if value is not None:
            setattr(gps, key, value)
    try:
        await gps.save()
        return gps.to_dict()
    except asyncpg.exceptions.UniqueViolationError:
        return JSONResponse('403 - Duplicated vin code found', status_code=403)


@app.delete("/gps/{gps_id}/", tags=['GPS'])
async def delete_gps(gps_id: int):
    gps = await Gps.objects().get(Gps.id == gps_id)
    if not gps:
        return JSONResponse('404 - No items with this id avaliable', status_code=404)

    await gps.remove()

    return JSONResponse('Successfully deleted')


@app.on_event("startup")
async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception:
        print("Unable to connect to the database")


@app.on_event("shutdown")
async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception:
        print("Unable to connect to the database")
