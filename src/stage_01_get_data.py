import argparse
from distutils.file_util import copy_file
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories,copy_files
import random


STAGE = "STAGE_NAME" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def get_data(config_path):
    ## read config files
    config = read_yaml(config_path)
    source_download_dirs=config["source_download_dirs"]
    local_data_dirs=config["local_data_dirs"]
    for source_download_dir,local_data_dir in tqdm(zip(source_download_dirs,local_data_dirs),total=2,desc="list of folders",colour="red"):
        create_directories([local_data_dir])
        copy_files(source_download_dir,local_data_dir)
    
    


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(">>>>> stage one started <<<<<")
        get_data(config_path=parsed_args.config)
        logging.info(
            ">>>>> stage one completed! all the data are saved in local <<<<<\n"
        )
    except Exception as e:
        logging.exception(e)
        raise e