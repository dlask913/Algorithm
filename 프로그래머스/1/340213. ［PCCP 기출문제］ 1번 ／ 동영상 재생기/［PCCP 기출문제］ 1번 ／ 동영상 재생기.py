def to_seconds(time):
    mm, ss = map(int, time.split(":"))
    return mm * 60 + ss

def is_between(start, pos, end):
    pos_sec = to_seconds(pos)
    start_sec = to_seconds(start)
    end_sec = to_seconds(end)
    return start_sec <= pos_sec <= end_sec

def solution(video_len, pos, op_start, op_end, commands):
    for c in commands:
        if is_between(op_start, pos, op_end): # 오프닝 사이인 경우
            pos = op_end
        
        x = -10 if c == "prev" else 10 # 명령에 따라 x 값 변경

        pos_sec = to_seconds(pos) + x
        len_sec = to_seconds(video_len)
        total = max(0, pos_sec) # 최소 0
        total = min(len_sec, total) # 최대 길이는 video_len 
        
        mm, ss = total // 60, total % 60
        pos = f"{mm:02}:{ss:02}" # 문자열로 변환
        
    if is_between(op_start, pos, op_end):
        pos = op_end
    
    return pos