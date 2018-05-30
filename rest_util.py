# -*- encoding: UTF-8 -*-

"""
Usage:
  rest_util.py ROBOT_IP
  rest_util.py (-h | --help)
Options:
  -h, --help
"""

from naoqi import ALProxy
from docopt import docopt


def main(arguments):

    robotIP = arguments.pop("ROBOT_IP", None)
    if (robotIP is None):
        robotIP = "127.0.0.1"

    port = 9559

    motion = ALProxy("ALMotion", robotIP, port)
    motion.rest()

if __name__ == "__main__":
    arguments = docopt(__doc__)

    main(arguments)
