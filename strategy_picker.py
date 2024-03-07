from fox_data.fox_messaging_classes import *
from fox_data.fox_helper_functions import split_encode,make_empty
import configparser
import random

REAL = 0
FAKE = 1
EMPTY = 2

CONFIG_PATH = "fox_config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

PROTOCOL_LENGTH = int(config["DEFAULT"]["PROTOCOL_LENGTH"])
CHANNELS_COUNT = int(config["DEFAULT"]["CHANNELS_COUNT"])
STRATEGY = int(config["DEFAULT"]["STRATEGY_INDEX"])
FAKE_MSG = config["DEFAULT"]["FAKE_MSG"]
REAL_CHUNKS_COUNT = int(config["DEFAULT"]["REAL_CHUNKS_COUNT"])
FAKE_CHUNKS_COUNT = int(config["DEFAULT"]["FAKE_CHUNKS_COUNT"])
EMPTY_CHUNKS_COUNT = int(config["DEFAULT"]["EMPTY_CHUNKS_COUNT"])

class FoxStrategyPicker:
    MAX_FOX = 0
    OPTIMAL_FOX = 1

    def __init__(self,real_msg,img_carrier):
        match STRATEGY:
            case self.MAX_FOX:
                self.__max_fox(real_msg,img_carrier)
            
            case self.OPTIMAL_FOX:
                self.__optimal_fox(real_msg,img_carrier)
            
    def __optimal_fox(self,real_msg,img_Carrier):
        reals = split_encode(real_msg, img_Carrier, REAL_CHUNKS_COUNT)
        fakes = split_encode(FAKE_MSG, img_Carrier, FAKE_CHUNKS_COUNT)
        empty = make_empty(img_Carrier)
        self.msgs = [[None for _ in range(CHANNELS_COUNT)] for _ in range(PROTOCOL_LENGTH)]
        for i in range(PROTOCOL_LENGTH):
            loc = [REAL,EMPTY,FAKE]
            random.shuffle(loc)
            self.msgs[i][loc[REAL]] = EncodedMSG(reals[i], Entity.REAL)
            self.msgs[i][loc[FAKE]] = EncodedMSG(fakes[i], Entity.FAKE)
            self.msgs[i][loc[EMPTY]] = EncodedMSG(empty, Entity.EMPTY)
        
        