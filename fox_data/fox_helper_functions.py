from LSBSteg import encode

def split_encode(msg,img,chunks_count):
    def is_last_chunk(i):
        return i==chunks_count-1
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