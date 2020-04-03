import bisect

def memoizedtopdown(x):
    if (x == 0):
        return 0
    elif (M[x] > 0):
        return M[x]
    else:
        M[x] = max((s_priority[x] + memoizedtopdown(p[x])), memoizedtopdown(x - 1))
        return M[x]


def bottomup(y):
    M[0] = 0
    for j in range(1, y + 1):
        M[j] = max(s_priority[j] + M[(p[j])], M[j - 1])
    return M[j]


def backtrack(M, j):
    if (j > 0):
        if (s_priority[j] + M[p[j]] >= M[j - 1]):
            solution_set.append(s_interval[j])
            backtrack(M, p[j])
        else:
            backtrack(M, j - 1)
    return solution_set


def bubblesort(interval_no, starting_time, finishing_time, priority_value):
    for i in range(len(finishing_time)):
        for j in range(len(finishing_time) - i - 1):
            if finishing_time[i] > finishing_time[i + 1]:
                interval_no[i], interval_no[i + 1] = interval_no[i + 1], interval_no[i]
                starting_time[i], starting_time[i + 1] = starting_time[i + 1], starting_time[i]
                finishing_time[i], finishing_time[i + 1] = finishing_time[i + 1], finishing_time[i]
                priority_value[i], priority_value[i + 1] = priority_value[i + 1], priority_value[i]
    return interval_no, starting_time, finishing_time, priority_value


print("Select Mode")
print("1. Top-Down Memoized Algorithm")
print("2. Bottom-Up Algorithm")
mode = input("Mode: ")

file1 = open("WIZ.txt", 'r')
items = file1.readlines()
interval_no = []
starting_time = []
finishing_time = []
priority_value = []

i = 0;
for x in items:
    temp = x.split()
    print(temp)
    interval_no.insert(i, int(temp[0]))
    starting_time.insert(i, int(temp[1]))
    finishing_time.insert(i, int(temp[2]))
    priority_value.insert(i, int(temp[3]))
    i = i + 1

bubblesort(interval_no, starting_time, finishing_time, priority_value)

print("Select your activities")
activities = input("Activities: ")
s_activities_str = activities.split()
s_activities_int = []
for i in range(len(s_activities_str)):
    s_activities_int.insert(i, int(s_activities_str[i]))

s_interval = [0]
s_start = [0]
s_end = [0]
s_priority = [0]
M = [0]
for i in range(len(s_activities_int)):
    for j in range(len(interval_no)):
        if (s_activities_int[i] == interval_no[j]):
            s_interval.insert(i + 1, interval_no[j])
            s_start.insert(i + 1, starting_time[j])
            s_end.insert(i + 1, finishing_time[j])
            s_priority.insert(i + 1, priority_value[j])
            M.insert(i + 1, -1)

bubblesort(s_interval, s_start, s_end, s_priority)

p = []

for i in range(len(s_interval)):
    index = bisect.bisect(s_end, s_start[i]) - 1
    p.append(index)

z = len(s_interval)

# Used in Backtrack Solution Function
solution_set = []

if (mode == '1'):
    print("Initiating Top-Down Memoized Algorithm")
    print("Final Weight: ")
    print(memoizedtopdown(z - 1))
    print("Solution set: ")
    print(backtrack(M, z - 1))
elif (mode == '2'):
    print("Initiating Bottom-Up Algorithm")
    print("Final Weight: ")
    print(bottomup(z - 1))
    print("Solution set: ")
    print(backtrack(M, z - 1))
else:
    print("Wrong Mode")