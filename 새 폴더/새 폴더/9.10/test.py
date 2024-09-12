# make_set : 각 요소를 parent 배열에 자기 자신으로 초기화 하는 과정
def init_set(N):
    # N 개 만큼 해당 요소를 가질 수 있는 배열을 할당. 해당 요소들을 각자 자기자신으로 초기화.
    parent = [i for i in range(N)]
    return parent


# find_set : 가장 최상위 부모(그룹의 대표)를 찾아라
def find_set(x):
    # 기저 조건 : 자기 자신이 부모라면 종료
    if x == parent[x]:
        return x

    parent[x] = find_set(parent[x])
    return parent

# union : x와 y가 속한 두 그룹을 하나로 합쳐라
def union(x, y):
    # parent[x] = y 이러면 안된다. 다른 부모를 가르키고 있다면 원래 있었던 그룹조차 연결이 안되는 것  따라서 부모들의 대표를 정해야함
    # 대표자를 찾기 위해 find_set 을 통해 찾아줄 것임
    root_x = find_set(x)
    root_y = find_set(y)

    # 같으면 바꿀 필요가 없음
    if root_x != root_y:
        # 1. x가 지게끔
        parent[root_x] = root_y

        # 2. y가 지게끔
        parent[root_y] = root_x

        # xy의 대표자들중 작은값을 대표로 정할때
        if root_x < root_y:
            parent[root_y] = root_x

        else:
            parent[root_x] = root_y


N = 5  # 요소의 개수
parent = init_set(N)  # [0, 1, 2, 3, 4]
union(0, 1)
union(2, 3)
union(0, 2)
union(0, 4)
