import sys
import time
from bs4 import BeautifulSoup 
from notification_system.logger.log import logging
from notification_system.exception.exception_handler import AppException
from notification_system.component.logics import NotificationSystem
from notification_system.config.configuration import AppConfiguration

class NotificationEngine:
    def __init__(self,app_config = AppConfiguration()):
        try:
            self.notification_obj = NotificationSystem()
            self.notification_config = app_config.get_notification_config()
            logging.info("Starting Notification System engine")
        except Exception as e:
            raise AppException(e, sys) from e

    
    def start(self):
        try:
            myHtmlData = self.notification_obj.getData(self.notification_config.covid_data_url)
            soup = BeautifulSoup( myHtmlData, 'html.parser')
            mystr = ""
            for tr in soup.find_all('tbody')[0].find_all('tr'):
                mystr += tr.get_text()
            itemlist= mystr.split('\n\n')
            
            lis = []
            for item in itemlist[106:108]:
                new = item
                lis.append(new)
            print(lis)
            logging.info(f"Case of COVID-19: {lis}")
            nTittle = "Case of COVID-19"
            nText = f"{lis[0]}: {lis[1]}"
            
            self.notification_obj.notifyMe(nTittle,nText)
            time.sleep(20)
        except Exception as e:
            raise AppException(e, sys) from e


if __name__ == "__main__":
    obj = NotificationEngine()
    while True:
        obj.start()

        