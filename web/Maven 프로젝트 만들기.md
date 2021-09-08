# Maven 프로젝트 만들기



## Eclipse에서 Maven 생성



### 1) 프로젝트 생성



File > New > Other..

![image](https://user-images.githubusercontent.com/51642448/132524986-552c292e-2029-499b-97d7-0d802dc0ecb8.png)



Java Project 선택

![image](https://user-images.githubusercontent.com/51642448/132526328-b286698f-c783-48a4-8122-cd25018050fd.png)



Project name 등 기본적인 설정 해주고 생성

![image](https://user-images.githubusercontent.com/51642448/132526072-8965d745-b021-41fc-8c82-8e416176ffe1.png)



프로젝트 오른쪽 클릭 > Configure > Convert to Maven Project

![image](https://user-images.githubusercontent.com/51642448/132526647-4213d59b-f379-4e54-b317-c79935e5a7b9.png)



Group Id : 프로젝트를 만드는 그룹의 유일한 이름, 보통 자바 패키지처럼 URI를 거꾸러 써서 나타낸다

Artifact Id : 프로젝트를 나타내는 유일한 이름, 그룹 내 다른 아티팩트와 이름이 달라야한다.

Version : 프로젝트 버전

Packaging : 필요한 형식을 사용한다.

![image](https://user-images.githubusercontent.com/51642448/132527003-ca148a1c-946e-49e9-b6c5-8528eecee39a.png)



우측 하단을 확인하면 필요한 부분에 대해서 다운로드한다.

다운로드 완료되면 Maven 끝!!

![image](https://user-images.githubusercontent.com/51642448/132527589-1da029af-50ec-4ec0-bdb2-5568be45c94d.png)



**근데 원래 파일구조가 이랬던가?**

![image](https://user-images.githubusercontent.com/51642448/132527915-0621783e-7215-4d87-9cab-7e220c09c06e.png)



## 다시한번 해보자



File > New > Other...

![image](https://user-images.githubusercontent.com/51642448/132529390-2b9f4f83-8f60-467c-b4fa-967ebbdf1763.png)



Maven Project 선택

![image](https://user-images.githubusercontent.com/51642448/132529556-c49353a8-0696-4c61-8485-38e41a8e8a04.png)



Create a simple project(skip archetype selection) 체크

location은 본인이 원하는 경로나 default경로

![image](https://user-images.githubusercontent.com/51642448/132529933-0210361a-964e-4b58-b2ff-b7d6157d3181.png)



설치중~ 세팅하는 이미지를 캡처 하나 못했다.

![image](https://user-images.githubusercontent.com/51642448/132531621-27f5155d-e0c7-40cb-9fa1-402746877634.png)



아래와 같은 파일 구조가 나왔다.

근데 왜 자바 버전이 저러지? 

우선 오늘은 여기까지

![image](https://user-images.githubusercontent.com/51642448/132531559-ffe4d03f-4daa-43d3-b861-b512b925594b.png)