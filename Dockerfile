FROM python:3
ADD src /
ADD data /
ADD requirements.txt /
RUN pip install -r requirements.txt

CMD [ "python", "./src/main.py" ]