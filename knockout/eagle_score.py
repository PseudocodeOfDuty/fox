class EagleScore:

    @staticmethod
    def calc(alpha_e,t=0,j=1):
        return (0.7 * j - 0.3 / 213 * t + 0.3) * (1 + 0.2 * alpha_e) * 60
    
    @staticmethod
    def calc_alpha(f_dodged,infakes,r_missed=0,inreals=1):
        return f_dodged/infakes - r_missed/inreals if infakes else 0
    
    @staticmethod
    def calc_jaccard(true_msg, test_msg):
        intersection = sum(min(true_msg.count(elem), test_msg.count(elem)) for elem in set(true_msg + test_msg))
        union = sum(max(true_msg.count(elem), test_msg.count(elem)) for elem in set(true_msg + test_msg))
        j = intersection / union if union != 0 else 0
        return j