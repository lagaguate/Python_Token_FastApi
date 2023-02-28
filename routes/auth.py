from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from function_jwt import write_token, validate_token

auth_routes = APIRouter()

class User(BaseModel):
    username: str
    email: EmailStr

@auth_routes.post("/login")
def login(user:User):
    print("=== POST LOGIN ===")
    print(user.dict())
    
    ## Se valido contra BD y todo OK
    if True:
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message":"User not found"},status_code=404)

@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    print ("*** verify token")
    print (Authorization)
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)

