FROM python:3-alpine
RUN pip install bottle requests
COPY main.py /
CMD ["python", "/main.py"]
