from LSBSteg import decode,encode

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
        return [cm.msg().tolist() for cm in channel_msgs]
    
    @staticmethod
    def extractEntities(channel_msgs):
        return [cm.entity() for cm in channel_msgs]
    
def split_encode(msg, img, chunks_count):
    def is_last_chunk(i):
        return i == chunks_count - 1

    chunk_len = len(msg) // chunks_count
    encoded_chunks = []
    for i in range(chunks_count):
        if is_last_chunk(i):
            msg_chunk = msg[i * chunk_len :]
        else:
            msg_chunk = msg[i * chunk_len : (i + 1) * chunk_len]
        img_copy = img.copy()
        encoded_chunks.append(encode(img_copy, msg_chunk))
    return encoded_chunks

def make_empty(img):
    img_copy = img.copy()
    return encode(img_copy,"")