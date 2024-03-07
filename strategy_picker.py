from fox_data.fox_messaging_classes import *
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

class FoxStrategyPicker:
    MAX_FOX = 0
    OPTIMAL_FOX = 1

    def __init__(self,reals,fakes,empty):
        match STRATEGY:
            case self.MAX_FOX:
                return self.__max_fox(reals,fakes)
            
            case self.OPTIMAL_FOX:
                return self.__optimal_fox(reals,fakes,empty)
            
    def __optimal_fox(self,reals,fakes,empty):
        msgs = [[None for _ in range(CHANNELS_COUNT)] for _ in range(PROTOCOL_LENGTH)]

        for i in range(PROTOCOL_LENGTH):
            loc = [REAL,EMPTY,FAKE]
            random.shuffle(loc)
            msgs[i][loc[REAL]] = EncodedMSG(reals[i], Entity.REAL)
            msgs[i][loc[FAKE]] = EncodedMSG(fakes[i], Entity.FAKE)
            msgs[i][loc[EMPTY]] = EncodedMSG(empty, Entity.EMPTY)
        
        return msgs