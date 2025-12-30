FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY app ./app

# Expose port
EXPOSE 5000

# Run with gunicorn (production-like)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.app:app"]
