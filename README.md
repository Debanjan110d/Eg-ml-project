# Student Dropout Prediction System

A Django-based web application for predicting student dropout likelihood based on academic performance metrics.

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Setup Instructions

1. Clone the repository or download the files:
```bash
git clone <repository-url>
cd sponnasi
```

2. Create a virtual environment:
```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

5. Navigate to the Django project directory:
```bash
cd student_dropout
```

6. Run database migrations:
```bash
python manage.py migrate
```

7. Start the development server:
```bash
python manage.py runserver
```

8. Open your web browser and go to:
```
http://127.0.0.1:8000/
```

## Usage

1. Enter the following student information:
   - JEE Main Score
   - Attendance Percentage
   - CGPA

2. Click "Predict" to see the dropout prediction result

## Project Structure

```
student_dropout/
├── predictor/              # Main application
│   ├── templates/         # HTML templates
│   ├── django_predictor.py # Prediction logic
│   ├── urls.py           # URL configurations
│   └── views.py          # View functions
├── student_dropout/       # Project settings
└── manage.py             # Django management script
```

## Troubleshooting

1. If you get a "No module named 'django'" error:
   - Make sure your virtual environment is activated
   - Run `pip install django`

2. If the server won't start:
   - Check if port 8000 is already in use
   - Try `python manage.py runserver 8080` to use a different port

3. If you see database errors:
   - Delete db.sqlite3 file (if it exists)
   - Run migrations again: `python manage.py migrate`

## Development

To modify the prediction thresholds, edit the `thresholds` dictionary in:
`predictor/django_predictor.py`

## License

This project is open-source and available under the MIT License.
