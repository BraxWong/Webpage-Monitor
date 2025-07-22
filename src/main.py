import time
import mannco_manitor
import skinport_monitor
import Selenium_Config

selenium_config = Selenium_Config.Selenium_Config()
while True:
    try:
        skinport_monitor.run(selenium_config)
        time.sleep(5)
        mannco_manitor.run(selenium_config)
    except Exception as e:
        print(f"Program has been terminated. Error Message: {e}")
        selenium_config.quit_session()
        break