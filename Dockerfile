FROM ubuntu:16.04
WORKDIR /home/ansible

RUN apt-get update && apt-get -fqy install python-pip sshpass python3 python3-venv
COPY . ./

RUN pip install --upgrade pip
RUN pip install pywinrm && pip install pywinrm[credssp]
RUN pip install ansible


ENV	DEBIAN_FRONTEND noninteractive
ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV ANSIBLE_SCP_IF_SSH=yes
ENV ANSIBLE_timeout=100
ENV ANSIBLE_allow_world_readable_tmpfiles=True


# RUN pip install virtualenv
# RUN python3 -m venv venv
# RUN . venv/bin/activate
RUN pip install -r requirements.txt

# CMD ./ansible-init.sh





#ENV ANSIBLE_DEBUG=1 