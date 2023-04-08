from typing import Dict

from app.main.feature.dto.feature_dto import FeatureRequest, FeatureResponse


class FeatureService:
    
    def __init__(self, feature_request: FeatureRequest = None) -> None:
        self.name = feature_request.name if feature_request else None
    

    def say_hello_service(self) -> FeatureResponse:
        if self.name == None:
            message = "Hello World"
        else:
            message = f"Hello {self.name}"
        return FeatureResponse(message=message)