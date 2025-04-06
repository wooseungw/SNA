import alive_progress

import time

def progress_bar():
    with alive_progress.alive_bar(100) as bar:
        for i in range(100):
            time.sleep(0.1)
            bar()
    print("Progress bar completed!")
progress_bar()