from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from router import login_user_router
from component.token_manager import validate_jwt


# user_model.Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(login_user_router.router)


AUTH_FAIL_RESPONSE = JSONResponse(
    content={'message': 'need auth token'}, status_code=400)


# 대부분 인증이 필요하면 예외 API 를 셋팅해서 사용
PASS_AUTH_URLS = {
    '/': {'GET'},
    '/login': {'POST'}
}


@app.middleware('http')
async def pass_url_checker(request: Request, call_next):
    path = request.url.path
    method = request.method
    if (not(PASS_AUTH_URLS.get(path) and method in PASS_AUTH_URLS.get(path))):
        token = request.cookies.get('auth_token')
        if (token is None or validate_jwt(token) is False):
            return AUTH_FAIL_RESPONSE
    response = await call_next(request)
    return response
