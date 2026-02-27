FROM python:3.11.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p inbox processed failed tools schemas

# Environment variables
ENV JWT_SECRET="super-secret-mcp-key"
ENV PORT=8080

EXPOSE 8080

CMD ["uvicorn", "factory_worker:app", "--host", "0.0.0.0", "--port", "8080"]
