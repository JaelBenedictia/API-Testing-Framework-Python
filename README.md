# API Testing Framework (Python)

This project is a REST API automation framework built using Python, Requests, and Pytest.

## Features
- Automated CRUD operations (GET, POST, PUT, DELETE)
- Status code validation
- JSON response validation
- Reusable API client
- Config-based base URL handling
- HTML test report generation

## Tech Stack
- Python
- Requests
- Pytest
- Pytest-HTML

## How to Run
pip install -r requirements.txt  
pytest --html=reports/report.html

## Project Structure
tests/ → Test cases  
utils/ → Config & reusable API client  
reports/ → Test execution reports  

## Author
Jael Benedictia
