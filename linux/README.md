# Linux


## 권한 관리

리눅스는 여러 사용자가 사용할 수 있는 멀티유저 운영체제이기 때문에 권한 관리가 매우 중요하다.
파일, 디렉토리의 권한과 소유권을 변경하는 방법을 알아보자.

### 1. 파일, 디렉토리 권한 확인

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

### 2. 권한

파일 또는 디렉토리의 권한은 '-rwxr-xr-x'으로 나타낼 수 있다.

4개의 부분으로 나누어진다 - rwx r-x r-x 4부분이다.

맨앞에 '-'는 파일인지 디렉토리인지 구분하기 위한것이다. 파일은 '-' 디렉토리는 'd'로 나타낸다.

다음 rwx는 각각의 권한을 나타낸다. 
- '-' >> 권한 없음
- 'r' >> 읽기(__r__ead)
- 'w' >> 쓰기(__w__rite)
- 'x' >> 실행(e__x__cute)

rwx부분이 또 3개로 나누어진다.

- 처음에 오는 'rwx'는 사용자(__u__ser)권한 ex) 'rwx'사용자에게 읽기 쓰기 실행권한을 모두 준다.
- 가운데 'r-x'는 그룹(__g__roup)의 권한 ex) 'r-x' 그룹에게 읽기와 실행 권한을 준다.
- 마지막에 오는 'r-x'는 다른사용자(__o__ther)   ex) 'r-x' 사용자와 그룹 외의 사람에게 읽기와 쓰기 권한을 준다.
- 디렉토리는 실행권한을 줘야 디렉토리에 들어갈 수 있다.

소유권은 'root root' 확인할 수 있다. 

앞에있는 root는 사용자 root를 의미하며 뒤에있는 root 그룹을 나타낸다.

```bash
-rwxr-xr-x 1 admin kitty  343 Aug 1 20:20 test
```
위의 코드를 해석해보자 
- 처음에 '-'는 파일을 의미한다.
- 다음나오는 'rwx' 3자리 권한은 사용자의 권한을 뜻한다. 파일을 보유한 사용자(admin)는 읽기, 쓰기, 실행 모든 권한을 가지고 있다.
- 'r-x' 두번째 나오는 3자리는 그룹의 권한을 뜻한다. 파일에 속한 그룹(kitty)는 읽기, 실행만 가능하다.
- 'r-x' 세번째 나오는 3자리는 그외의 사용자를 의미한다. 사용자들은 읽기, 실행만 가능하다.
- 'test'라는 이름을 가진 파일이다.


### 3. 권한 변경(chmod 명령어)

파일, 디렉토리의 권한을 바꾸기 위해 'chmod'명령어를 사용한다.

우선 위에서 권한을 __r__ead, __w__rite, e__x__cute, 소유권을 __u__, __g__roup, __o__ther로 표기한 이유가 있다.

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
정말 직관적으로 알 수 있다. chmod에서 __o__ther에게 '+'권한을 준다. 어떤권한? e__x__cute권한 

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
__u__ser에게서 '-'권한을 빼앗는다. 어떤권한 ?? __r__ead, __w__rite, e__x__cute권한을 

위와같이 한번에 여러개를 주고 뺄수도 있다. 반대로 한번에 'ugo+w'처럼 소유권도 한번에 설정 할 수 있다.


마지막으로 숫자들을 사용하는 방법을 확인해보자.

```bash
-rwxr-xr-x 1 admin kitty  343 Aug 1 20:20 test
```

위에서 소유권은 총 3부분으로 나눌 수 있다.

user, group, other 3부분이다. 그리고 권한도 3부분으로 나눌 수 있다. r, w, x 3개이다.

작은 r, w, x부터 나누어보자 
rwx를 2진수로 바꾸어서 생각해보자
- 'rwx' >> '111'
- 'r-x' >> '101'
- 'r--' >> '100'
이진수를 다시 8진수로 바꾸어보자
- '111' >> 7
- '101' >> 5
- '100' >> 4
다들 아시다시피 3개의 2진수중 첫번째는 4, 두번째는 2, 세번째 수는 1로 매핑이 된다.

예를들어 읽기와 실행의 권한을 주고싶다면 4 + 1 = 5 >> 5를 부여하면된다.(우선 기억만하자)

이러한 권한이 총 3개가 있다 user, group, other 총 3개의 숫자를 이용해 모든 권한을 조절할 수 있따.

```bash
$ ls -l
-rwxr-xr-x 1 root root  343 Aug 1 20:20 test
-rw-r-xr-- 1 root root 1044 Aug 3 21:50 chmodtest
-rwxr-xr-- 1 root root  456 Aug 9 10:20 algorism
$ chmod 777 test
$ ls -l chmodtest
-rwxrwxrwx 1 root root 1044 Aug 3 21:50 test
```

__chmod 777 tset__

7은 r = 4, w = 2, x = 1 세개의 권한을 모두 뜻한다.

777은 rwxrwxrwx와 같은 뜻이다.

755는 rwxr-xr-x와 같은 뜻이다.

이런식으로도 권한을 줄 수 있따.
