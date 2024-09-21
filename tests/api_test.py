import pytest
from fastapi.testclient import TestClient
from src.facebook_api.router import router
from src.facebook_api.schemas import TextMessage, PhotoMessage
from src.config import TEST_RECIPIENT_ID, TEST_MESSAGE_TEXT, TEST_MESSAGE_PHOTO

client = TestClient(router)

def test_send_message():
    message = TextMessage(recipient_id=f'{TEST_RECIPIENT_ID}', message_text=f'{TEST_MESSAGE_TEXT}')
    response = client.post("/send_message", json=message.model_dump())
    
    assert response.status_code == 200
    assert response.json() == {"status": "success", "response": response.json()}

def test_send_photo():
    message = PhotoMessage(recipient_id=f'{TEST_RECIPIENT_ID}', image_url=f'{TEST_MESSAGE_PHOTO}', is_reusable=True)
    response = client.post("/send-photo", json=message.model_dump())
    
    assert response.status_code == 200
    assert response.json() == {"status": "success", "response": response.json()}