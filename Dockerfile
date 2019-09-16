FROM python:3

ADD models.py /
ADD views.py /

RUN pip install flask
RUN pip install flask_httpauth
RUN pip install sqlalchemy
RUN pip install passlib
RUN pip install httplib2

CMD [ "python", "./views.py" ]