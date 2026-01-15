from fastapi import FastAPI, WebSocket
import numpy

app = FastAPI()

#IMPORTANT DENIAL
all_denials = [
    "Unfortunately, I have to say no.",
    "I'm unable to help with that.",
    "That won't work for me.",
    "I need to decline.",
    "Not this time, sorry.",
    "I appreciate you asking, but I can't.",
    "I'm honoured you asked, but no.",
    "I'm going to have to decline.",
    "I won't be able to participate.",
    "Thank you, but I'm not interested.",
    "I'm flattered, but I must decline.",
    "I'll have to say no for now.",
    "Why must I?",
    "No thank you.",
    "I respectfully decline."
]

@app.websocket("/ws")
async def websocker_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        random_text_output_index = numpy.random.randint(0, len(all_denials))
        await websocket.send_text(all_denials[random_text_output_index])