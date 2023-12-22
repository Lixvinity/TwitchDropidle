import webbrowser
import time
import subprocess

# Define your links and corresponding times
links = ["https://www.twitch.tv/TWITCHCHANNELLINK", "https://www.twitch.tv/TWITCHCHANNELLINK", "https://www.twitch.tv/TWITCHCHANNELLINK"]
times = ["19:45", "21:46", "23:48"]

# Convert times to seconds since midnight
time_seconds = [int(h) * 3600 + int(m) * 60 for h, m in (t.split(':') for t in times)]


while True:
    current_time = time.strftime("%H:%M")
    print ("Working")
    if current_time in times:
        index = times.index(current_time)
        url_to_open = links[index]

        # Kill the browser process
        subprocess.run(["taskkill", "/f", "/im", "firefox.exe"])


        # Open the link
        webbrowser.open(url_to_open)
        print(f"Opened {url_to_open} at {current_time}")


    # Sleep for a short interval to avoid high CPU usage
    time.sleep(15)  # Adjust the sleep interval as needed
