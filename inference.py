import json

import joblib
import numpy as np

from app.core.config import settings
from app.schemas.prediction import PredictionRequest
from app.services.preprocessing import request_to_dataframe


class ModelService:
    def __init__(self) -> None:
        self.model = None
        self.known_locations: set[str] = set()

    def load(self) -> None:
        self.model = joblib.load(settings.model_path)
        with open(settings.locations_path) as f:
            self.known_locations = set(json.load(f))

    def predict(self, request: PredictionRequest) -> float:
        frame = request_to_dataframe(request, self.known_locations)
        log_price = self.model.predict(frame)[0]
        return float(np.expm1(log_price))


model_service = ModelService()
