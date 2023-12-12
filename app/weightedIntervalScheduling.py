from datetime import datetime

from datetime import datetime

class WeightedIntervalScheduling:
    def __init__(self):
        self.scheduled_tasks = []
        self.p = []
        self.m = []

    def sort_by_finish_time(self, tasks):
        sorted_tasks = sorted(tasks[1:], key=lambda task: task[1])
        return sorted_tasks

    def largest_compatible_indices(self, sorted_tasks, n):
        self.p = [0] * (n + 1)

        for j in range(2, n): # [h_inicio, h_fim, peso]
            for i in range(j - 1, 0, -1):
                if sorted_tasks[i][1] <= sorted_tasks[j][0]:  
                    self.p[j] = i
                    break

    def iterative_compute_opt(self, sorted_tasks, n):
        self.m = [0] * (n + 1)

        for i in range(1, n+1):
            self.m[i] = max(sorted_tasks[i][2] + self.m[self.p[i - 1]], self.m[i-1])

    def find_solution(self, n, sorted_tasks):
        if n == 0:
            return None
        
        if sorted_tasks[n][2] + self.m[self.p[n]] > self.m[n-1]:
            self.scheduled_tasks.append(sorted_tasks[n])
            self.find_solution(self.p[n], sorted_tasks)
        else:
            self.find_solution(n-1, sorted_tasks)

