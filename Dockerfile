FROM python:3.9.1
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]