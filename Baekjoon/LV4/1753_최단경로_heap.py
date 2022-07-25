#1753 최단 경로 - 이코테 ver 
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
n , m = map(int,input().split()) # 정점의 개수, 간선의 개수 (노드, 간선)
k = int(input()) #시작 노드 

graph = [[] for i in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보
visited = [False] * (n+1) #방문처리 
distance = [INF] * (m+1) #c최단거리 테이블 무한으로 초기화 

for _ in range(m):
  u,v,w = map(int,input().split()) #모든 간선 정보 입력
  graph[u].append((v,w)) #u에서 v가는 간선 w

def dijkstra(start): 
  queue = []
  heapq.heappush(queue,(0,start))
  distance[start] = 0
  while queue: #큐가 비어있지 않으면
    dist, now = heapq.heappop(queue) #가장 최단 거리가 짧은 노드 정보 꺼내기
    if distance[now] < dist: #이미 처리된 적이 있으면 무시
      continue
    for i in graph[now]: #현재 노드와 연결된 다른 인접 노드 확인 
      cost = dist + i[1] #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue,(cost,i[0]))

dijkstra(k)

for i in range(1,n+1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])