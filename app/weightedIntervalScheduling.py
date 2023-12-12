from datetime import datetime


def sort_by_finish_time(tasks):
    sorted_tasks = sorted(tasks[1:], key=lambda task: task[1])
    return [tasks[0]] + sorted_tasks


def largest_compatible_indices(sorted_tasks, n):
    p = [0] * n

    for j in range(1, n): # [h_inicio, h_fim, peso]
        for i in range(j - 1, 0, -1):
            if sorted_tasks[i][1] <= sorted_tasks[j][0]:  
                p[j] = i
                break
    return p


def iterative_compute_opt(sorted_tasks, n, p):
    m = [0] * (n + 1)

    for i in range(1, n + 1):
        p_index = p[i - 1] if p[i - 1] is not None else 0
        m[i] = max(sorted_tasks[i-1][2] + m[p_index], m[i-1])

    return m


def find_solution(n):
    if n == 0:
        return None
    
    p_index = p[n] if p[n] is not None else 0

    if sorted_tasks[n][2] + m[p_index] > m[n-1]:
        scheduled_tasks.append(sorted_tasks[n])
        find_solution(p_index)
    else:
        find_solution(n-1)

# tasks = [ # [h_inicio, h_fim, peso]
#     [0,0,0],
#     [datetime(2023, 12, 11, 8, 30), datetime(2023, 12, 11, 12, 0), 3],
#     [datetime(2023, 12, 11, 9, 0), datetime(2023, 12, 11, 10, 30), 2],
#     [datetime(2023, 12, 11, 10, 30), datetime(2023, 12, 11, 12, 30), 4],
#     [datetime(2023, 12, 11, 12, 0), datetime(2023, 12, 11, 13, 0), 5],
#     [datetime(2023, 12, 11, 10, 0), datetime(2023, 12, 11, 16, 30), 2],
#     [datetime(2023, 12, 11, 11, 30), datetime(2023, 12, 11, 13, 30), 3],
#     [datetime(2023, 12, 11, 15, 30), datetime(2023, 12, 11, 17, 0), 4],
#     [datetime(2023, 12, 11, 16, 0), datetime(2023, 12, 11, 18, 0), 5],
#     [datetime(2023, 12, 11, 15, 0), datetime(2023, 12, 11, 19, 0), 3],
#     [datetime(2023, 12, 11, 18, 30), datetime(2023, 12, 11, 20, 0), 2],
# ]
# scheduled_tasks = []

# n = len(tasks)
# sorted_tasks = sort_by_finish_time(tasks)
# p = largest_compatible_indices(sorted_tasks, n)
# m = iterative_compute_opt(sorted_tasks, n, p)

# find_solution(n-1)
# print("Scheduled Task: ")
# print(scheduled_tasks)

