# Nao-DanceFreezePy

Program for Jaclyn's Masters Thesis 2016-2017

Nao dances to songs that stop periodically. When the music stops, Nao freezes in place. This version is in Python to be run remotely and for easier logging. It includes the animations, plays the audio, and logs start/stop times. Turn autonomous life off using Nao's web interface before running the program or else Nao will move during the pauses.

## Installation
Requires naoqi Python SDK available from Softbank Robotics and docopt available via pip. As with all naoqi Python programs at this point, requires Python 2.7 and is not compatible with Python 3+.

Music files need to be split into clips manually and the files transfered to Nao in the directory "/var/persistent/home/nao/dancefreeze/music/". The original files can be found at:

- <http://freekidsmusic.com/traditional-childrens-songs/a-tisket-a-tasket/>
- <http://freekidsmusic.com/traditional-childrens-songs/twinkle-twinkle-little-star/>
- <https://musopen.org/music/2777/frederic-chopin/berceuse-op-57/>
- <https://musopen.org/music/3039/scott-joplin/harmony-club-waltz/>

Freekidsmusic.com songs are performances of public domain works used with permission of the artists. Musopen.org songs are public domain performances of public domain works. 

Once all dependencies are installed, clone the repository and run from the command line.

## Usage
	python robotdf.py ROBOT_IP SONG
	py -2.7 robotdf.py ROBOT_IP SONG
	robotdf.py (-h | --help)

Use the py -2.7 style command on Windows to specify running with Python 2.7.

Songs are abbreviated to berceuse, tisket, twinkle, and waltz.

## Authors
Developed for the Mind Music Machine Lab @ Michigan Tech, for more details see https://trim.mtu.edu. Email addresses (in parentheses) end in @mtu.edu unless otherwise specified.

Jaclyn Barnes, Lead Developer (jaclynb)

Myounghoon "Philart" Jeon, Lab Director (mjeon)


## Legal

Copyright (C) 2018 Michigan Technological University

Licensed under GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.html)