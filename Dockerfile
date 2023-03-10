FROM python:3.9

RUN mkdir app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./iris_clf.joblib /app/iris_clf.joblib
COPY ./iris_app.py /app/iris_app.py

EXPOSE 5000

CMD [ "python", "/app/iris_app.py"]