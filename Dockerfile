FROM python:3

ADD src /src
ADD data /data
ADD requirements.txt /

RUN pip install cmake
RUN pip install dlib
RUN pip install -r requirements.txt

RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y

CMD [ "python", "src/main.py" ]