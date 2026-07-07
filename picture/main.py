from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException, UploadFile, File
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }


@app.get("/")
def home():
    return {
        "message": "homepage to make uploading picture"
    }


@app.get("/photo/{filename}")
async def get_photo(filename: str):

    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException( 
            status_code=404,
            detail="Photo not found"
        )

    return FileResponse(file_path)

