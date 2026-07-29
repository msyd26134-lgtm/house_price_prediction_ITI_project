from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_path: str = "../model/house_price.pkl"
    locations_path: str = "../model/locations.json"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
