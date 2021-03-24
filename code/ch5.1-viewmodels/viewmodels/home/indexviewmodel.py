from typing import List

from starlette.requests import Request

from services import package_service, user_service
from viewmodels.shared.viewmodel import ViewModelBase

class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.release_count: int = package_service.release_count()
        self.package_count: int = package_service.package_count()
        self.user_count: int = user_service.user_count()
        self.packages: List = package_service.latest_packages(limit=5)

        # {
        #     'package_count': 274_000,
        #     'release_count': 2_234_847,
        #     'user_count': 78_169,
        #     'packages': [
        #         {'id': 'fastapi', 'summary': "A great web framework"},
        #         {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
        #         {'id': 'httpx', 'summary': "Requests for an async world"}
        #     ]
        # }