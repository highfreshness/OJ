# H = 층, W = 층별 객실 수, T = 입력 받을 테스트 데이터 수, N = N번째 객실 수

t = int(input())

info = []
hotel = []

info = [map(int, input().split()) for x in range(t)]

for i in info:
    h, w, n = i
    for r in range(1,w+1):
        for f in range(1,h+1):
            hotel.append((f*100)+r)
    print(hotel[n-1])
    hotel = []

