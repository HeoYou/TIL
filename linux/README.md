# Linux


## 권한 관리

리눅스는 여러 사용자가 사용할 수 있는 멀티유저 운영체제이기 때문에 권한 관리가 매우 중요하다.
파일, 디렉토리의 권한과 소유권을 변경하는 방법을 알아보자.

### 파일, 디렉토리 권한 확인

```bash
$ ls -l
```
- ls 명령어를 사용하면 -파일, 디렉토리의 권한-을 확인할 수 있다.

```bash
-rwxr-xr-x 1 root root  343 Aug 1 20:20 test
-rw-r-xr-- 1 root root 1044 Aug 3 21:50 chmodtest
-rwxr-xr-- 1 root root  456 Aug 9 10:20 algorism
```
띄어쓰기를 기준으로 - 파일권한, 링크수, 사용자, 그룹, 파일크기, 수정시간, 파일이름 -을 의미한다.

### 권한

파일 또는 디렉토리의 권한은 '-rwxr-xr-x'으로 나타낼 수 있다.

4개의 부분으로 나누어진다 - rwx r-x r-x 4부분이다.

맨앞에 '-'는 파일인지 디렉토리인지 구분하기 위한것이다. 파일은 '-' 디렉토리는 'd'로 나타낸다.

다음 rwx는 각각의 권한을 나타낸다. 
- '-' >> 권한 없음
- 'r' >> 읽기(-r-ead)
- 'w' >> 쓰기(-w-rite)
- 'x' >> 실행(e-x-cute)

rwx부분이 또 3개로 나누어진다.

- 처음에 오는 'rwx'는 사용자(-u-ser)권한 ex) 'rwx'사용자에게 읽기 쓰기 실행권한을 모두 준다.
- 가운데 'r-x'는 그룹(-g-roup)의 권한 ex) 'r-x' 그룹에게 읽기와 실행 권한을 준다.
- 마지막에 오는 'r-x'는 다른사용자(-o-ther)   ex) 'r-x' 사용자와 그룹 외의 사람에게 읽기와 쓰기 권한을 준다.
- 디렉토리는 실행권한을 줘야 디렉토리에 들어갈 수 있다.

소유권은 'root root' 확인할 수 있다. 

앞에있는 root는 사용자 root를 의미하며 뒤에있는 root 그룹을 나타낸다.

```bash
-rwxr-xr-x 1 admin kitty  343 Aug 1 20:20 test
```
위의 코드를 해석해보자 
- 처음에 '-'는 파일을 의미한다.
- 'rwx' 처음 나오는 3자리 권한은 사용자의 권한을 뜻한다. 파일을 보유한 사용자(admin)는 읽기, 쓰기, 실행 모든 권한을 가지고 있다.
- 'r-x' 두번째 나오는 3자리는 그룹의 권한을 뜻한다. 파일에 속한 그룹(kitty)는 읽기, 실행만 가능하다.
- 'r-x' 세번째 나오는 3자리는 그외의 사용자를 의미한다. 사용자들은 읽기, 실행만 가능하다.
- 'test'라는 이름을 가진 파일이다.


### 권한 변경(chmod 명령어)

파일, 디렉토리의 권한을 바꾸기 위해 'chmod'명령어를 사용한다.

우선 위에서 권한을 -r-ead, -w-rite, e-x-cute, 소유권을 -u-, -g-roup, -o-ther로 표기한 이유가 있다.

볼드 처리된 글씨를 이용하여 권한을 주고 빼앗을 수 있다.


```bash
$ ls -l
-rwxr-xr-x 1 root root  343 Aug 1 20:20 test
-rw-r-xr-- 1 root root 1044 Aug 3 21:50 chmodtest
-rwxr-xr-- 1 root root  456 Aug 9 10:20 algorism
$ chmod o+x chmodtest
$ ls -l chmodtest
-rw-r-xr-x 1 root root 1044 Aug 3 21:50 chmodtest
```

'chmod o+x chmodtest'
정말 직관적으로 알 수 있다. chmod에서 -o-ther에게 '+'권한을 준다. 어떤권한? e-x-cute권한 

다른 예
```bash
$ ls -l
-rwxr-xr-x 1 root root  343 Aug 1 20:20 test
-rw-r-xr-- 1 root root 1044 Aug 3 21:50 chmodtest
-rwxr-xr-- 1 root root  456 Aug 9 10:20 algorism
$ chmod u-rwx chmodtest
$ ls -l chmodtest
----r-xr-x 1 root root 1044 Aug 3 21:50 chmodtest
```
'chmod u-rwx chmodtest'
-u-ser에게서 '-'권한을 빼앗는다. 어떤권한 ?? -r-ead, -w-rite, e-x-cute권한을 

위와같이 한번에 여러개를 주고 뺄수도 있다. 반대로 한번에 'ugo+w'처럼 소유권도 한번에 설정 할 수 있다.