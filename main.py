if __name__ == "__main__":

    import uvicorn
    import os

    uvicorn.run("app:app", reload=True, host='0.0.0.0',port=int(os.getenv('FAST_API_PORT','8000')))
