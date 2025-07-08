from pydantic_settings import BaseSettings
from pydantic import Field

class APIConfig(BaseSettings):
    """
    Configuration for the Barcode API.
    """
    barcode_upload_img_api_url: str = Field(default="http://localhost:8000/api/v1/image/upload-image/")
    barcode_read_api_url: str = Field(default="http://localhost:8000/api/v1/image/read-barcode/")
    ocr_upload_img_api_url: str = Field(default="http://localhost:8000/api/v1/image/upload-image/")
    ocr_extract_text_api_url: str = Field(default="http://localhost:8000/api/v1/ocr/extract-text/")
    gateway_api_key: str = Field(alias="GATEWAY_API_KEY", default="test")
