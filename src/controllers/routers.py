from fastapi.responses import JSONResponse
from src.instance.server import server
from fastapi import Request, Response
from src.schemas.models import Password
from dotenv import load_dotenv
from datetime import datetime

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

import random
import string
import os

# API Variables

load_dotenv()
AuthorizationENV = os.getenv('AUTHORIZATION')

limiter = Limiter(key_func=get_remote_address)

app = server.manager
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

# All routes using the post method in the body

@app.post("/")
@limiter.limit("50/minute")
async def root(request: Request, res: Response, passwd: Password):
    Authorization = request.headers.get('Authorization')
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if Authorization == AuthorizationENV:
        length = passwd.length

        if length >= 100:
            return JSONResponse(
                status_code=431,
                content={
                    "detail": [
                        {
                            "fields": [
                                "body",
                                "length"
                            ],
                            "msg": "Request Header Fields Too Large",
                            "timestamp": now
                        }
                    ]
                }
            )
        
        carac = lower + upper + digits + punctuation
        password = "".join(random.sample(carac, length))

        return JSONResponse(
            status_code=200,
            content={
                "detail": [
                    {
                       "password": password,
                        "timestamp": now 
                    }
                ],
            }
        )
        
    else:
        return JSONResponse(
            status_code=401,
            content={
                    "detail": [
                        {
                            "msg": "You don't have permission to access this page",
                            "timestamp": now
                        }
                    ],
                }
            )
