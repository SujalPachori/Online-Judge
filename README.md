# CodeShrine - Online Judge Platform

<div align="center">

[![Django](https://img.shields.io/badge/Django-5.2.1-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)

**Your shrine to practice, compete, and grow as a coder.**

[Visit Live Site](http://www.codeshrine.xyz) • [Report Bug](https://github.com/SujalPachori/Online-Judge/issues) • [Request Feature](https://github.com/SujalPachori/Online-Judge/issues)

</div>

---

## Overview

CodeShrine is a modern online judge platform built with Django that provides a competitive programming environment for coders to practice, compete, and improve their skills. With support for multiple programming languages, real-time code execution, and AI-powered hints, CodeShrine offers an engaging learning experience.

### Key Features

- **User Authentication** - Secure registration and login system
- **Problem Management** - Browse, search, and solve coding problems with varying difficulty levels
- **Multi-Language Support** - Write code in C, C++, Python, and Java
- **Real-Time Execution** - Instant code compilation and execution with Docker isolation
- **Custom Test Cases** - Test your code against custom inputs before submission
- **AI-Powered Hints** - Get intelligent code suggestions using Google Gemini AI
- **Submission History** - Track all your submissions with detailed verdicts (AC, WA, TLE, RE, CE)
- **User Profiles** - Personalized profiles with submission statistics and achievements
- **Modern UI** - Dark-themed, responsive interface built with Bootstrap
- **Responsive Design** - Works seamlessly across desktop and mobile devices

---

## Live Demo

Visit the application: **[http://www.codeshrine.xyz](http://www.codeshrine.xyz)**

---

## Technology Stack

<table>
<tr>
<td>

**Backend**
- Django 5.2.1
- Python 3.11
- Gunicorn (WSGI Server)
- SQLite (Development)

</td>
<td>

**Frontend**
- HTML5 & CSS3
- Bootstrap 4.5
- JavaScript
- Dark Theme UI

</td>
</tr>
<tr>
<td>

**Code Execution**
- Docker Containers
- Subprocess Management
- Time & Memory Limits
- Secure Sandboxing

</td>
<td>

**AI Integration**
- Google Gemini API
- Code Analysis
- Intelligent Hints
- Error Detection

</td>
</tr>
<tr>
<td>

**Deployment**
- Docker
- AWS EC2
- Nginx
- Docker Hub

</td>
<td>

**Development**
- Git & GitHub
- VS Code
- Virtual Environment
- Docker Desktop

</td>
</tr>
</table>

---

## Project Structure

```
Online_Judge/
├── home/                       # Main application
│   ├── models.py              # Database models (Problem, Submission, Profile)
│   ├── views.py               # Business logic and request handling
│   ├── forms.py               # Form definitions
│   ├── templates/             # HTML templates
│   └── static/                # CSS, JS, images
├── online_judge/              # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   └── wsgi.py                # WSGI configuration
├── codes/                     # Temporary code files
├── inputs/                    # Test case inputs
├── outputs/                   # Execution outputs
├── media/                     # User uploads (profile pictures)
├── staticfiles/               # Collected static files
├── Dockerfile                 # Docker container configuration
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
├── manage.py                  # Django CLI
└── README.md                  # This file
```

---

## Setup & Installation

### Prerequisites

- Python 3.11+
- Docker Desktop (for code execution)
- Git
- Google Gemini API Key ([Get one here](https://aistudio.google.com/app/apikey))

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/SujalPachori/Online-Judge.git
   cd Online-Judge
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv myenv
   myenv\Scripts\activate

   # Linux/MacOS
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file in project root
   echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Frontend: http://127.0.0.1:8000
   - Admin Panel: http://127.0.0.1:8000/admin

---

## Docker Deployment

### Build and Run Locally

```bash
# Build Docker image
docker build -t codeshrine .

# Run container
docker run -d -p 8000:8000 \
  -e GEMINI_API_KEY="your_api_key_here" \
  --name codeshrine-app \
  codeshrine
```

### Deploy to Production (AWS EC2)

1. **Build and push to Docker Hub**
   ```bash
   docker build -t your-username/codeshrine:latest .
   docker push your-username/codeshrine:latest
   ```

2. **On EC2 instance**
   ```bash
   # Pull image
   docker pull your-username/codeshrine:latest

   # Create directories
   mkdir -p ~/codes ~/inputs ~/outputs ~/media

   # Run container
   docker run -d \
     --name codeshrine-app \
     -p 8000:8000 \
     -e GEMINI_API_KEY="your_api_key" \
     --restart unless-stopped \
     -v ~/codes:/app/codes \
     -v ~/inputs:/app/inputs \
     -v ~/outputs:/app/outputs \
     -v ~/media:/app/media \
     your-username/codeshrine:latest
   ```

3. **Configure Nginx**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location /static/ {
           proxy_pass http://127.0.0.1:8000/static/;
       }

       location /media/ {
           proxy_pass http://127.0.0.1:8000/media/;
       }
   }
   ```

---

## Usage Guide

### For Users

1. **Register/Login** - Create an account or login to access features
2. **Browse Problems** - View available coding problems sorted by difficulty
3. **Solve Problems** - Write code in your preferred language (C, C++, Python, Java)
4. **Test Code** - Run custom test cases before final submission
5. **Get AI Hints** - Click "Get Hint" for intelligent suggestions from Gemini AI
6. **Submit Solution** - Submit your code for evaluation against hidden test cases
7. **View Results** - Check submission status (AC, WA, TLE, RE, CE)
8. **Track Progress** - View your submission history and statistics

### For Admins

1. Access admin panel at `/admin`
2. Add new problems with test cases
3. Manage users and submissions
4. Configure problem difficulty and tags
5. Monitor system performance

---

## Supported Languages & Compilers

| Language | Compiler/Interpreter | Version |
|----------|---------------------|---------|
| C        | GCC                 | Latest  |
| C++      | G++                 | Latest  |
| Python   | Python3             | 3.11+   |
| Java     | OpenJDK             | 11+     |

---

## Security Features

- **CSRF Protection** - Django built-in CSRF middleware
- **Password Hashing** - Secure password storage with Django's authentication
- **Docker Isolation** - Code execution in isolated containers
- **Execution Limits** - Time and memory constraints prevent abuse
- **Input Validation** - All user inputs are sanitized
- **API Key Security** - Environment-based configuration

---

## Contributing

Contributions are always welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly

---

## Known Issues & Limitations

- Code execution requires Docker to be running
- Large file uploads may timeout (configured limit: 100MB)
- AI hints require valid Gemini API key with quota
- SQLite not recommended for production (use PostgreSQL)

---

## Changelog

### Version 1.0.0 (Current)
- Initial release with core features
- Gemini AI integration for code hints
- Docker-based deployment
- Dark-themed responsive UI
- Submission tracking and history

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**Sujal Pachori**

- GitHub: [@SujalPachori](https://github.com/SujalPachori)
- Project: [Online-Judge](https://github.com/SujalPachori/Online-Judge)
- Website: [http://www.codeshrine.xyz](http://www.codeshrine.xyz)

---

## Acknowledgments

- Django framework and community
- Google Gemini AI for intelligent code analysis
- Bootstrap for UI components
- Docker for containerization
- AWS for hosting infrastructure

---

## Support

If you have any questions or need help, please:

1. Check the [Issues](https://github.com/SujalPachori/Online-Judge/issues) page
2. Open a new issue with detailed description
3. Contact via GitHub

---

<div align="center">

**Star this repository if you find it helpful!**

Made with ❤️ by [Sujal Pachori](https://github.com/SujalPachori)

</div>


