FROM python:3.10
ENV DB_USER postgres
ENV DB_PASSWORD postgres
ENV DB_HOST host.docker.internal
ENV DB_PORT 5432
ENV DB_NAME db_post
ENV USERS_PATH http://mcs_users:5000
WORKDIR /post
COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --dev
EXPOSE 5000
CMD ["python", "src/main.py"]

