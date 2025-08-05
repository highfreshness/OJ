def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # 분:초 -> 초 변환 함수
    def convert_time(mm_ss:str) -> int:
        mm, ss= mm_ss.split(":")
        return int(mm)*60 + int(ss)
    
    # 현재 재생 위치가 오프닝과 엔딩 사이인 경우 건너뛰기
    def check_in_op(pos_time:int, start_time:int, end_time:int)->int:
        if start_time <= pos_time < end_time:
            return end_time
        return pos_time

    video_time = convert_time(video_len)
    pos_time = convert_time(pos)
    start_time = convert_time(op_start)
    end_time = convert_time(op_end)
    
    # 스킵 구간 확인1
    pos_time = check_in_op(pos_time, start_time, end_time)
    # 기능 모음을 순차 수행
    for command in commands:
        # 기능이 이전 인 경우
        if command == "prev":
            # 현재 위치가 10초 미만인 경우 처음 위치로 이동
            if pos_time < 10:
                pos_time = 0
            else:
                pos_time = pos_time - 10
            
        # 기능이 다음인 경우  
        else:
            # 현재 위치가 동영상 마지막에 대해 10초가 남지 않았다면 마지막으로 이동
            if (video_time - pos_time) <= 10: 
                pos_time = video_time
            else:
                pos_time = pos_time + 10
        
        # 스킵 구간 확인2        
        pos_time = check_in_op(pos_time, start_time, end_time)
                

            
    # 초로 변환했던 시간을 분,초로 변경
    mm = pos_time // 60
    ss = pos_time % 60

    answer = f"{mm:02d}:{ss:02d}"
    return answer