<img width="1321" height="297" alt="Group 12" src="https://github.com/user-attachments/assets/04d61f43-c7ab-48af-9cd0-e6d4c504db87" />

This pet project was created to refresh my Python knowledge after finishing my first year at university 😅

---

> [!NOTE]
> Python Assistant CLI is a console application that helps with everyday tasks directly from the terminal
> The project includes weather checking, task management, and currency conversion using external APIs and a colorful terminal interface powered by Rich

## Technology Stack:

* Python - main programming language for building the CLI application
* Rich - beautiful terminal UI with tables, panels, colors, and prompts
* Requests - HTTP requests for working with external APIs
* python-dotenv - environment variable management using `.env`
* OpenWeather API - weather data by city
* Frankfurter API - currency exchange rates
* OOP - class-based architecture for API clients and task management

## Key Features:

* Weather search by city using OpenWeather API
* Currency converter using real exchange rates
* Task manager with add, find, show, and delete functionality
* Hashtag system for task categories and priorities
* Rich-based colorful terminal interface
* ASCII logo and main menu
* API client architecture with a base parent class
* Error handling for invalid input, API errors, and missing environment variables

## Getting Started:

### 1. Clone the repository

```bash
git clone https://github.com/Marchello-Projects/Python_Assistant_CLI

cd Python_Assistant_CLI
```

### 2. Create and activate virtual environment

For Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows PowerShell:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory with the following content:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
```

> [!NOTE]
> You need an OpenWeather API key for the weather feature

### 5. Run the application

For Linux / macOS:

```bash
python3 main.py
```

For Windows:

```bash
python main.py
```
