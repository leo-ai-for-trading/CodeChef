'''
//solution: (x-2,y+1) and (x-1,y+2)
//            (x+1,y+2),(x+2,y+1) and (x+2,y-1),(x+1,y-2)
//dx[8] = {2,2,-2,-2,1,1,-1,-1}
//dy[8] = {1,-1,1,-1,2,-2,2,-2}
//for c = 0: 7
//    x1 = x + dx[i]
//    y1 = y + dy[i]
//it becomes x1 = x+2
//           y1 = y+1

'''

rel_pos = [[1,2], [2,1], [1, -2], [2,-1], [-1,2], [-1,-2], [-2,1], [-2,-1]]
def knight_circle(x1, y1):
    li = []
    for pos in rel_pos:
        if x1+pos[0] >= 1 and x1 + pos[0] <= 8:
            if y1+pos[1] >= 1 and y1 + pos[1] <= 8:
                li.append([x1+pos[0], y1+pos[1]])
    return li
for _ in range(int(input())):
    ret = "NO"
    x1, y1 = map(int, input().split(' '))
    x2, y2 = map(int, input().split(' '))
    li1 = knight_circle(x1, y1)
    li2 = knight_circle(x2, y2)
    for i in li1:
        if i in li2:
            ret ="YES"
            break
    print(ret)
