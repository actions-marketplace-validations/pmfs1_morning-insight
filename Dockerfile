FROM ubuntu:rolling
COPY ./ENTRYPOINT.ps1 /ENTRYPOINT.ps1
COPY ./DATABASE.jsonc /DATABASE.jsonc
RUN apt-get update -y && apt-get install -y --install-recommends apt-utils openssh-client gnupg2 dirmngr iproute2 procps lsof htop net-tools psmisc curl tree wget rsync ca-certificates unzip bzip2 zip nano vim-tiny less jq lsb-release apt-transport-https dialog libc6 libgcc1 libkrb5-3 libgssapi-krb5-2 libicu[0-9][0-9] liblttng-ust[0-9] libstdc++6 zlib1g locales sudo ncdu man-db strace manpages manpages-dev init-system-helpers software-properties-common && sudo apt-get full-upgrade -y && wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && sudo dpkg -i packages-microsoft-prod.deb && sudo apt-get update -y && sudo apt-get install -y powershell --install-recommends && sudo rm packages-microsoft-prod.deb && lsb_release -a
ENTRYPOINT [ "pwsh", "-c", "/ENTRYPOINT.ps1" ]