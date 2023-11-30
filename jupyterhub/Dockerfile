ARG JUPYTERHUB_VERSION
FROM jupyterhub/jupyterhub:$JUPYTERHUB_VERSION

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

RUN apt-get update &&\
    apt-get install python3-netifaces

# Install dependencies (for advanced authentication and spawning)
RUN pip install \
    dockerspawner\
    jupyterhub-nativeauthenticator