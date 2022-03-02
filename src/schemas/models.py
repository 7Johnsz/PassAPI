from fastapi import FastAPI
from fastapi.responses import JSONResponse

from typing import Optional
from pydantic import BaseModel

# Schemas

class Password(BaseModel):
    length: int

    def length(self, length):
        self.length = length

        return self.length

password = Password()
    
