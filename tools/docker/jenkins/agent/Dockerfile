FROM jenkins/ssh-agent:debian-jdk17

RUN apt-get update \
    && apt-get install -y sudo curl git unzip wget \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN sh -c "echo \"jenkins ALL=(ALL:ALL) NOPASSWD: ALL\" >> /etc/sudoers"

# # Install Terraform
# RUN apt-get update \
#     && apt-get install -y gnupg software-properties-common \
#     && wget -O- https://apt.releases.hashicorp.com/gpg | \
#     gpg --dearmor | tee /usr/share/keyrings/hashicorp-archive-keyring.gpg \
#     && gpg --no-default-keyring \
#     --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
#     --fingerprint \
#     && sh -c "echo \"deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
#     https://apt.releases.hashicorp.com $(lsb_release -cs) main\"" \
#     | tee /etc/apt/sources.list.d/hashicorp.list \
#     && apt-get update && apt-get install -y terraform \
#     && apt-get clean \
#     && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# # Install AWS CLI
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
#     && unzip awscliv2.zip \
#     && rm awscliv2.zip \
#     && ./aws/install
