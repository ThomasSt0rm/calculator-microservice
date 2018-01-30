FROM python:3.6
COPY . /opt/frontend/
RUN cd /opt/frontend && \
    pip3.6 install -r requirements.txt
EXPOSE 5053
CMD ["python3.6", "/opt/frontend/frontend.py"]