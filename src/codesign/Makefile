.PHONY: all

all: codesign.pem

codesign.key:
	openssl genrsa -out $@ 4096

codesign.pem: codesign.key
	openssl req -new -x509 -config ca.cnf -extensions codesigning -key $< -out $@
