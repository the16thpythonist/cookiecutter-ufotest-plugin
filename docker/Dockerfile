FROM debian:buster
MAINTAINER Jonas Teufel <jonseb1998@gmail.com>

ENV UFOTEST_REPOSITORY="https://github.com/the16thpythonist/ufotest.git"

# == INSTALLING SYSTEM DEPENDENCIES ==

RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y python3 python3-pip

# == INSTALLING UFOTEST ==

# Here we install the main ufotest code from the repository and not from pip itself. This makes sure we have the most
# recent development version of ufotest to test our plugin with.
RUN mkdir /root/Software && \
    cd /root/Software && \
    git clone $UFOTEST_REPOSITORY && \
    cd ufotest && \
    python3 -m pip install --user . && \
    export PATH=/root/.local/bin:$PATH && \
    ufotest --version

# This will actually create the ufotest installation folder.
RUN export PATH=/root/.local/bin:$PATH && \
    ufotest init && \
    ls -a $HOME/.ufotest

# -- Initialize entrypoint for our plugin code --
# Here we create a folder within the plugins folder of the ufotest installation which has the name of our plugin,
# but we dont actually put anything in it. The content will be the code in our local folder of the main machine which
# is mounted / mapped to that location within the contaienr
RUN mkdir $HOME/.ufotest/plugins/{{ cookiecutter.project_slug }}


ENTRYPOINT docker/entrypoint.sh
CMD ufotest --help
