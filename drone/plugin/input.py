"""
This module contains utility functions for finding and parsing plugin
input during development or normal runtime.
"""
import sys
import json


def get_input():
    """
    Look for input in argv and stdin. De-serialize and return whatever
    we can find.

    :rtype: dict
    :return: A dictionary of parameters from Drone.
    :raises: ValueError if no valid input is found, since this is required
        for normal plugin operation.
    """

    if '--' in sys.argv:
        payload_str = _get_input_from_argv()
    else:
        payload_str = _get_input_from_stdin()
    return json.loads(payload_str)


def _get_input_from_stdin():
    """
    This is only used during plugin testing and development. Drone
    passes params in via argv.

    :rtype: str
    :return: The value passed to the plugin via stdin.
    :raises: :py:class:`ValueError` if nothing is passed in.
    """
    params = sys.stdin.read()
    if not params:
        raise ValueError("No plugin input was found in argv or stdin.")
    return params


def _get_input_from_argv():
    """
    Drone passes parameters in via argv under normal operation. These
    are started with a ``--``.

    :rtype: str
    :returns: The value passed to the plugin via argv.
    :raises: ValueError if we found a ``--`` delimeter but no
        subsequent JSON payload.
    """
    payload_index = sys.argv.index('--') + 1
    params = sys.argv[payload_index:]
    if not params:
        raise ValueError(
            "A JSON payload was expected after the -- delimiter, but none "
            "was found.")
    return ' '.join(params)
