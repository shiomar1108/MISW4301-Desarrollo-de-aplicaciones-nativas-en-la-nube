FROM python:3.10
LABEL author="h.galindos@uniandes.edu.co"
RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip
RUN pip install pipenv
WORKDIR /backend
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --system --deploy --ignore-pipfile
COPY . .
EXPOSE 5000