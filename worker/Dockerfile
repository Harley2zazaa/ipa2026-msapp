FROM python
WORKDIR /home/myapp
COPY ./requirements.txt /home/myapp/
RUN pip install -r requirements.txt
COPY ./consumer.py /home/myapp/
COPY ./callback.py /home/myapp/
COPY ./database.py /home/myapp/
COPY ./router_client.py /home/myapp/
CMD ["python","-u", "/home/myapp/consumer.py"]