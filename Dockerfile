FROM apache/spark-py:latest

COPY sparkApp.py /sparkApp.py

RUN chmod +x /sparkApp.py

CMD ["/usr/local/spark/bin/spark-submit", "--master", "local[*]", "/sparkApp.py"]

