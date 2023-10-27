FROM python:3.7
COPY requirements.txt .
RUN python3 -m pip install -r \
    requirements.txt --quiet --no-cache-dir \
    && rm -f requirements.txt
COPY ./transform_2.py .
CMD ["python3", "transform_2.py"]