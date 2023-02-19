FROM python:alpine
WORKDIR /home/data
COPY ./ ./
CMD ["python" ,"shalakaAssignment3.py"]
