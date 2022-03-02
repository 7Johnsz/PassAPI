from fastapi import FastAPI

import uvicorn

# Server


class Server():
    def __init__(self, ):
        self.manager = FastAPI(
            title="API",
            version="1.0.1",
            docs="/docs",
            author="Johnsz",
        )

    def run(self, ):
        uvicorn.run(
            self.manager,
            host="127.0.0.1",
            port=8080
        )
    


server = Server()
