def solution(book_time):
    answer = 0
    room = []
    book_time.sort()
    for i in range(len(book_time)):
        if not room:
            room.append(book_time[i])
        else:
            bh,bm = map(int,book_time[i][0].split(":"))
            flag = True
            for j in range(len(room)):
                rh,rm = map(int,room[j][1].split(":"))
                rh = rh if (rm+10)<60 else rh+1
                if (rh==bh and (rm+10)%60<=bm) or rh<bh:
                    flag = False
                    room[j]=book_time[i]
                    break
            if flag:
                room.append(book_time[i])
    answer = len(room)
    return answer