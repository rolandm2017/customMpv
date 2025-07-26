import os
os.environ["PATH"] = r"C:\Users\rlm\Downloads\mpv-x86_64-20250720-git-440f35a" + os.pathsep + os.environ["PATH"]

import mpv


MPV_PATH = r"C:\Users\rlm\Downloads\mpv-x86_64-20250720-git-440f35a\mpv.exe"  # <= replace with your actual mpv.exe path
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


# Press K to mark the end of a subtitle. Splits the subtitle in two, 
# donating the end piece to the next subtitles.

# TODO: User can press <something> to ... retry? try again? what UI?

# The fixer adjusts the timestamps up to and including the spike. Saves edits. Merges into main SRT.

# SRT has:
#   - original file, never changes, read-only.
#   - segment file, the SRT of the segment.
#   - Updated file, where changes are merged into.

# GOAL: I'd like to be able to use this on LOST! And Soon!