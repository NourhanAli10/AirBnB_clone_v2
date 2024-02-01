#!/usr/bin/python3
"""This module generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using
the function do_pack."""

from fabric.api import local
import datetime


def do_pack():
    """
    Create a compressed archive from the web_static folder.
    """
    local("mkdir -p versions/")
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    path = local('tar -cvzf {} web_static/'.format(file_name), capture=True)
    if path.succeeded:
        return file_name
    else:
        return None
