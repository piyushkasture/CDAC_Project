This project is a UI automation testing framework built using Playwright with Python for evaluating the OrangeHRM Open Source Demo Application.

---
### Prerequisites

- **Python 3.10+**
- pip

### Setup (Windows)

1. Create and activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```
---

## Project Structure

- `pages/` — Page Objects (e.g., `LoginPage.py`, `AdmminPage.py`)
- `tests/` — Test suites organized by feature
- `testData/` — Test data files (`*.json`)
- `utils/` — Helpers (`DriverManager.py`, `DataReader.py`, `CustomLogger.py`)
- `config/environments/` — Environment configuration (e.g., `dev.yaml`)
- `reports/` — Generated HTML and Allure reports
- `main_runner.py` — Convenience script to run a set of end-to-end tests

---

## Running Tests

- Run the full test suite using pytest:

```bash
pytest
```

- Run a single test file or directory:

```bash
pytest tests/authentication/test_login.py -q
pytest tests/end_to_end/ -q
```

- Run the predefined main runner script:

```bash
python main_runner.py
```

---

## Reports & Results

- HTML report: `reports/assignment.html`
- Allure raw results: `reports/allure-results`

```bash
# Generate static report
allure generate reports/allure-results -o reports/allure-report --clean
# Serve the report locally
allure open reports/allure-report
# or
allure serve reports/allure-results
```


