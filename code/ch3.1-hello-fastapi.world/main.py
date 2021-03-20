import fastapi
import uvicorn
from uvicorn.main import main

app = fastapi.FastAPI()


@app.get('/')
def index():
    return {'message': "Hello x World"}


if __name__ == '__main__':
    uvicorn.run(app)
else:
    pass