from fastapi import FastAPI,APIRouter
from linebot import WebhookHandler
from linebot.v3.messaging import Configuration

app = FastAPI()

config = Configuration(access_token='LINE_CHANNEL_SECRET')
handler = WebhookHandler('LINE_CHANNEL_ACCESS_TOKEN')
router = APIRouter(prefix="", tags=["line_bot"])
