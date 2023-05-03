from config import URL 
from src.core import Core, Response


class UserEndPoint():
    def __init__(self):
        self.base_url = URL
        self.request = Core()

    def login_user(self) -> Response:
        response = self.request.get(url=self.base_url+'/user/login')
        return response

