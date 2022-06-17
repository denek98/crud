# Simple Car Logistic CRUD Project
Here is a primitive CRUD project using Fast Api as ASGI, Piccolo as ORM and Docker as container

## Stuff used
* FastAPI
* Piccolo ORM
* Postgres

### How to run
1. Clone the repo
```sh
git clone https://github.com/denek98/crud
```
2. Build up Docker
```sh
cd crud
docker-composer up --build -d
```
3. Go to `http://0.0.0.0:8337` in your browser (port can be changed in `.env` file)

### How to shut down
To shut the docker containers down simply run
```sh
docker-compose down
```

### Good to know
There's a `.env` file included to set the needed environment variables for the different parts of the app to run.
