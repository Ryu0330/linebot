from fastapi import FastAPI,APIRouter,Header,Request
from linebot.v3.messaging import Configuration
from linebot.exceptions import InvalidSignatureErro
from linebot.models import (
    MessageEvent, TextMessage, FollowEvent, UnfollowEvent,
    TextSendMessage, ImageMessage, AudioMessage
)
from linebot import LineBotApi, WebhookHandler

config = Configuration(access_token='LINE_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('LINE_CHANNEL_SECRET')

app = FastAPI()

@app.post("/callback")
async def callback(
    request: Request,
    x_line_signature=Header(None)
):
    body = await request.body()
    body = body.decode
    

@handler.add(MessageEvent)
def handle_message(event):
    if event.type != "text":
        return
    responsemessage = event.text


