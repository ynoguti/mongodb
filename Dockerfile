FROM python:3.9

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
#COPY main.py .
#CMD ["python", "main.py"]