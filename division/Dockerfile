FROM python:3.6
COPY . /opt/division/
RUN cd /opt/division && \
    pip3.6 install -r requirements.txt
EXPOSE 5054
CMD ["python3.6", "/opt/division/division.py"]