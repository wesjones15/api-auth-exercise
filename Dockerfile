FROM python:3

ADD models.py /
ADD views.py /

RUN pip install flask
RUN pip install sqlalchemy
RUN pip install passlib

CMD [ "python", "./views.py" ]