from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import APIKeyHeader
import os
from config.api_config import APIConfig
load_dotenv()

app = FastAPI()

# Get API key with validation
apiConfig = APIConfig()

SECRET_API_KEY = apiConfig.gateway_api_key
if not SECRET_API_KEY:
    raise ValueError("API_KEY environment variable must be set")

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def get_api_key(api_key: str = Depends(api_key_header)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key header missing",
            headers={"WWW-Authenticate": "ApiKey"}
        )
    
    if api_key != SECRET_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
            headers={"WWW-Authenticate": "ApiKey"}
        )
    
    return api_key