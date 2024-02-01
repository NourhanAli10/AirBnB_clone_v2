#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers, using the
function do_deploy
"""

from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ["54.90.37.130", "54.90.47.215"]


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Extract archive to /data/web_static/releases/<archive_filename_without_extension>/
        archive_filename = archive_path.split("/")[-1]
        folder_name = archive_filename.split(".")[0]
        release_path = "/data/web_static/releases/{}".format(folder_name)
        run("sudo mkdir -p {}".format(release_path))
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_filename, release_path))

        # Remove the archive from the web server
        run("sudo rm /tmp/{}".format(archive_filename))

        # Move contents to the current version
        run("sudo mv {}/web_static/* {}/".format(release_path, release_path))
        run("sudo rm -rf {}/web_static".format(release_path))

        # Remove the old symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("sudo ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(str(e)))
        return False
