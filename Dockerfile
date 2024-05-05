FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code
COPY ./app /app

# Copy the Hugging Face model files
COPY ./model /model

# Expose port
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]