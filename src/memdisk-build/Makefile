.PHONY: all build

all: memdisk

clean:
	rm -rf memdisk

build: Dockerfile
	docker build -t memdisk-build --rm .

memdisk: build
	docker run --rm memdisk-build cat bios/memdisk/memdisk >$@
