FROM python:3.6
WORKDIR /app
COPY . /app
RUN apt-get update
RUN sh -c '/bin/echo -e "Y\n" | apt-get install ffmpeg'
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn","-b","0.0.0.0:5000","app:create_app()"]
