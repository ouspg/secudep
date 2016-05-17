# secudep - Secure Deployment Tooling

## Tools

Various tools to build things.

### ipxe-for

One script to bind together all tools below.

### ipxe-build

Docker-stuff to build ipxe usb and iso images with certificate pinning.

### x509extract

Extract and validate X.509 certificate from given host and port. Ugly. Rewrite needed.

```
$ ./x509extract github.com 443
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  184k  100  184k    0     0  82186      0  0:00:02  0:00:02 --:--:-- 82157
depth=1 /C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert SHA2 Extended Validation Server CA
verify error:num=20:unable to get local issuer certificate
verify return:0
DONE
depth=1 /C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert SHA2 Extended Validation Server CA
verify error:num=20:unable to get local issuer certificate
verify return:0
DONE

oherrala@code0253:~/ouspg/secudep/src/x509extract$ ls -l *.cer
-rw-r--r--  1 oherrala  staff  7244 May 17 16:40 github.com.cer
```
