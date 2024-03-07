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

CHANNELS_COUNT = int(config["DEFAULT"]["CHANNELS_COUNT"])
STRATEGY = int(config["DEFAULT"]["STRATEGY_INDEX"])
FAKE_MSG = config["DEFAULT"]["FAKE_MSG"]


class FoxStrategyPicker:
    MAX_FOX = 0
    OPTIMAL_FOX = 1

    def __init__(self,real_msg,img_carrier):
        match STRATEGY:
            case self.MAX_FOX:
                self.real_Count = 3
                self.fake_count = 6
                self.empty_count = 0
                self.protocol_length = 3
                self.__max_fox(real_msg,img_carrier)
            
            case self.OPTIMAL_FOX:
                self.real_Count = 6
                self.fake_count = 6
                self.empty_count = 6
                self.protocol_length = 6
                self.__optimal_fox(real_msg,img_carrier)
            
    def __optimal_fox(self,real_msg,img_Carrier):
        reals = split_encode(real_msg, img_Carrier, self.real_Count)
        fakes = split_encode(FAKE_MSG, img_Carrier, self.fake_count)
        empty = make_empty(img_Carrier)
        self.msgs = [[None for _ in range(CHANNELS_COUNT)] for _ in range(self.protocol_length)]
        for i in range(self.protocol_length):
            loc = [REAL,EMPTY,FAKE]
            random.shuffle(loc)
            self.msgs[i][loc[REAL]] = EncodedMSG(reals[i], Entity.REAL)
            self.msgs[i][loc[FAKE]] = EncodedMSG(fakes[i], Entity.FAKE)
            self.msgs[i][loc[EMPTY]] = EncodedMSG(empty, Entity.EMPTY)

    def __max_fox(self,real_msg,img_carrier):
        reals = split_encode(real_msg, img_carrier, self.real_Count)
        fakes = split_encode(FAKE_MSG, img_carrier, self.fake_count)
        reals_loc = random.sample(range(CHANNELS_COUNT), self.real_Count)
        self.msgs = [[None for _ in range(CHANNELS_COUNT)] for _ in range(self.protocol_length)]
        for i in range(self.protocol_length):
            self.msgs[i][reals_loc[i]] = EncodedMSG(reals[i], Entity.REAL)

        fake_filling_i = 0

        for i in range(self.protocol_length):
            for j in range(CHANNELS_COUNT):
                if self.msgs[i][j] == None:
                    self.msgs[i][j] = EncodedMSG(fakes[fake_filling_i], Entity.FAKE)
                    fake_filling_i += 1

        assert fake_filling_i == self.fake_count

        
        