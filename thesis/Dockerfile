FROM debian:jessie

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y -o aquire::retries=10 install \
            make \
            texlive \
            texlive-lang-english \
            texlive-lang-finnish \
            texlive-latex-extra \
    && \
    apt-get clean

WORKDIR /build
COPY * ./
RUN make
