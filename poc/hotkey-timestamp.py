#!/usr/bin/env python3
"""
MPV Timestamp Hotkey Script
Adds F10 hotkey to MPV that prints current timestamp when pressed.

TODO
Need this because, I must be able to press a hotkey, and,
get the current timestamp to START recording audio, and again to END recording audio.

TODO
I also must press hotkey to grab a screenshot.

TODO
I must also get the subtitles going
"""

import os
os.environ["PATH"] = r"C:\Users\rlm\Downloads\mpv-x86_64-20250720-git-440f35a" + os.pathsep + os.environ["PATH"]

import mpv

MPV_PATH = r"C:\mpv-x86_64\mpv.exe"  # <= replace with your actual mpv.exe path
# MPV_PATH = r"C:\Users\rlm\Downloads\mpv-x86_64-20250720-git-440f35a\mpv.exe"  # <= replace with your actual mpv.exe path
VIDEO_PATH = r"C:\Users\rlm\Videos\hazy\Hazy - Awake.webm"  # <= replace with your video


player = mpv.MPV()

@player.on_key_press('k')
def on_j():
    timestamp = player.time_pos  # time_pos gives the current timestamp in seconds
    # Format timestamp as HH:MM:SS or as you wish
    # Send/use the timestamp as needed
    print(f'K pressed at {timestamp:.2f}s')

player.play(VIDEO_PATH)

player.wait_for_playback()