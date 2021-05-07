#############################################
# BUILDER IMAGE: Only for building the code #
#############################################
FROM python:3.8-slim-buster AS builder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gcc \
    git \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    python3-dev

# Create user for building and installing pip packages inside its home for security purposes
RUN useradd --create-home cmsbuilder
ENV BUILDER_HOME=/home/cmsbuilder
WORKDIR $BUILDER_HOME
USER cmsbuilder

# Install dependencies and create layer cache of them
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Install test dependencies and create layer cache of them
COPY test-requirements.txt .
RUN pip install --user -r test-requirements.txt

######################################
# RUNNER IMAGE: For running the code #
######################################
FROM python:3.8-slim-buster

# Install here only runtime required packages
RUN apt-get update && apt-get install -y \
    gettext \
    libproj-dev \
    gdal-bin \
    python3-gdal

RUN groupadd -g 2000 cmsadm && \
    useradd -u 2000 -g cmsadm --create-home cmsadm

ENV USER_HOME=/home/cmsadm
WORKDIR $USER_HOME
USER cmsadm

# Copy pip install results from builder image
COPY --from=builder --chown=cmsadm /home/cmsbuilder/.local $USER_HOME/.local

# Make sure scripts installed by pip in .local are usable:
ENV PATH=$USER_HOME/.local/bin:$PATH
RUN mkdir tmp

COPY --chown=cmsadm domain/ domain/
COPY --chown=cmsadm infrastructure/ infrastructure/
COPY --chown=cmsadm locale/ locale/
COPY --chown=cmsadm presentation/ presentation/
COPY --chown=cmsadm projectCato/ projectCato/
COPY --chown=cmsadm templates/ templates/
COPY --chown=cmsadm manage.py manage.py
COPY --chown=cmsadm scripts/ scripts/
