# -*- encoding: UTF-8 -*-

"""
Usage:
  berceuse.py ROBOT_IP SONG
  berceuse.py (-h | --help)
Options:
  -h, --help
"""

from naoqi import ALProxy
from docopt import docopt
import logging
import logging.config
import datetime
import time

songparts =  {'Berceuse': 5,
              'Tisket': 5,
              'Twinkle': 5,
              'Waltz': 4}

songlength = {'Berceuse': [11, 9, 14, 7, 7],
              'Tisket': [18, 14, 14, 12, 13],
              'Twinkle': [7, 5, 10, 5, 10], 
              'Waltz': [10, 8, 13, 12]}

pauses =    {'Berceuse': [3, 2, 4, 2],
             'Tisket': [3, 3, 2],
             'Twinkle': [2, 1, 3, 2],
             'Waltz': [3, 2, 4]}

def setuplogging():
    logger = logging.getLogger("humandf")
    logger.setLevel(logging.INFO)
 
    # create the logging file handler
    now = datetime.datetime.now()
    log_filename = "log\\robotdf_" + now.strftime('%Y_%m_%d_%H_%M_%S') + ".log"
    fh = logging.FileHandler(log_filename)
 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
  if (robotIP == None):
    robotIP = "127.0.0.1"

  port = 9559

  song = arguments.pop("SONG", None)
  if (song == None):
    sys.exit("Need song argument")

  audio = ALProxy("ALAudioPlayer", robotIP, port)
  motion = ALProxy("ALMotion", robotIP, port)
  posture = ALProxy("ALRobotPosture", robotIP, port)

  motion.wakeUp()
  posture.goToPosture("StandInit", 0.5)

  for i in range(songparts[song]):
    songfile = "/var/persistent/home/nao/dancefreeze/music/" + song + str(i+1) + ".wav"
    logger.info("Start " + song + str(i+1))
    audio.playFile(songfile)
    logger.info("End " + song + str(i+1))
    if (i < len(pauses[song])):
      time.sleep(pauses[song][i])
      logger.info("Pause of " + str(pauses[song][i]) + " secs")

  posture.goToPosture("StandInit", 0.5)
  motion.rest()

if __name__ == "__main__":
  arguments = docopt(__doc__)

  main(arguments)