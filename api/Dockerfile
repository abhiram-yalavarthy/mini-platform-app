FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create non-root user
RUN useradd -m appuser

WORKDIR /app
COPY api/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY api /app/api

USER appuser
EXPOSE 8080

CMD ["python", "-m", "uvicorn", "api.src.main:app", "--host", "0.0.0.0", "--port", "8080"]
