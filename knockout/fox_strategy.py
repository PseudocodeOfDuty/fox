from eagle_score import EagleScore

class FoxIteration:
    def __init__(self,r,f,e):
        self.r = r
        self.f = f
        self.e = e

class FoxStrategy:
    def __init__(self):
        self.__fs = []
        self.__len = 0
        self.__fakes = 0
        self.__infakes = 0
        self.__alpha = 0

    def add_itr(self,r,f,e):
        self.__fs.append(FoxIteration(r,f,e))
        self.__len += 1
        self.__fakes += f
        rf_sum = r + f
        self.__alpha += rf_sum / (rf_sum + e)
        if f>0:
            self.__infakes += 1
    
    def __calc_beta_fox(self):
        return 19 / 60 * self.__fakes - self.__fakes * self.__fakes / 36
    
    def calc_fox_score(self,t,b=14):
        beta = self.__calc_beta_fox()
        return 16 * self.__alpha / self.__len + 12 * beta + 0.2 * b - 0.04 * t + 8
    
    def calc_eagle_superscore(self):
        alpha_e = EagleScore.calc_alpha(self.__fakes,self.__infakes)
        return EagleScore.calc(alpha_e)
    
    def calc_linear_programming_score(self,t_fox,b_fox):
        return self.calc_fox_score(t_fox,b_fox) - self.calc_eagle_superscore()

#Optimal
# fs = FoxStrategy()
# for i in range(6):
#     fs.add_itr(1,1,1)
# t = 6.172 + 0.42 * 6
# print(fs.calc_fox_score(t))
# print(fs.calc_eagle_superscore())