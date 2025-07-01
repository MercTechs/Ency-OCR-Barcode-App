import hatchet
from tasks.example_task import upload_image_task
from database.connection import DatabaseConnection
from tasks.example_task import upload_image_task, hatchet, validate_image_task, extract_text_task
# Initialize Hatchet worker
upload_image_worker = hatchet.worker("upload_image_worker", workflows=[upload_image_task, validate_image_task, extract_text_task])