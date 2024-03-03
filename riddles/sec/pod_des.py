from riddles.sec.sec_utils import *
from riddles.sec.pod_des_tables import DES_T


class SingleBlockDES:
    DES = DES_T()

    def encrypt(self, key, block):
        bit_key = bytes_to_bits(key)
        K = self.__gen_subkeys(bit_key)
        bit_block = bytes_to_bits(block)
        block = self.__P(bit_block, self.DES.IP_64T)
        L = block[:32]
        R = block[32:]
        for cur_byte in range(16):
            ogR = R[:]
            R = self.__P(R, self.DES.EXP_48T)
            R = xor(R, K[cur_byte])
            C = self.__sbox_logic(R)
            R = self.__P(C, self.DES.P_32T)
            R = xor(R, L)
            L = ogR
        cipher = self.__P(R + L, self.DES.FP_64T)
        return hexer(cipher)

    def __P(self, block, table):
        return [block[i] for i in table]

    def __gen_subkeys(self, key):
        K = [[0] * 48] * 16
        key = self.__P(key, self.DES.P_56T)
        cur_byte = 0
        L = key[:28]
        R = key[28:]
        for cur_byte in range(16):
            L = circular_shift(L, self.DES.LR_16T[cur_byte])
            R = circular_shift(R, self.DES.LR_16T[cur_byte])
            K[cur_byte] = self.__P(L + R, self.DES.P_48T)
        return K

    def __sbox_logic(self, data):
        C = []
        B = [data[i : i + 6] for i in range(0, len(data), 6)]
        for cur_bit in range(8):
            m = (B[cur_bit][0] << 1) + B[cur_bit][5]
            n = (
                (B[cur_bit][1] << 3)
                + (B[cur_bit][2] << 2)
                + (B[cur_bit][3] << 1)
                + B[cur_bit][4]
            )
            v = self.DES.S_BOXSET[cur_bit][(m << 4) + n]
            C.extend([(v >> i) & 1 for i in range(3, -1, -1)])
        return C
