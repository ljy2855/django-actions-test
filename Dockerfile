From python:3.8.13


WORKDIR /Workspace

COPY ./requirements.txt /Workspace/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Workspace/requirements.txt && \
    pip install --no-cache-dir uwsgi


COPY . /Workspace

CMD ["python", "/Workspace/mysite/manage.py", "migrate"]

CMD ["uwsgi", "--ini", "/Workspace/uwsgi.ini"]
# uwsgi로 실행할 수 있도록 cmd 교체

EXPOSE 8000