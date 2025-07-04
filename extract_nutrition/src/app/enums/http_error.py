from enum import Enum

class HttpError(Enum):
    METADATA_NOT_FOUND = "Metadata not found"
    IMAGE_NOT_VALID = "Image is not valid"
    IMAGE_NOT_VALIDATED_FOR_OCR = "Image isn't validated for OCR"