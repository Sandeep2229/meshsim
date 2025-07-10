# app/main.py
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import authenticate_user, create_access_token, get_current_user
from app import mesh_utils
import os

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

app = FastAPI()



@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Invalid credentials")

        access_token = create_access_token(data={"sub": user["username"]})
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        print("❌ Login Error:", e)
        raise HTTPException(status_code=500, detail="Internal login error")


@app.get("/")
def read_root():
    return {"message": "Welcome to MeshSim API"}

@app.post("/upload-geometry")
async def upload_geometry(
    file: UploadFile = File(...),
    current_user: str = Depends(get_current_user)
):
    try:
        # Step 1: Read file content
        content = await file.read()
        text_data = content.decode("utf-8")
        print("📄 Uploaded File Content:")
        print(text_data)

        # Step 2: Save file locally
        save_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(save_path, "wb") as f:
            f.write(content)
        print(f"✅ File saved to {save_path}")

        # Step 3: Generate mesh (optional)
        result = mesh_utils.generate_mesh(text_data)

        # Step 4: Return response
        return {
            "user": current_user,
            "filename": file.filename,
            "saved_path": save_path,
            "mesh": result
        }

    except Exception as e:
        print("❌ Internal Server Error:", e)
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/health")
def health_check():
    return {"status": "ok"}
