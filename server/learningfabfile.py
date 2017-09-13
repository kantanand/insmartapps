import os
import time
from fabric.api import local, run, env, put, task, cd, sudo
from fabric.tasks import execute
from fabric.contrib.project import rsync_project
from fabric.contrib.files import sed

env.learning_root = '/home/ubuntu/learning'

host_name = ""
domain_name = ""
db_host_name = "localhost"
if len(env.hosts) > 0:
    host_name = env.hosts[0].split('@')[-1]
    domain_name = host_name

if 'domain_name' in env:
    domain_name = env.domain_name
    host_name = domain_name

# Check Server and Set DB Connection
if host_name == 'insmartapps.com':
    db_host_name = 'localhost'
else:
    db_host_name = "localhost"

# set-up uwsgi
@task
def uwsgi():
    run('mkdir -p /tmp/learning/etc/init.d')
    put('webserver/uwsgi/etc/init.d/learning-uwsgi.ini', '/tmp/learning/etc/init.d/')
    put('webserver/uwsgi/etc/init.d/learning-uwsgi.sh',
        '/tmp/learning/etc/init.d/', mirror_local_mode=True)
    run('sudo cp -r /tmp/learning/etc/init.d/* /etc/init.d/')
    run('sudo chmod 700 /etc/init.d/learning-uwsgi.sh')

# set-up nginx
@task
def nginx():
    run('mkdir -p /tmp/learning')
    put('webserver/certs/*', '/tmp/learning')
    run('mkdir -p /tmp/learning/etc/nginx/sites-enabled')
    put('webserver/nginx/etc/nginx/sites-enabled/default',
        '/tmp/learning/etc/nginx/sites-enabled/')
    sed('/tmp/learning/etc/nginx/sites-enabled/default',
        "\[SERVER_NAME\]", host_name, backup='')
    run('sudo cp -r /tmp/learning/* /')
    run('sudo /etc/init.d/nginx restart')

# start uwsgi
@task
def start_uwsgi():
    sudo('/etc/init.d/learning-uwsgi.sh start')

# stop uwsgi
@task
def stop_uwsgi():
    sudo('/etc/init.d/learning-uwsgi.sh stop')

# force stop uwsgi
@task
def force_stop_uwsgi():
    sudo('pkill -9 "uwsgi"')

# restart uwsgi
@task
def restart():
    execute(stop_uwsgi)
    execute(start_uwsgi)

# fore restart uwsgi
@task
def force_restart():
    execute(force_stop_uwsgi)
    execute(start_uwsgi)

# first time for setting up db Note: all data will be lost
@task
def setupdb():
    run('mkdir -p /tmp/learning')
    put('database/learning.sql', '/tmp/learning')
    run('mysql -prootusk -uroot < /tmp/learning/learning.sql')

# sync all learning and learning django files
@task
def cp():
    print('copying learning source')
    rsync_project('/home/ubuntu', 'learning')

@task
def set_config_values():
    """
    used to set the config values 
    """
    sed('/home/ubuntu/learning/learning/settings-production.py',
        "\[SERVER_NAME\]", host_name, backup='')
    sed('/home/ubuntu/learning/learning/settings.py',
        "\[SERVER_NAME\]", host_name, backup='')

    sed('/home/ubuntu/learning/config.py', "\[DB_HOST_NAME\]", db_host_name, backup='')
    sed('/home/ubuntu/learning/config.py', "\[DB_HOST_NAME\]", db_host_name, backup='')

@task
def create_base_folders():
    run('mkdir -p /home/ubuntu/learning/log')
    run('mkdir -p /home/ubuntu/learning/uploads')
    run('mkdir -p /home/ubuntu/learning/media/uploads')
    run('mkdir -p /home/ubuntu/media/uploads')
    run('/home/ubuntu/env/bin/pip install -r /home/ubuntu/learning/requirements.txt')

# collect all static files
@task
def static():
    with cd(env.learning_root):
        run('/home/ubuntu/env/bin/python manage.py collectstatic -v0 --noinput --settings=learning.settings-production')

# sync all db
@task
def dbsync():
    with cd(env.learning_root):
        if host_name == 'insmartapps.com':
            run('/home/ubuntu/env/bin/python manage.py migrate')
        else:
            run('/home/ubuntu/env/bin/python manage.py makemigrations')
            run('/home/ubuntu/env/bin/python manage.py migrate')

# create super user
@task
def create_super_user():
    with cd(env.learning_root):
        run('less cr_superuser.py | /home/ubuntu/env/bin/python manage.py shell')

# clear all code
@task
def clearcode():
    run('rm -rf /home/ubuntu/learning')

# clearn all static riles
@task
def clearstatic():
    run('rm -rf /home/ubuntu/static')

# clear all code and static files
@task
def clear():
    execute(clearcode)
    execute(clearstatic)

# needed for first time set up of machine
@task
def setup():
    execute(uwsgi)
    execute(nginx)
    execute(setupdb)
    execute(cp)
    execute(dbsync)
    execute(static)
    execute(create_super_user)
    execute(start_uwsgi)

# everytime code can be deployed to production or testing server
# through this deploy

# for daily deploy
@task
def deploy():
    execute(cp)
    execute(dbsync)
    execute(static)

# for giving build
@task
def clean_deploy():
    execute(clear)
    execute(setupdb)
    execute(deploy)
    execute(create_super_user)
    execute(force_restart)

@task
def check_domain():
    print domain_name
