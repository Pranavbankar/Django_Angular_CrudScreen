## How to Run Your Django + Angular Project

## 1. Backend (Django)


cd backend
CREATE TABLE students_student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    city VARCHAR(100),
    address TEXT,
    dob DATE,
    is_active BOOLEAN
);

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Backend will run at: http://127.0.0.1:8000/app/student

## 2. Frontend (Angular)
cd frontend
npm install
ng serve -o


   
   
