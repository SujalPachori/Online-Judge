# CodeShrine - Online Judge Platform

CodeShrine is a Django-based online judge platform designed to support competitive programming and coding practice. It offers features such as user authentication, problem listings, code submission, real-time execution, and submission history tracking within a modern, dark-themed user interface.

---

## Features

- User registration and login (including Firebase Google OAuth integration)
- Problem list and detailed problem view pages
- Code editor with support for multiple programming languages (C++, Python, Java)
- Execution of custom test cases
- Submission system with verdicts and result tracking
- Submission history with the ability to view submitted code
- User profile management

---

## Technology Stack

- **Backend:** Django
- **Frontend:** HTML, Tailwind CSS, Bootstrap (dark mode)
- **Authentication:** Django authentication system and Firebase Google OAuth
- **Code Execution:** Docker for secure, isolated code execution environments
- **Database:** SQLite (development) / PostgreSQL (recommended for production)

---

## Folder Structure
Online_Judge/
├── home/ # Main application with views, models, and templates
├── online_judge/ # Project configuration and settings
├── templates/ # Shared templates
├── static/ # Static files
├── DockerFile # Containerization configuration
├── requirements.txt # Python dependencies
└── manage.py # Django management script

yaml
Copy
Edit

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/SujalPachori/Online-Judge.git
   cd Online-Judge
Create and activate a virtual environment

bash
Copy
Edit
python -m venv myenv
myenv\Scripts\activate  # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations

bash
Copy
Edit
python manage.py migrate
Run the development server

bash
Copy
Edit
python manage.py runserver
Contribution Guidelines
Contributions are welcome. If you would like to contribute, please fork the repository and submit a pull request. For significant changes, open an issue to discuss your ideas first.

License
This project is licensed under the MIT License. See the LICENSE file for more information.


