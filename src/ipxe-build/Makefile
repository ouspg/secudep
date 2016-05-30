.PHONY: all build

TAG ?= latest

all: ipxe-$(TAG).usb ipxe-$(TAG).iso

clean:
	rm -f ipxe-*.{iso,usb}

build: Dockerfile boot.ipxe build.sh ipxe.patch *.pem
	docker build -t ipxe-build:$(TAG) --rm .

ipxe-$(TAG).usb: build
	docker run --rm ipxe-build:$(TAG) cat bin/ipxe.usb >$@

ipxe-$(TAG).iso: build
	docker run --rm ipxe-build:$(TAG) cat bin/ipxe.iso >$@

console: build
	docker run -ti ipxe-build:$(TAG) sh
