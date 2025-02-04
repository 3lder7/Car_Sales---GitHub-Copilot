# Brazilian Party Snacks Project

This project is designed to showcase and sell Brazilian party snacks through a web application. It consists of a backend implemented in Python using Flask and a frontend built with HTML, CSS, and JavaScript.

## Project Structure

```
brazilian-party-snacks
├── backend
│   ├── app.py                # Main entry point for the Flask application
│   ├── requirements.txt      # Dependencies for the backend
│   └── tests
│       └── test_app.py      # Unit tests for the Flask application
├── frontend
│   ├── css
│   │   └── styles.css        # CSS styles for the frontend
│   ├── js
│   │   └── scripts.js        # JavaScript for interactivity
│   ├── index.html            # Main HTML file for the frontend
│   └── tests
│       └── test_scripts.js   # Unit tests for the JavaScript code
├── README.md                 # Project documentation
└── .gitignore                # Files and directories to ignore in version control
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd brazilian-party-snacks
   ```

2. **Set up the backend:**
   - Navigate to the `backend` directory.
   - Create a virtual environment (optional but recommended):
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```

3. **Run the Flask application:**
   ```
   python app.py
   ```

4. **Set up the frontend:**
   - Open `index.html` in a web browser to view the application.

## Usage

- The web application allows users to browse and purchase various Brazilian party snacks.
- Users can interact with the page using the provided JavaScript functionalities.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.