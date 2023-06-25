FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY message_service.py /app/message_service.py
RUN pip install flask pika 
EXPOSE 8021
CMD ["python", "-u", "message_service.py"]
