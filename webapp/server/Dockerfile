FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y build-essential
# needed for running ffmpeg on audio files
RUN sh -c '/bin/echo -e "Y\n" | apt-get install ffmpeg'

# python dependencies
RUN pip install --upgrade pip
RUN pip install pip-tools
RUN pip install numpy==1.19.5 Cython==0.29.24

# disable multiprocessing to fix sklearn bug
ENV SKLEARN_NO_OPENMP=TRUE

# rest of requirements
COPY requirements.in .
RUN pip-compile requirements.in && pip install -r requirements.txt

# revert to correct version of numpy
# RUN pip install numpy==1.19.5


EXPOSE 5000
CMD ["gunicorn","-b","0.0.0.0:5000","app:create_app"]
