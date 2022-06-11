class Exception:
    def checkScore(self, score):
        for sc in score:
            if not (0 <= sc <= 100):
                raise Exception("Score must be 0 <= n <= 100")
    
    def checkInput(self, n, k):
        if not (1 <= k <= n <= 50):
            raise ValueError("[INPUT ERROR]:\nInput must be 1 <= k <= n <= 50\n") 
    
    def checkScoreOrder(self, score):
        for i in range(len(score) - 1):
            if score[i+1] > score[i]:
                raise ValueError("\n\n[INPUT ERROR] Given score must in non-increasing order. As the score[i] represents the contestant i-th place")