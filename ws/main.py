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
    "Thank you, but I'm not interested.",
    "I'm flattered, but I must decline.",
    "I'll have to say no for now.",
    "Why must I?",
    "No thank you.",
    "I respectfully decline."
]

greetings = [
    "Hi",
    "hi",
    "Hello",
    "hello",
    "hey",
    "Hey"
]



@app.websocket("/ws")
async def websocker_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if data in greetings:
            await websocket.send_text("Hello there! How can I assist you today?")
        elif "why" in data:
            await websocket.send_text("Brother stop asking why and all")
        else:
            random_text_output_index = numpy.random.randint(0, len(all_denials))
            await websocket.send_text(all_denials[random_text_output_index])