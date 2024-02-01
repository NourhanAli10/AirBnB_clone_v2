#!/usr/bin/python3
"""
Fabric script based on the file 3-deploy_web_static.py that deletes
out-of-date archives

execute: fab -f 100-clean_web_static.py do_clean -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, run
import os

env.hosts = ["54.90.37.130", "54.90.47.215"]


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 0:
        return

    try:
        # Delete unnecessary archives in versions folder
        local("ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number + 1))

        # Delete unnecessary archives in web_static/releases folder on both servers
        run("ls -1t /data/web_static/releases/ | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number + 1))

    except Exception as e:
        pass
