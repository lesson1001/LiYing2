
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from liying.pipeline import process_one
from io import BytesIO

app = FastAPI()

@app.post("/process")
async def process(image: UploadFile = File(...)):
    img = await image.read()
    result = process_one(BytesIO(img), bg_color="white", size="1inch")
    return StreamingResponse(BytesIO(result), media_type="image/jpeg")
