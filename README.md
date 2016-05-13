# Secure Deployment for Challenging Environments

BSc. Thesis hopefully progressing with peer pressure from [OUSPG Open](https://github.com/ouspg/ouspg-open).


# things

 * Layers:
   * Hardware, boot, OS, configuration management, application
   * e.g. Physical server, iPXE, Alpine, cloud-init, Docker

 * Chain of trust:
   * We have to trust something. then pass the trust forward.
     * -> trusted USB media includes X.509 certificate pinned HTTPS URL
     * -> HTTPS delivers e.g. GPG public keys for CentOS/Debian repository validation
     * -> drop root SSH authorized_keys into installed OS
   * Lots of steps can be public on Internet
     * How to deal with things which can't?

 * Evaluate state of the art in
   * Network booting: iPXE?
   * Certificate pinning: is iPXE's pinning sufficient?
   * Repository and package signing: GPG signatures? OpenBSD Signify?
   * Configuration management: cloud-init? Ansible? Salt? Puppet?
   * Applications: Docker?

 * Implementation
   * Easy to clone ("Personal boot infrastructure")
     * git clone, $EDITOR config, scripts/build, git push https://example.com/own/repo
     * Trust of the build environment
       * Building certificate pinnings with TLS MITM not worth it
   * Easy to build
     * Dockerize builds?
     * Generate as much as possible from simple configuration
   * Future work (easily out of scope for this thesis):
     * Maybe everything into one USB stick to work without Internet
     * Boot verifies signed commits from Git repo
