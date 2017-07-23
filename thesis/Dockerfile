FROM debian:jessie-slim

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y -o acquire::retries=10 install \
            make \
            texlive \
            texlive-lang-english \
            texlive-lang-finnish \
            texlive-latex-extra \
            lacheck \
            chktex \
    && \
    apt-get clean

WORKDIR /build
COPY * ./
RUN make
