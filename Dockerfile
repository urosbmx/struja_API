FROM python:3.11-slim
LABEL authors="uroskatanic"

WORKDIR /app

COPY . /app

# Install dependencies, allowing system-wide package installation
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Command to run the Python file
CMD ["uvicorn", "main:app", "--reload"]