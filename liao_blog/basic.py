#!/usr/local/bin
# coding=utf-8

#score increase rate
s1 = 72
s2 = 85
r = (s2 -s1)/s1
#from ipdb import set_trace
#set_trace()
print('%.1f%%' %(r*100))

hight = 1.75
weight = 80.5
BMI = weight/(hight**2)
print('%.1f' %BMI)

def update_highest_index(subj, score, index):
    global highest_index
    if highest_index[subj][0] < score:
        highest_index[subj][0] = score
        highest_index[subj][1] = index

number = int(input('Please input the student number:'))
all = number
info_ls = []
while number > 0:
    info_ls.append(input().split())
    number -= 1
print(info_ls)
avg_scores = [0, 0, 0]
highest_index = [[0, 0], [0, 0], [0, 0]]
for index, info in enumerate(info_ls):
    avg_scores[0] += int(info[2])
    update_highest_index(0, int(info[2]), index)
    avg_scores[1] += int(info[3])
    avg_scores[2] += int(info[4])
avg_scores = [x//all for x in avg_scores]
print(avg_scores)
print(highest_index)
print('subj1 highest student id:', highest_index[0][1])

