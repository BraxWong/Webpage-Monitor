import time
import mannco_manitor
import skinport_monitor

while True:
    skinport_monitor.run()
    time.sleep(5)
    mannco_manitor.run()