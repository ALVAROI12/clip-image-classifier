FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend app code
COPY backend/ .

# Expose port required by Cloud Run
EXPOSE 8080

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]
