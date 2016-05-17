FROM alpine:3.3

RUN apk -U upgrade && \
    apk add \
        bash \
        cdrkit \
        coreutils \
        gcc \
        git \
        make \
        musl-dev \
        perl \
        syslinux \
        xz-dev

WORKDIR /workdir
RUN git clone https://git.ipxe.org/ipxe.git

WORKDIR /workdir/ipxe/src
COPY build.sh boot.ipxe ipxe.patch cert.cer ./

RUN sh build.sh
