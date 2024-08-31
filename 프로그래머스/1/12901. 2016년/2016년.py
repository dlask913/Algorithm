def solution(a, b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    endDay = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    day = 0
    for month in range(a):
        day += endDay[month]
    return week[(day + b - 1) % 7]