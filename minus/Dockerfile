FROM python:3.6
COPY . /opt/minus/
RUN cd /opt/minus && \
    pip3.6 install -r requirements.txt
EXPOSE 5052
CMD ["python3.6", "/opt/minus/minus.py"]