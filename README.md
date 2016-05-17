# Secure Deployment for Challenging Environments

BSc. Thesis hopefully progressing with peer pressure from [OUSPG Open](https://github.com/ouspg/ouspg-open).

**Research question/problem:** How to securely deploy/provision Linux installations over insecure network/Internet using truested starting point?


# things

 * Layers to consider:
   * Hardware, boot, OS, configuration management, application
   * e.g. Physical server + USB media, iPXE, Alpine, cloud-init, Docker
   * e.g. Virtualization + PXE, iPXE, Some OS, ...
   * UEFI Secure Boot out of scope?
   * How high to climb in this thesis?

 * Chain of trust:
   * We have to trust something. then pass the trust forward.
     * -> boot image which GPG signed which is verified and then written into USB media
     * -> trusted USB media includes X.509 certificate pinned HTTPS URL
     * -> Next step (HTTPS) could use HTTP Basic Auth or X.509 client cert for authentication
     * -> HTTPS delivers e.g. GPG public keys for Alpine/CentOS/Debian repository validation
     * -> drop root SSH authorized_keys into installed OS
   * Lots of steps can be public on Internet
     * How to deal with things which can't?
     * Preshared password? X.509 client cert auth?
   * What are "impossible" (beyond reasonable effort) or hard to trust?
     * Hardware backdoors/vulnerabilities, OS distribution backdoors/vulns

 * What existing software and features there already is?
   * Network booting: iPXE?
   * Certificate pinning: is iPXE's pinning sufficient?
   * Repository and package signing: GPG signatures? OpenBSD Signify?
   * Configuration management: cloud-init? Ansible? Salt? Puppet?
   * Applications: Docker?

 * Implementation
   * Easy to copy and adjust ("Personal Boot Infrastructure")
     * git clone, $EDITOR config, scripts/build, git push https://example.com/own/repo
     * Trust of the build environment
       * Building certificate pinnings with TLS MITM not worth it
       * Signing keys, etc. need to be protected
   * Easy to build
     * Dockerize builds?
     * Generate as much as possible from simple configuration
   * Future work (easily out of scope for this thesis):
     * Maybe everything into one USB stick to work without Internet
     * Boot verifies signed commits from Git repo

 * stuff to read:
   * Secure Server Provisioning and Communication Mechanism in Cloud
     * http://www.ijarcsse.com/docs/papers/Volume_5/4_April2015/V5I4-0512.pdf
   * Information security auditing tool for authorities – Katakri 2015
     * http://formin.fi/public/default.aspx?contentid=328713&contentlan=2&culture=en-US
     * http://www.defmin.fi/files/3417/Katakri_2015_Information_security_audit_tool_for_authorities_Finland.pdf
   * x86 Network Booting: Integrating gPXE and PXELINUX
     * https://kernel.org/doc/ols/2008/ols2008v1-pages-9-18.pdf
   * An Updated Performance Comparison of Virtual Machines and Linux Containers
     * https://domino.research.ibm.com/library/cyberdig.nsf/papers/0929052195DD819C85257D2300681E7B/$File/rc25482.pdf
     * http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=7095802&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D7095802
   * An Approach for Secure Software Installation
     * http://static.usenix.org/legacy/events/lisa02/tech/full_papers/venkatakrishnan/venkatakrishnan_html/
   * signify: Securing OpenBSD From Us To You
     * https://www.openbsd.org/papers/bsdcan-signify.html
   * Developing Software in a Hostile Environment
     * https://www.openbsd.org/papers/dev-sw-hostile-env.html
   * CAIA Testbed for TEACUP Experiments
     * Notes: Unsecure boot (DHCP, TFTP, HTTP)
     * version 1: http://caia.swin.edu.au/reports/140314B/CAIA-TR-140314B.pdf
     * version 2: http://caia.swin.edu.au/reports/150210C/CAIA-TR-150210C.pdf
   * Operating System Support for Run-Time Security with a Trusted Execution Environment
     * https://www.researchgate.net/profile/Javier_Gonzalez33/publication/297732884_Operating_Security_System_Support_for_Run-Time_Security_with_a_Trusted_Execution_Environment/links/56e1b86208ae40dc0abf5981.pdf
   * Fedora's Secure Boot FAQ
     * https://fedoraproject.org/wiki/Secureboot
