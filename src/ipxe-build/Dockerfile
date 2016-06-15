FROM alpine:3.4

RUN apk -U upgrade && \
    apk add \
        bash \
        cdrkit \
        coreutils \
        gcc \
        git \
        make \
        mg \
        musl-dev \
        openssl \
        perl \
        syslinux \
        xz-dev

WORKDIR /workdir
RUN git clone https://git.ipxe.org/ipxe.git

WORKDIR /workdir/ipxe/src
COPY build.sh boot.ipxe ipxe.patch *.pem ./

RUN sh build.sh
