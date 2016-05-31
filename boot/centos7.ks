# Default environment
text
lang en_US.UTF-8
keyboard --vckeymap=fi
timezone UTC --utc --ntpservers=0.centos.pool.ntp.org,1.centos.pool.ntp.org,2.centos.pool.ntp.org,3.centos.pool.ntp.org

# Security
auth --enableshadow --passalgo=sha512
selinux --disabled

# Networking
network --bootproto=dhcp --ipv6=auto --activate
firewall --enabled --ssh

# Installation
url --url="http://mirror.centos.org/centos/7/os/x86_64/"
ignoredisk --only-use=sda
autopart --type=lvm
clearpart --all --initlabel --drives=sda
bootloader --append=" crashkernel=auto" --location=mbr --boot-drive=sda

eula --agreed
reboot --eject

%packages --ignoremissing
@^minimal
@core
%end
