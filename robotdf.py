# -*- encoding: UTF-8 -*-

"""
Usage:
  robotdf.py ROBOT_IP SONG
  robotdf.py (-h | --help)
Options:
  -h, --help
"""

from naoqi import ALProxy
from docopt import docopt
import logging
import logging.config
import datetime
import time

import berceuseDance
import tisketDance
import twinkleDance
import waltzDance

berceuse = berceuseDance.berceuse
tisket = tisketDance.tisket
twinkle = twinkleDance.twinkle
waltz = waltzDance.waltz


def setuplogging():

    logger = logging.getLogger("robotdf")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    now = datetime.datetime.now()
    log_filename = "log\\robotdf_" + now.strftime('%Y_%m_%d_%H_%M_%S') + ".log"
    fh = logging.FileHandler(log_filename)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    return (logger)


def main(arguments):
    """
    Play and log music for human Dance Freeze
    """

    logger = setuplogging()

    robotIP = arguments.pop("ROBOT_IP", None)
    if (robotIP is None):
        robotIP = "127.0.0.1"

    port = 9559

    song = arguments.pop("SONG", None)
    if (song is None):
        sys.exit("Need song argument")

    if (song == "Berceuse"):
        songObj = berceuse
    elif (song == "Tisket"):
        songObj = tisket
    elif (song == "Twinkle"):
        songObj = twinkle
    elif (song == "Waltz"):
        songObj = waltz
    else:
        sys.exit("Invalid song name")

    audio = ALProxy("ALAudioPlayer", robotIP, port)
    motion = ALProxy("ALMotion", robotIP, port)
    posture = ALProxy("ALRobotPosture", robotIP, port)

    motion.wakeUp()
    posture.goToPosture("Stand", 0.8)

    for i in range(songObj.get_num_parts()):
        songfile = "/var/persistent/home/nao/dancefreeze/music/" + \
            songObj.get_song_name() + str(i + 1) + ".wav"
        logger.info("Start " + songObj.get_song_name() + str(i + 1))
        audio.post.playFile(songfile)
        motion.angleInterpolation(songObj.get_part(i).get_names(),
                                  songObj.get_part(i).get_keys(),
                                  songObj.get_part(i).get_times(), True)
        logger.info("End " + songObj.get_song_name() + str(i + 1))
        time.sleep(songObj.get_part(i).get_pause_length())

    posture.goToPosture("Stand", 0.8)

if __name__ == "__main__":
    arguments = docopt(__doc__)

    main(arguments)
