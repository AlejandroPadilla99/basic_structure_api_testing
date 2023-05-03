#lib
import requests
from dataclasses  import dataclass

@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict

class Core:
    def get(self, url: str, headers: dict) -> Response:
        response = requests.get(url=url, headers=headers)
        return self._get_responses(response)

    def post(self, url: str, playload: str, headers: dict) -> Response:
        response = requests.post(url=url, playload=playload, headers=headers)
        return self._get_responses(response)

    def put(self, url: str, playload: str, headers: dict) -> Response:
        response = requests.put(url=url, playload=playload, headers=headers)
        return self._get_responses(response)

    def delete(self, url: str, headers: dict) -> Response:
        response = requests.delete(url=url, headers=headers)
        return self._get_responses(response)

    @staticmethod
    def _print_logs(method: str, url: str, playload: str, headers: str, response: str) -> None:
        return

    @staticmethod
    def _get_responses(response: str) -> Response:
        status_code = response.status_code
        text = response.text
        
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(status_code, text, as_dict, headers)

