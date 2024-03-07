class FoxCSPSolution:
    def __init__(self,solution,score,n):
        self.__solution = solution
        self.__score = score
        self.__n = n

    def __str__(self) -> str:
        return f"Best till now: n = {self.__n}, score = {self.__score}\n{self.__solution}"

    def get_solution(self):
        return self.__solution
    
    def get_score(self):
        return self.__score
    
    def keep_if_higher_score_than(self,other_fcsp):
        if other_fcsp is None:
            return self
        if self.__score > other_fcsp.get_score():
            return self
        return other_fcsp