from fastapi import APIRouter, Form, HTTPException, Query
from fastapi.responses import Response
import requests
from src.facebook_api.schemas import TextMessage, SuccessMessage, PhotoMessage
from src.config import PAGE_ACCESS_TOKEN, PAGE_ID
import httpx

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/send_message")
async def send_message(message: TextMessage) -> SuccessMessage:
    """Отправить сообщение пользователю через Facebook API."""
    url = f"https://graph.facebook.com/v20.0/{PAGE_ID}/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {
            "id": message.recipient_id
        },
        "messaging_type": "RESPONSE",
        "message": {
            "text": message.message_text
        }
    }
    
    response = requests.post(url, json=payload)
    print(response)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json().get("error", "Ошибка при отправке сообщения."))
    
    return {"status": "success", "response": response.json()}


@router.post("/send-photo")
async def send_photo(message: PhotoMessage) -> SuccessMessage:
    url = f"https://graph.facebook.com/v20.0/{PAGE_ID}/messages?access_token={PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {
            "id": message.recipient_id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": message.image_url,
                    "is_reusable": message.is_reusable
                }
            }
        }
    }
    response = requests.post(url, json=payload)
    print(response)
    return {"status": "success", "response": response.json()}