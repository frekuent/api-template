# API Template Project

This project is a template for creating FastAPI services using Django ORM, Docker, and Kubernetes.

## Project Structure

```markdown
api-template/
├── app/
├── core/
├── envs/
├── requirements/
├── tests/
└── k8s/
```

## Environments

This template includes configurations for different environments: `local`, `development`, `staging`, and `production`.

## Quick Start

### 1. Clone the repository

```bash
git clone <repo-url>
cd api-template
```

### 2. Set up Environment Variables

Copy the `.env.example` file to configure environment variables for each environment.

```bash
cp envs/.env.example envs/.env.local
```

Edit `envs/.env.local` with your local configuration values as needed.

## Running the Project
### Option 1: Run Locally with Uvicorn
**Step 1: Install Dependencies**
Make sure you are in a virtual environment, then install dependencies:
```bash
pip install -r requirements/local.txt
```

**Step 2: Activate Pre-commit Hooks**
Set up pre-commit hooks to automatically check code quality before each commit:
```bash
pre-commit install --hook-type pre-commit --hook-type pre-push
```

**Step 3: Start the Project with Uvicorn**
Run the project using Uvicorn:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --env-file ./envs/.env.local
```
The API should now be accessible at http://127.0.0.1:8000.

### Option 2: Run with Docker
To run the project in a Docker container with the local environment settings:
**Step 1: Build the Docker Image**
```bash
docker build -t api-template --build-arg ENV=local .
```
**Step 2: Run the Docker Container**
```bash
docker run -d -p 8000:8000 --env-file ./envs/.env.local api-template
```
The API should now be accessible at http://127.0.0.1:8000.

### Running Tests
Run tests with:
```bash
pytest
```

## Pre-commit Hooks

This project uses **pre-commit** to run checks and format code automatically before commits. Pre-commit hooks help
ensure code quality and consistency across the team.

### 1. Set Up Pre-commit Hooks

Once pre-commit is installed, run the following command to install the hooks specified in .pre-commit-config.yaml:

```bash
pre-commit install --hook-type pre-commit --hook-type pre-push
```

This will set up pre-commit to run automatically on git commit.

### 2. Run Pre-commit Hooks Manually

You can also run the hooks manually on all files with:

```bash
pre-commit run --all-files
```

## Code Formatting and Linting

This project uses **Ruff** for linting, **Black** for code formatting, and **DJLint** for linting Django templates.
Below are instructions for running these tools manually.

### 1. **Ruff** - Python Linting

[Ruff](https://github.com/charliermarsh/ruff) is used for fast Python linting.

Run Ruff on the entire codebase:

```bash
ruff .
```

Run Ruff on specific files or directories:

```bash
ruff path/to/file_or_directory.py
```

### 2. Black - Code Formatting

Black is a code formatter for Python.

Run Black on the entire codebase:

```bash
black .
```

Run Black on specific files or directories:

```bash
black path/to/file_or_directory.py
```
