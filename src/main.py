import time
import mannco_manitor
import skinport_monitor
import Selenium_Config

while True:
    selenium_config = Selenium_Config.Selenium_Config()
    skinport_monitor.run(selenium_config)
    time.sleep(5)
    mannco_manitor.run(selenium_config)
    selenium_config.quit_session()