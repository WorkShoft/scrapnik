import time
import progressbar

widgets=[
    ' [', progressbar.Timer(), '] ',
    progressbar.Bar(),
    ' (', progressbar.ETA(), ') ',
]
for i in progressbar.progressbar(range(20), widgets=widgets):
    time.sleep(0.1)
