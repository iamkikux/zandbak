from fastapi import FastAPI
from fastapi.responses import RedirectResponse,Response



app = FastAPI()


@app.get("/health-check/")
def health_check():
    return {"message": "OK"}

@app.get("/login", response_class=RedirectResponse)
async def login_okta():
    return RedirectResponse(url="https://dev-98713027.okta.com/oauth2/v1/authorize?client_id=0oa6o221jtMVJ50Vt5d7&response_type=code&response_mode=query&scope=openid&redirect_uri=http://localhost:8000/authorization-code/callback&state=relsa&nonce=9d796220-1c55-4eb1-a41b-aef2c70fb420")

@app.get("/authorization-code/callback", response_class=Response)
def auth_callback():
    print("callback")