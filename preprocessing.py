import pandas as pd

from app.schemas.prediction import PredictionRequest


def request_to_dataframe(request: PredictionRequest, known_locations: set[str]) -> pd.DataFrame:
    location_grouped = request.location if request.location in known_locations else "other"
    return pd.DataFrame([{
        "area_sqft": request.area_sqft,
        "floor_num": request.floor_num,
        "bathroom": request.bathroom,
        "balcony": request.balcony,
        "location_grouped": location_grouped,
        "Furnishing": request.furnishing,
        "Transaction": request.transaction,
        "Ownership": request.ownership,
        "facing": request.facing,
    }])
