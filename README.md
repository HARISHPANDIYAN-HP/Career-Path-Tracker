# Career Path Tracker

A simple web application to help users track their education and career paths. Users can set learning goals, track progress through milestones, upload certificates, and get personalized career suggestions based on their completed goals.

## Features

- Set and track learning goals
- Update progress on goals
- Add certificates and achievements
- Get career suggestions based on completed goals
- Clean and responsive UI for both desktop and mobile
- Local data storage using SQLite

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Database: SQLite
- ORM: SQLAlchemy

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd career-path-tracker
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
career-path-tracker/
├── app.py              # Main Flask application
├── models.py           # Database models
├── requirements.txt    # Python dependencies
├── static/
│   └── css/
│       └── style.css  # Stylesheet
└── templates/
    └── index.html     # Main HTML template
```

## Usage

1. **Adding Goals**
   - Click on the "Add Goal" section
   - Fill in the goal title, description, and category
   - Click "Add Goal" to save

2. **Tracking Progress**
   - Use the progress slider on each goal card
   - Click "Update Progress" to save changes

3. **Adding Certificates**
   - Navigate to the Certificates section
   - Fill in certificate details
   - Click "Add Certificate" to save

4. **Career Suggestions**
   - Automatically generated based on completed goals
   - Updates when goals are marked as complete

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.