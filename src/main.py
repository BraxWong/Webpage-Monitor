import time
import mannco_manitor
import skinport_monitor

while True:
    mannco_manitor.run()
    time.sleep(5)
    skinport_monitor.run()