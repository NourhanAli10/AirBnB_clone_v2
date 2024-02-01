#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env, put, run, Connection

env.hosts = ["54.90.37.130", "54.90.47.215"]
user_name = ""


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False

    file = archive_path.split("/")[-1]
    file_name = file.split(".")[0]
    
    with Connection(user_name@env.hosts) as conn:
        conn.put(archive_path, "/tmp/{}".format(file))
        

