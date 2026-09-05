FROM python
WORKDIR /home/myapp
COPY ./requirements.txt /home/myapp/
RUN pip install -r requirements.txt
COPY ./worker1.py /home/myapp/
COPY ./producer.py /home/myapp/
COPY ./database.py /home/myapp/
CMD ["python","-u", "/home/myapp/worker1.py"]