FROM python
WORKDIR /home/myapp
COPY ./requirements.txt /home/myapp/
RUN pip install -r requirements.txt
COPY ./database.py /home/myapp/
COPY ./producer.py /home/myapp/
COPY ./scheduler.py /home/myapp/

CMD ["python","-u", "/home/myapp/scheduler.py"]