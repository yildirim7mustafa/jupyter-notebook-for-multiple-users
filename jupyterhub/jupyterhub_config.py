import os 

c = get_config()  

import nativeauthenticator
#c.JupyterHub.allow_named_servers = True
c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.JupyterHub.template_paths = [f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"]
c.Authenticator.admin_users = {"myadmin"}

import netifaces
docker0 = netifaces.ifaddresses('eth0')
docker0_ipv4 = docker0[netifaces.AF_INET][0]

c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.hub_connect_ip = docker0_ipv4['addr']

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']

#notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
#c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
#c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }


network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }
c.DockerSpawner.remove = True