import sys
import os
from plyer import notification  #For getting notification
import requests
from notification_system.logger.log import logging
from notification_system.exception.exception_handler import AppException
from notification_system.config.configuration import AppConfiguration


class NotificationSystem:
    """
    NotificationSystem is a class 
    It contains all the functionality needed to send notification 
    """

    def __init__(self, app_config = AppConfiguration()):
        """
        Initiate the NotificationSystem class
        """
        try:
            self.templates_config = app_config.get_templates_config()
            self.notification_config = app_config.get_notification_config()
            logging.info("Initializing NotificationSystem")
        except Exception as e:
            raise AppException(e, sys) from e


    
    def getData(self,url):
        try:
            r= requests.get(url)
            return r.text
        except Exception as e:
            raise AppException(e, sys) from e

    
    # This function will give me the notification
    def notifyMe(self,title,message):
        try:
            notification.notify(
                title = title,
                message = message,
                app_icon = os.path.join(self.templates_config.icon_dir, self.templates_config.icon_name),
                timeout = 5)
        
        except Exception as e:
            raise AppException(e, sys) from e

