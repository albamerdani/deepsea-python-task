# Pull base image
FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

# Install dependencies
RUN pip install -r /requirements.txt

EXPOSE 5000
CMD ["python", "app/main.py"]