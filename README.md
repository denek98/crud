## Setup

### Install requirements

```bash
pip install -r requirements.txt
```

# Simple Car Logistic CRUD Project
Here is a primitive CRUD project using Fast Api as ASGI, Piccolo as ORM and Docker as container

## Stuff used
* FastAPI
* Piccolo ORM
* Postgres

### How to run
1. Clone the repo
```sh
git clone https://github.com/denek98/car_crud
```
2. Build up Docker
```sh
cd car_crud
docker-composer up --build -d
```

To shut the docker containers down simply run
```sh
docker-compose down
```

### Good to know
There's a `.env` file included to set the needed environment variables for the different parts of the app to run.