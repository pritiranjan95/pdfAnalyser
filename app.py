from utils import app
from controllers import analyser_controller
from config.consts import HOST
from config.consts import PORT
import uvicorn
from tests import services


app.include_router(analyser_controller.router)

@app.get("/")
def index():
    return "PDF Analyser Services"




if __name__ == "__main__":
    uvicorn.run(app,host = HOST,port  = PORT)