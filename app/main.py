from flask import Flask
from app.controller.controller import router

deepsea_app = Flask()

deepsea_app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(deepsea_app, host="localhost", port=5000)
