from pydantic import BaseModel

class FeatureRequest(BaseModel):
    name : str

class FeatureResponse(BaseModel):
    message: str