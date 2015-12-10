from future import standard_library
standard_library.install_aliases()

import io
import os
import shutil
import tempfile
import socket
import zipfile
import urllib.request  # noqa

socket.setdefaulttimeout(10.0)
REPO_OWNER = 'gtaylor'
REPO_NAME = 'drone-hipchat'
EXTRACTED_DIR_NAME = '{}-master'.format(REPO_NAME)
TEMPLATE_URL = "https://github.com/{}/{}/archive/master.zip"


def download_and_extract_template(template_path):
    if os.path.exists(template_path):
        raise ValueError('Directory {} already exists.'.format(template_path))

    req = urllib.request.urlopen(TEMPLATE_URL.format(REPO_OWNER, REPO_NAME))
    fobj = io.BytesIO(req.read())
    zip_file = zipfile.ZipFile(file=fobj)

    with tempfile.TemporaryDirectory() as tmpdir_path:
        zip_file.extractall(path=tmpdir_path)
        extracted_path = os.path.join(tmpdir_path, EXTRACTED_DIR_NAME)
        shutil.move(extracted_path, template_path)


def main():
    plugin_name = 'test-plugin'

    print("Yay")
    download_and_extract_template(plugin_name)
