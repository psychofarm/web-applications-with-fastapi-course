
from typing import Optional

from starlette.requests import Request
from starlette.responses import Response



auth_cookie_name = 'pypi_account'


def set_auth(response: Response, user_id: int):
    #
    #
    response.set_cookie(auth_cookie_name, str(user_id), secure=False, httponly=True)







def get_user_id_via_auth_cookie(request: Request) -> Optional[int]:
    if auth_cookie_name not in request.cookies:
        return None






    user_id = int(request.cookies[auth_cookie_name])






    return user_id