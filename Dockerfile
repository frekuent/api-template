# Use Python 3.12
FROM python:3.12

# Set the working directory
WORKDIR /app

# Set environment argument to specify requirements file
ARG ENV=local

# Copy only the requirements files and install dependencies
COPY ./requirements /app/requirements
RUN pip install --no-cache-dir -r /app/requirements/${ENV}.txt

# Copy the entire project
COPY . /app

# Set environment variable for Django settings
ENV ENV=${ENV}

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
