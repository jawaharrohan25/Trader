# Trading Strategy

A Python trading strategy application built with Streamlit for analyzing NIFTY options strategies.

## Setup

### Prerequisites
- Python 3.8+

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

```bash
streamlit run nifty_strategy_app.py
```

## Project Structure

```
Trading_strategy/
├── src/                       # Source code
│   ├── __init__.py
│   └── main.py
├── nifty_strategy_app.py      # Main Streamlit application
├── requirements.txt           # Project dependencies
├── README.md                  # This file
└── .gitignore                 # Git ignore patterns
```

## Development

### Adding Dependencies

Add packages to `requirements.txt` and run:
```bash
pip install -r requirements.txt
```

### Code Style

Follow PEP 8 conventions for Python code.

## License

This project is licensed under the MIT License.
