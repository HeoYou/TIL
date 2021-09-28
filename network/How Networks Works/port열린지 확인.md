# Port 열린지 확인

사무실을 옮긴 후 부터 DB에 접속이 안되서 알아보는 중 Ncloud DB서버에 포트 개방이 안되있던걸 확인 할 수 있었다.

그리고 포트가 열린지 확인하는 방법을 확인해 보았다.



### telnet을 사용한 확인

telnet을 사용하면 port가 열려있는지 확인 할 수 있다.

```
telnet ip port
```



위와 같은 방법을 이용하면 연결이 되면 열려있는 상태

연결이 되지 않으면 닫혀있는 상태로 볼 수 있다.



telnet은 사용전에 설치를 따로 해주어야한다.



![image](https://user-images.githubusercontent.com/51642448/135097285-6675c47e-ff87-4b0f-a077-de0012380d67.png)



제어판 >> 프로그램 >> 프로그램 및 기능에서

windows 기능 켜기/끄기 선택



![image](https://user-images.githubusercontent.com/51642448/135097398-c77f9f2e-d8c3-4aa5-8041-05d2f9811134.png)

가장 아래부분에 텔넷 클라이언트 체크하고 확인하면 된다.

여기서 .Net 3.5가 설치되어야한다.



그러면 명령으를 사용할 수 있다.