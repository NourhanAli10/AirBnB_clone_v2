#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers using the function do_deploy.
"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ["54.90.37.130", "54.90.47.215"]


def do_deploy(archive_path):
    """Deploys the web_static archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/
        archive_filename = archive_path.split('/')[-1]
        folder_name = archive_filename.split('.')[0]
        path_release = "/data/web_static/releases/"

        run("mkdir -p {}{}".format(path_release, folder_name))
        run("tar -xzf /tmp/{} -C {}{}".format(
            archive_filename, path_release, folder_name))

        # Remove the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Move the contents of the extracted folder
        run("mv {0}{1}/web_static/* {0}{1}/".format(
            path_release, folder_name))

        # Remove the empty web_static folder
        run("rm -rf {}{}/web_static".format(path_release, folder_name))

        # Remove the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {0}{1} /data/web_static/current".format(
            path_release, folder_name))

        return True

    except Exception as e:
        return False
