from fastapi import FastAPI,HTTPException,Header,Request
from linebot.v3.messaging import Configuration
from linebot.exceptions import InvalidSignatureError
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
    try:
        handler.handle(body,x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=404, detail='InvalidSignatureError')
    return 'np'

@handler.add(MessageEvent)
def handle_message(event):
    if event.type != "text":
        return
    
    LineBotApi.reply_message(
        reply_token=event.reply_token,
        messages=TextMessage(text=event.message.text)
    )


