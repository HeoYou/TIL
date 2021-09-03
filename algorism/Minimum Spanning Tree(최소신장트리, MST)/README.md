## Minimun Spanning Tree(최소 신장 트리)

최소 신장 트리는 어떤 그래프에서 가중치의 합이 최소인 **최소 연결부분 그래프**를 말한다. **부분 그래프**는 어떤 그래프를 구성하고 있는 간선들 가운데 일부가 제거된 그래프를 뜻한다.


예를 들어 다음과 같은 그래프가 있다.


![image](https://user-images.githubusercontent.com/51642448/131949023-58ac8f50-fa63-4229-b565-8553b4beb0b7.png)

아래의 그래프들은 위의 그래프의 부분 그래프에 포함되는 그래프이다.


![image](https://user-images.githubusercontent.com/51642448/131949088-95dcad8b-b509-4285-a37d-d1fe4e38dfd2.png)
![image](https://user-images.githubusercontent.com/51642448/131949112-5a3cfa82-c2b6-4558-82de-41ee9299e5f3.png)



![image](https://user-images.githubusercontent.com/51642448/131949134-ebd115ab-7b93-45a4-a9ad-61117950c540.png)
![image](https://user-images.githubusercontent.com/51642448/131949163-54dc3767-163a-4945-86f4-6cdaf95bac3d.png)



여러 **부분 그래프** 중에서도 연결 그래프는 그래프를 구성하는 모든 두 정점 사이에 경로가 존재하는 그래프를 말한다.

여기서 최소라는 단어가 붙은 **최소 연결 부분 그래프**는 간서의 수를 최소로 이용하여 만들 수 있는 연결 그래프 즉 트리를 뜻하게 됩니다. 

트리가 그래프의 특수한 형태였다면 최소 신장트리는 트리의 특수한 형태중 하나이다. 따라서 그래프의 특수한 형태였다면 최소 신장 트리는 트리의 특수한 형태중 하나이다.

따라서 트리가 갖는 특징인 사이클이 없다라는 점과, 모든 정점을 연결해야 한다는 점 등을 만족해야 한다.


최소 신장 트리를 구하는 잘 알려진방법
- 크루스칼(Kruskal) 알고리즘
- 프림(Prim) 알고리즘