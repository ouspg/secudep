# Secure Deployment for Challenging Environments

BSc. Thesis hopefully progressing with peer pressure from [OUSPG Open](https://github.com/ouspg/ouspg-open).


# things

 * Layers:
   * Hardware, boot, OS, configuration management
   * e.g. Physical server, iPXE, Alpine, cloud-init, Docker

 * Chain of trust:
   * We have to trust something. then pass the trust forward.
     * -> trusted USB media includes X.509 certificate pinned HTTPS URL
     * -> HTTPS delivers e.g. GPG public keys for CentOS/Debian repository validation
     * -> drop root SSH authorized_keys into installed OS
   * Lots of steps can be public on Internet
     * How to deal with things which can't?

 * Implementation
   * Easy to clone ("Personal boot infrastructure")
     * git clone, $EDITOR config, git push https://example.com/own/repo
   * Easy to build
     * Dockerize builds
     * Generate as much as possible
   * Future work (maybe out of scope for this thesis):
     * Maybe everything into one USB stick to work without Internet
