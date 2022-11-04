FROM ubuntu:rolling
COPY ./main.py /main.py
COPY ./DATABASE.json /DATABASE.json
RUN apt-get update -y && apt-get install -y --install-recommends apt-utils openssh-client gnupg2 dirmngr iproute2 procps lsof htop net-tools psmisc curl tree wget rsync ca-certificates unzip bzip2 zip nano vim-tiny less jq lsb-release apt-transport-https dialog libc6 libgcc1 libkrb5-3 libgssapi-krb5-2 libicu[0-9][0-9] liblttng-ust[0-9] libstdc++6 zlib1g locales sudo ncdu man-db strace manpages manpages-dev init-system-helpers software-properties-common python3.11 python3.11-distutils python3.11-dev python3-pip && python3.11 -m pip install --user pipenv && sudo apt-get full-upgrade -y && lsb_release -a
ENTRYPOINT [ "/bin/bash", "-c", "OUTPUT=$(python3.11 /main.py) && echo OUTPUT=$OUTPUT >> $GITHUB_OUTPUT" ]