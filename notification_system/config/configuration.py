import os
import sys
from notification_system.logger.log import logging
from notification_system.utils.util import read_yaml_file
from notification_system.exception.exception_handler import AppException
from notification_system.entity.config_entity import TemplatesConfig, NotificationConfig


ROOT_DIR = os.getcwd()
# Main config file path
CONFIG_FOLDER_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_FOLDER_NAME,CONFIG_FILE_NAME)


class AppConfiguration:
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH):
        try:
            self.configs_info = read_yaml_file(file_path=config_file_path)
        except Exception as e:
            raise AppException(e, sys) from e

    
    def get_templates_config(self) -> TemplatesConfig:
        try:
            templates_config = self.configs_info['templates_config']
            templates_dir = templates_config['templates_dir']

            icon_dir = os.path.join(templates_dir, templates_config['icon_dir'])
            icon_name = templates_config['icon_name']

            response = TemplatesConfig(
                icon_dir = icon_dir,
                icon_name = icon_name,
            )

            logging.info(f"Templates config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e

    

    def get_notification_config(self) -> NotificationConfig:
        try:
            notification_config = self.configs_info['notification_configuration']

            covid_data_url = notification_config['covid_data_url']

            response = NotificationConfig(
                covid_data_url = covid_data_url,
            )

            logging.info(f"Notification config: {response}")
            return response

        except Exception as e:
            raise AppException(e, sys) from e

    


