
from app.main.feature import feature_router
from app.main.feature.dto.feature_dto import FeatureRequest
from app.main.feature.service.feature_service import FeatureService, FeatureResponse

@feature_router.post("/hello")
def say_hello(feature_request: FeatureRequest = None) -> FeatureResponse:
    service_response = FeatureService(feature_request)
    return service_response.say_hello_service()