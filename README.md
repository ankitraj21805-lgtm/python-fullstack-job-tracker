# Python Full Stack Job Tracker

A beginner-friendly full-stack project with a **Python FastAPI backend**, **SQLite database**, and **HTML/CSS/JavaScript frontend**.

This project helps track job applications, statuses, companies, roles, notes, and recruiter follow-ups. It is built as a recruiter-friendly GitHub project to demonstrate backend APIs, database CRUD, frontend integration, and clean project structure.

## 🚀 Live Demo

🔗 [View Live App](https://python-fullstack-job-tracker.onrender.com)



## 📌 Why This Project Matters

This project is useful for students and job seekers who want to manage applications in one dashboard.

It demonstrates:

- Python backend development
- REST API creation
- SQLite database integration
- CRUD operations
- Frontend and backend connection
- Clean UI dashboard
- Real-world full-stack workflow

## ✨ Features

- Add new job applications
- View all applications
- Search by company, role, status, or notes
- Filter by application status
- Update application status
- Delete applications
- Dashboard statistics
- SQLite database storage
- FastAPI interactive API docs
- Responsive frontend UI

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- SQLite
- Uvicorn

### Frontend
- HTML5
- CSS3
- JavaScript

### Tools
- Git
- GitHub
- VS Code

## 📂 Folder Structure

```txt
python-fullstack-job-tracker/
│
├── backend/
│   ├── database.py
│   └── main.py
│
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── styles.css
│
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-fullstack-job-tracker.git
cd python-fullstack-job-tracker
```

### 2. Create virtual environment

Windows:

```bash
python -m venv venv
venv\\Scripts\\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run Locally

```bash
uvicorn backend.main:app --reload
```

Open in browser:

```txt
http://127.0.0.1:8000
```

API docs:

```txt
http://127.0.0.1:8000/docs
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Check server health |
| GET | `/api/applications` | Get all applications |
| POST | `/api/applications` | Add a new application |
| PUT | `/api/applications/{id}` | Update an application |
| DELETE | `/api/applications/{id}` | Delete an application |
| GET | `/api/stats` | Get dashboard statistics |

## 🧪 Example JSON

```json
{
  "company": "Deloitte",
  "role": "Frontend Developer",
  "status": "Applied",
  "source": "LinkedIn",
  "notes": "Applied for junior frontend role"
}
```

## 🧠 What I Learned

- Building REST APIs using FastAPI
- Connecting frontend JavaScript to backend APIs
- Performing CRUD operations with SQLite
- Creating a responsive dashboard UI
- Structuring a full-stack Python project
- Writing recruiter-friendly project documentation

## 🔮 Future Improvements

- Add login authentication
- Add resume upload field
- Add job priority score
- Add CSV export
- Add charts
- Add email reminder automation
- Deploy backend on Render
- Add GitHub Actions build check

## 👨‍💻 Author

**Ankit Sharma**  
Frontend Developer | Junior Full Stack Developer | AI Automation Enthusiast

- GitHub: [ankitraj21805-lgtm](https://github.com/ankitraj21805-lgtm)
- Email: [ankitraj21805@gmail.com](mailto:ankitraj21805@gmail.com)

## 📄 License

This project is open source and available under the MIT License.
