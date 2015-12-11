"""
A basic CLI utility to quickly bootstrap a new Python-based Drone plugin.

This works by downloading a zip of the Python plugin template GitHub
repository (see ``TEMPLATE_REPO`` below). We then substitute variables
surrounded in double curly braces (like ``{{ AUTHOR_NAME }}``), resulting
in a mostly ready-to-go plugin directory.

See :py:func:`prompt_for_variables` for details on the variables and how
the substitutions work.
"""
from future import standard_library
standard_library.install_aliases()

import io
import os
import shutil
import socket
import zipfile
import argparse
import tempfile
import datetime
import urllib.request  # noqa

socket.setdefaulttimeout(10.0)
TEMPLATE_REPO = {
    'repo_owner': 'gtaylor',
    'repo_name': 'drone-python-plugin-template',
}

parser = argparse.ArgumentParser(
    description='Bootstraps a new Python-based Drone plugin.')
parser.add_argument('plugin_name', type=str, help='The plugin name.')


def download_and_extract_template(plugin_path):
    """
    Downloads a zip archive of the Python plugin template repo on GitHub.
    Extracts it to the value provided in ``plugin_path``.

    :param str plugin_path: The plugin dir will end up being created here.
    """
    if os.path.exists(plugin_path):
        raise ValueError('Directory {} already exists.'.format(plugin_path))

    template_archive_url = \
        "https://github.com/%(repo_owner)s/%(repo_name)s/archive/master.zip"
    req = urllib.request.urlopen(template_archive_url % TEMPLATE_REPO)
    # If the repo ever gets huge, we'll probably want to use a proper tempfile.
    fobj = io.BytesIO(req.read())
    zip_file = zipfile.ZipFile(file=fobj)

    # We can't extract the zip directly to a directory name of our choosing.
    # Extract it to a temporary directory, then move it to where the
    # user is expecting.
    with tempfile.TemporaryDirectory() as tmpdir_path:
        zip_file.extractall(path=tmpdir_path)
        extracted_dir_name = '%(repo_name)s-master' % TEMPLATE_REPO
        extracted_path = os.path.join(tmpdir_path, extracted_dir_name)
        shutil.move(extracted_path, plugin_path)


def prompt_for_variables(plugin_path):
    """
    Populates all of the template variables we'll be substituting, prompting
    the user for values as needed.

    :param str plugin_path: The path where the plugin directory will be
        created.
    :rtype: dict
    :return: A dict of template variables that will be substituted.
    """
    template_vars = {
        'PLUGIN_NAME': os.path.basename(plugin_path),
        'SHORT_DESCRIPTION': '',
        'AUTHOR_NAME': '',
        'AUTHOR_EMAIL': '',
        'ORG_OR_AUTHOR_USERNAME': '',
        'YEAR': str(datetime.datetime.now().year),
    }
    # This has to match the length of the title in ReST.
    template_vars['TITLE_UNDERLINE'] = len(template_vars['PLUGIN_NAME']) * '='

    print("Creating a new plugin called:", template_vars['PLUGIN_NAME'])
    while not template_vars['AUTHOR_NAME']:
        template_vars['AUTHOR_NAME'] = \
            input("What is the plugin author's name?: ").strip()
    while not template_vars['AUTHOR_EMAIL']:
        template_vars['AUTHOR_EMAIL'] = \
            input("What is the plugin author's email address?: ").strip()
    while not template_vars['SHORT_DESCRIPTION']:
        template_vars['SHORT_DESCRIPTION'] = \
            input("Provide a one-sentence overview of the plugin: ").strip()
    while not template_vars['ORG_OR_AUTHOR_USERNAME']:
        template_vars['ORG_OR_AUTHOR_USERNAME'] = \
            input("What is the GitHub/Bitbucket/GitLab/etc organization "
                  "or owner username for the plugin repo? "
                  "(ex: drone, gtaylor): ").strip()
    return template_vars


def replace_template_variables_in_file(file_path, template_vars):
    """
    Given a file, replace all matching template variables in it. These are
    denoted by double curly braces. IE: {{ SOME_VAR }}

    :param str file_path: Path to a file to substitute variables in.
    :param dict template_vars: A dict of variables to substitute in.
    """
    with open(file_path) as fobj:
        contents = fobj.read()

    for key, val in template_vars.items():
        contents = contents.replace('{{ ' + key + ' }}', val)
    with open(file_path, 'w') as fobj:
        fobj.write(contents)


def replace_all_template_variables(plugin_path, template_vars):
    """
    Go through all files in the plugin dir and replace template variables
    as we encounter them.

    :param str plugin_path: Path to the newly created plugin dir.
    :param dict template_vars: The template variables to substitute in.
    """
    for root, dirs, files in os.walk(plugin_path):
        for t_file in files:
            file_path = os.path.join(root, t_file)
            replace_template_variables_in_file(file_path, template_vars)


def main():
    """
    Main entrypoint for the command.
    """
    args = parser.parse_args()
    plugin_path = args.plugin_name

    print('Downloading Python Drone plugin template...')
    download_and_extract_template(plugin_path)
    template_vars = prompt_for_variables(plugin_path)
    replace_all_template_variables(plugin_path, template_vars)


if __name__ == '__main__':
    main()
