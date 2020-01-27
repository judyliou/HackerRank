# Solution 1
def minTime(machines, goal):
    make = [1.0/x for x in machines]
    lower_bound = int(goal / sum(make)) - 1
    upper_bound = lower_bound + max(machines) + 1

    while lower_bound < upper_bound:
        print(lower_bound, upper_bound)
        day = (lower_bound + upper_bound) // 2
        product = sum([day // i for i in machines])
        if product >= goal:
            upper_bound = day 
        elif product < goal:
            lower_bound = day + 1
    return lower_bound   
    
# Solution 2    
def minTime(machines, goal):
    make = [1.0/x for x in machines]
    lower_bound = int(goal / sum(make)) - 1
    upper_bound = lower_bound + max(machines) + 1

    while True:
        if sum([lower_bound // i for i in machines]) >= goal:
            return lower_bound
        lower_bound += 1
