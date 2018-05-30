# Nao Dance Freeze Python

Program for Jaclyn's Masters Thesis 2016-2017

Nao dances to songs that stop periodically When the music stops, Nao freezes in place. This version is in Python to be run remotely and for easier logging. It includes the animations, plays the audio, and logs start/stop times. Turn autonomous life off using Nao's web interface before running the program or else Nao will move during the pauses.

Usage: berceuse.py ROBOT_IP SONG berceuse.py (-h | --help) Options: -h, --help

Songs are abbreviated to Berceuse, Tisket, Twinkle, and Waltz.

Music files need to be split into clips manually. The original files can be found at:

- <http://freekidsmusic.com/traditional-childrens-songs/a-tisket-a-tasket/>
- <http://freekidsmusic.com/traditional-childrens-songs/twinkle-twinkle-little-star/>
- <https://musopen.org/music/2777/frederic-chopin/berceuse-op-57/>
- <https://musopen.org/music/3039/scott-joplin/harmony-club-waltz/>
