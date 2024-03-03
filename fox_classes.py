from LSBSteg import decode

class Entity:
    FAKE = 'F'
    REAL = 'R'
    EMPTY = 'E'
    POOL = ["F","R","E"]

    @staticmethod
    def check(e):
        return e in Entity.POOL
    
class EncodedMSG:

    def __init__(self,msg,entity):
        assert Entity.check(entity)
        self.__msg = msg
        self.__entity = entity

    def msg(self):
        return self.__msg
    
    def entity(self):
        return self.__entity
    
    def serialize(self):
        print(f"{decode(self.__msg)} | {self.__entity}")

    @staticmethod
    def extractMSGs(channel_msgs):
        return [cm.msg() for cm in channel_msgs]
    
    @staticmethod
    def extractEntities(channel_msgs):
        return [cm.entity() for cm in channel_msgs]