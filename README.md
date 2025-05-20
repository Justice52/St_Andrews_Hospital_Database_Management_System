# 🏥 Hospital Appointment System

A web-based hospital appointment management system built with Django. The application allows doctors and patients to register, book appointments, 
track prescriptions, and view medical history. Admin users can manage doctors, patients, and appointment records via a secure dashboard.

## 🚀 Features

- 👨‍⚕️ Doctor Registration and Management
- 🧑‍🤝‍🧑 Patient Registration and Management
- 📅 Appointment Booking System
- 💊 Prescription Management
- 📖 Medical History Tracking
- 🔐 Admin Panel for User and Appointment Management

## 🛠️ Tech Stack

- Backend: Django (Python)
- Database: SQLite (default, can be switched to PostgreSQL/MySQL)
- Frontend: HTML5, CSS3, Bootstrap 
- Authentication: Django’s built-in user model (customized for role-based access)


## 📸 Screenshots

![{02187758-6DCE-4AF3-934C-73915A4525D2}](https://github.com/user-attachments/assets/fff5b6c8-cb82-4345-95db-2ccbdad33f5e)
![{85EAC0D7-87EE-4591-985F-0248E841086D}](https://github.com/user-attachments/assets/35653c19-1e03-4cfc-b881-cd3cb2f4a2c4)
![{1E8F9E05-6984-4E4D-8E3D-7658B2FC564E}](https://github.com/user-attachments/assets/fc68a28b-fc79-44e7-9908-09c6c0ea3be3)
![{70A03102-9383-4553-9AF0-2CAF51F6C5FF}](https://github.com/user-attachments/assets/24073db2-7c2d-438e-96d9-ccab85196605)





## 📂 Project Structure
St_Andrews_Hospital_Database_Management_System/
- ├── assets/admin/ # Admin-related assets (CSS, JS, images)
- ├── djangoProject/ # Main Django project configuration
- ├── final/ # Main application logic (views, models, forms)
- ├── static/ # Static files
- ├── templates/ # HTML templates for all roles
- ├── db.sqlite3 # Default development database
- └── manage.py # Django management script


## 💻 Technologies Used

- Framework: Django (Python)
- Database: SQLite (can be upgraded to PostgreSQL/MySQL)
- Frontend: HTML5, CSS3, SCSS, JavaScript
- Styling: Bootstrap + Custom CSS/SCSS

## 🚀 Getting Started

1. 📥 Clone the repository:

```bash
git clone https://github.com/Justice52/St_Andrews_Hospital_Database_Management_System.git
cd St_Andrews_Hospital_Database_Management_System
```

2. 🐍 Create and activate a virtual environment:
```
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

3. 📦 Install required packages:
```
   pip install -r requirements.txt  # Create this file if not already present
```
4. 🔃 Run migrations:
   ```
   python manage.py migrate
   
6. 👤 Create a superuser:
   ```
   python manage.py createsuperuser

8. ▶️ Start the development server:
   ```
   python manage.py runserver

10. 🌐 Open in browser:
Visit
```
 http://127.0.0.1:8000/
```
🔐 Roles & Access
👨‍⚕️ Doctor: Manage appointments, view/add prescriptions

👨‍👩‍⚕️ Patient: Register, book appointments, view medical records

🛠️ Admin: Oversee doctors, patients, and system activity

📌 Notes
You can customize settings like database or add REST API support via Django REST Framework.


📃 License
This project is open source and available under the MIT License.

🙋‍♂️ Author
Created by Justice Ayamdoo
Email: justice2022aya@gmail.com


