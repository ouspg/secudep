FROM alpine:3.3

ENV SYSLINUX syslinux-6.03

RUN apk -U upgrade && \
    apk add \
        build-base \
        curl \
        linux-headers \
        make \
        nasm \
        perl

WORKDIR /workdir
RUN curl -fO https://www.kernel.org/pub/linux/utils/boot/syslinux/${SYSLINUX}.tar.gz && \
    tar zxvf ${SYSLINUX}.tar.gz

WORKDIR /workdir/${SYSLINUX}
RUN make bios memdisk
