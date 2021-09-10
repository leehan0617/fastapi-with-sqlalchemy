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
    '/docs': {'GET', 'POST'},
    '/openapi.json': {'GET'},
    '/login': {'POST'}
}


@app.middleware('http')
async def pass_url_checker(request: Request, call_next):
    path = request.url.path
    method = request.method
    print(path)
    for key, item in PASS_AUTH_URLS.items():
        print(key)
        if path.startswith(key) and method in item:
            print('dont need check token')
            print(path)
            pass_url = True
            break

    if (not pass_url):
        print(f'current path ${path} need to check token')
        token = request.cookies.get('auth_token')
        if (token is None or validate_jwt(token) is False):
            return AUTH_FAIL_RESPONSE
    response = await call_next(request)
    return response
