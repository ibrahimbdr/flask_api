from flask import Blueprint

auth = Blueprint("auth", __name__,
                 url_prefix="/api/v1/auth")

@auth.post('/regester')
def regester():
    return "User created"

@auth.get("/me")
def me():
    return {"user": "me"}