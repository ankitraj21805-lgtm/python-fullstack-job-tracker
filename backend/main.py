from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from backend.database import get_connection, initialize_database, rows_to_dicts

app = FastAPI(
    title="Python Full Stack Job Tracker API",
    description="FastAPI backend for tracking job applications with SQLite.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ApplicationBase(BaseModel):
    company: str = Field(..., min_length=2, max_length=80)
    role: str = Field(..., min_length=2, max_length=100)
    status: str = Field(..., min_length=2, max_length=40)
    source: str = Field(..., min_length=2, max_length=80)
    notes: str = Field(default="", max_length=500)

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: int
    created_at: str

initialize_database()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_frontend() -> FileResponse:
    return FileResponse("frontend/index.html")

@app.get("/api/health")
def health_check() -> dict:
    return {"status": "ok", "message": "Python FastAPI backend is running"}

@app.get("/api/applications", response_model=List[Application])
def get_applications() -> list:
    with get_connection() as connection:
        rows = connection.execute("SELECT * FROM applications ORDER BY created_at DESC").fetchall()
    return rows_to_dicts(rows)

@app.post("/api/applications", response_model=Application, status_code=201)
def create_application(application: ApplicationCreate) -> dict:
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO applications (company, role, status, source, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (application.company, application.role, application.status, application.source, application.notes),
        )
        new_id = cursor.lastrowid
        row = connection.execute("SELECT * FROM applications WHERE id = ?", (new_id,)).fetchone()
    return dict(row)

@app.put("/api/applications/{application_id}", response_model=Application)
def update_application(application_id: int, application: ApplicationUpdate) -> dict:
    with get_connection() as connection:
        existing = connection.execute("SELECT * FROM applications WHERE id = ?", (application_id,)).fetchone()
        if existing is None:
            raise HTTPException(status_code=404, detail="Application not found")
        connection.execute(
            """
            UPDATE applications
            SET company = ?, role = ?, status = ?, source = ?, notes = ?
            WHERE id = ?
            """,
            (application.company, application.role, application.status, application.source, application.notes, application_id),
        )
        row = connection.execute("SELECT * FROM applications WHERE id = ?", (application_id,)).fetchone()
    return dict(row)

@app.delete("/api/applications/{application_id}")
def delete_application(application_id: int) -> dict:
    with get_connection() as connection:
        existing = connection.execute("SELECT * FROM applications WHERE id = ?", (application_id,)).fetchone()
        if existing is None:
            raise HTTPException(status_code=404, detail="Application not found")
        connection.execute("DELETE FROM applications WHERE id = ?", (application_id,))
    return {"message": "Application deleted successfully"}

@app.get("/api/stats")
def get_stats() -> dict:
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT status, COUNT(*) AS count
            FROM applications
            GROUP BY status
            """
        ).fetchall()
        total = connection.execute("SELECT COUNT(*) AS count FROM applications").fetchone()["count"]
    status_counts = {row["status"]: row["count"] for row in rows}
    return {
        "total": total,
        "applied": status_counts.get("Applied", 0),
        "interview": status_counts.get("Interview", 0),
        "saved": status_counts.get("Saved", 0),
        "rejected": status_counts.get("Rejected", 0),
        "offer": status_counts.get("Offer", 0),
    }
