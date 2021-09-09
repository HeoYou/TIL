# lombok을 설치해보자



lombok은 그냥 dependency에 추가만 한다고 돌아가지 않았다.

그래서 작성



1. 우선 필요한 버전의 lombok을 pom.xml에 추가하자

```xml
<dependency>
    <groupId>org.projectlombok</groupId> 
    <artifactId>lombok</artifactId> 
    <scope>provided</scope> 
</dependency>

```



2. lombok이 다운로도된 경로로 가자

   가서 주소창에 cmd를 치면 경로에서 커멘드창이 열린다.

![image](https://user-images.githubusercontent.com/51642448/132689620-9648569a-921c-467b-8482-b9dd443469fa.png)

3. lombok을 실행시켜 주자.

   - java -jar lombok.jar

![image](https://user-images.githubusercontent.com/51642448/132689920-49f5a898-cadb-4a02-99b0-f7d31d5ac54d.png)



4.  확인 클릭.

![image](https://user-images.githubusercontent.com/51642448/132690123-b2118b3a-bb7b-46c5-97ff-4bb840d13a56.png)



5. 설치할 이클립스 실행파일 선택해주자.

![image](https://user-images.githubusercontent.com/51642448/132690568-884dbe13-fab8-4e34-b187-e9a4bb24c1b4.png)

![image](https://user-images.githubusercontent.com/51642448/132690816-201975e6-f940-4d69-8a90-4c2837673ade.png)



6. Install/update

![image](https://user-images.githubusercontent.com/51642448/132690976-f96da43d-c875-4bad-af21-9377456e0032.png)



7. 설치 끝

![image](https://user-images.githubusercontent.com/51642448/132691174-88ec21a0-28fd-4d79-8d68-79acbeb2118f.png)



8. eclipse폴더에 있는 eclipse.ini를 확인해보자

   - 마지막줄에 아래 두 줄이 추가되어야 하는데?

     ```
     -vmargs
     -javaagent:lombok.jar
     ```

   -javaagent:C:\Tool\eclipse\lombok.jar << 이것만 추가됨.. 뭐지?

   우선 재시작하고 해보자.
