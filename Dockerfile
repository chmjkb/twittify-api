# newest python slim image
FROM python:3.10-slim

# dir containing our api
WORKDIR /twitter-api

# copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy all the other files
COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
