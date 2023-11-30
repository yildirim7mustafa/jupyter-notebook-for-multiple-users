# Jupyter Notebook For Multiple Users
It is a multi-user Hub that spawns, manages, and proxies multiple instances of the single-user Jupyter notebook server.Users can sign up (admin has to confirm it) and when a user start a server, hub creates a container for him.Provides isolation development environment for users 

## Steps to Setup

**1. Clone the repository**

```bash
git clone https://github.com/yildirim7mustafa/jupyter-notebook-for-multiple-users 
```

**2. Change admin username (optional)**

jupyterhub/jupyterhub_config.py -> c.Authenticator.admin_users = {"myadmin"}

**3. Up to docker compose**

```bash
docker compose up -d 
```
**4. Sign up for admin**
<p> create an admin account </p>

**5. Sign up for user**
<p> if you are trying local, you may use new private window </p>



