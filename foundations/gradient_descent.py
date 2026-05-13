class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        res = init
        
        for i in range(iterations):
            delta = 2 * res
            res -= learning_rate * delta

        return round(res, 5)