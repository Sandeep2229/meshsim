# 🧱 MeshSim: AI-Powered Geometry Upload & Mesh API (FastAPI + Docker)

MeshSim is a backend system built with **FastAPI**, designed for secure uploading and lightweight processing of geometry files (e.g., `.msh`, `.geo`). It includes token-based authentication, Dockerized deployment, and structured API endpoints — laying the foundation for future AI-powered meshing workflows.

## 🚀 Features

- ✅ Token-based user authentication via `/login`
- ✅ Auth-protected file upload at `/upload-geometry`
- ✅ Reads, saves, and processes uploaded geometry files
- ✅ Returns simulated mesh output
- ✅ Built with **FastAPI**, **OAuth2**, **Docker**, and **Python**
- ✅ Health check endpoint at `/health`
- 🐳 Fully containerized using Docker

## 📦 Tech Stack

- **Backend**: FastAPI, Pydantic
- **Security**: OAuth2PasswordBearer (JWT)
- **Auth**: Password-based with hashed credentials
- **Mesh Utility**: Custom logic in `mesh_utils.py` (dummy for now)
- **Containerization**: Docker
- **Optional**: PostgreSQL, Celery (planned features)

## 📂 Project Structure

```
meshsim/
│
├── app/
│   ├── main.py         # FastAPI app and endpoints
│   ├── auth.py         # Auth logic (login, token)
│   ├── mesh_utils.py   # Placeholder mesh generator
│
├── uploads/            # Saved uploaded geometry files
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🔐 Authentication Flow

1. POST to `/login` with form:
   ```json
   {
     "username": "sandeep",
     "password": "password123"
   }
   ```
   Receive:
   ```json
   {
     "access_token": "xxx.yyy.zzz",
     "token_type": "bearer"
   }
   ```
2. Use token in `/docs` or headers:
   ```
   Authorization: Bearer <access_token>
   ```

## 📤 Upload Geometry

**Endpoint**: `POST /upload-geometry`

- **Headers**: Bearer token required
- **Payload**: File upload (e.g., `.geo`, `.txt`)
- **Response**:
  ```json
  {
    "user": "sandeep",
    "filename": "example.geo",
    "saved_path": "uploads/example.geo",
    "mesh": { ... }
  }
  ```

## ✅ Health Check

Visit: `GET http://localhost:8000/health`

**Response**:
```json
{"status": "ok"}
```

## 🐳 Docker Deployment

### 🛠️ Build the container
```bash
docker build -t meshsim-app .
```

### ▶️ Run it
```bash
docker run -d -p 8000:8000 --name meshsim meshsim-app
```

### 🌐 Open
Navigate to: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🔮 Future Ideas

- AI-powered mesh quality scoring
- PostgreSQL storage for uploaded jobs
- CI/CD with GitHub Actions
- FastAPI BackgroundTasks or Celery queue

## 📜 License

MIT License © 2025 Sai Sandeep Mamidala

Feel free to fork, clone, and build on it!
