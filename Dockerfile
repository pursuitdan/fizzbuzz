FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python git 
RUN git clone https://github.com/pursuitdan/fizzbuzz
WORKDIR /fizzbuzz
RUN ["python", "test_fizzbuzz.py"]
CMD ["python", "c_fizzbuzz.py"]
