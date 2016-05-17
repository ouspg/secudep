
TAG ?= latest

all: ipxe.usb ipxe.iso

build: Dockerfile boot.ipxe build.sh
	docker build -t ipxe-build:$(TAG) --rm .

ipxe.usb: build
	docker run --rm ipxe-build:$(TAG) cat bin/$@ >$@

ipxe.iso: build
	docker run --rm ipxe-build:$(TAG) cat bin/$@ >$@
