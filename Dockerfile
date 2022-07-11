FROM ubuntu:18.04

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8

RUN apt-get update
RUN apt-get install g++ python3-dev python3-pip curl automake wget make chromium-chromedriver -y
# RUN ["cp",  "/usr/lib/chromium-browser/chromedriver", "/usr/bin"]
RUN wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
RUN tar zxfv mecab-0.996-ko-0.9.2.tar.gz
WORKDIR /mecab-0.996-ko-0.9.2
RUN ./configure --build=arm
RUN make
RUN make check
RUN su
RUN make install

WORKDIR /
RUN wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
RUN tar zxfv mecab-ko-dic-2.1.1-20180720.tar.gz
WORKDIR /mecab-ko-dic-2.1.1-20180720
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install

WORKDIR /
COPY app/requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
