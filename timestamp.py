from python_mpv_jsonipc import MPV
import asyncio

# === CONFIGURATION ===
MPV_PATH = r"C:\mpv-x86_64\mpv.exe"  # <= replace with your actual mpv.exe path
VIDEO_PATH = r"C:\Users\rlm\Videos\hazy\Hazy - Awake.webm"  # <= replace with your video

# === SCRIPT ===
async def main():
    mpv = MPV(mpv_location=MPV_PATH)

    # Set up keybind: J sends a message we can catch
    # mpv.command("define-key", "J", "script-message report-time")
    # mpv.command("script-binding", "bind J script-message report-time")

    # Listen for the keybind
    @mpv.on_event('client-message')
    def on_message(event):
        if event.args and event.args[0] == 'report-time':
            timestamp = mpv.time_pos
            print(f"J key pressed at: {format_time(timestamp)}")

    # Load the video
    mpv.command("loadfile", VIDEO_PATH)

    # Keep the script alive
    while True:
        await asyncio.sleep(1)

def format_time(seconds):
    if seconds is None:
        return "unknown"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02}:{m:02}:{s:02}"

if __name__ == "__main__":
    asyncio.run(main())
