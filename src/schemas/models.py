from pydantic import BaseModel

# Schemas

class Password(BaseModel):
    length: int
    
    class Config:
        extra = "forbid"
