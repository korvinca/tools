FROM jenkins/ssh-agent:debian-jdk17

RUN apt-get update \
    && apt-get install -y curl git unzip sudo wget \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_18.x -o /tmp/nodesource_setup.sh \
    && bash /tmp/nodesource_setup.sh \
    && apt-get install -y nodejs \
    && rm /tmp/nodesource_setup.sh \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN sh -c "echo \"jenkins ALL=(ALL:ALL) NOPASSWD: ALL\" >> /etc/sudoers"