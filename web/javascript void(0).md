# javascript:void(0)

javascript:void(0)는 html a태그의 속성 중 하나인 href의 값으로 많이 사용된다.

javascript:로 시작하는 URI를 지원하는 브라우저에서는, URI에 있는 코드의 평가 결과가 undefined가 아니라면 페이지의 콘텐츠를 반환 값으로 대체합니다. void 연산자를 사용하면 undefined를 반환할 수 있다

```javascript
<a href="javascript:void(0);">
  클릭해도 아무 일도 없음
</a>
<a href="javascript:void(document.body.style.backgroundColor='green');">
  클릭하면 배경색이 녹색으로
</a>
```

### 기본 사용법

처음에는 어떻게 사용하는지 몰랐으나 다른 블로그 찾아보면서 알았다.

html요소를 클릭하여 이벤트를 발생시킬 경우, 자바스크립트로 어떤 동작이 일어나게끔 컨트롤해야한다.

특히 <a></a>태그를 이용한 마우스를 올렸을 때에 페이지가 이동을 하느넋을 쉬게 알게끔 해주는것?

이런 이유 때문에 자바스크립트의 이벤트 핸들러인 onclick등을 사용해 명시적으로 클릭을 유도할 경우 상당히 많이 사용한다. 

보통은 a태그를 클릭하게 되면 속성중 하나이 gref에 지정한 url로 페이지가 바뀌면서 이동한다. 그러나 페이지가 이동을 하지 않게 하곳 싶을 때 javascript:void(0)을 사용하면 된다.

쉽게말해서 a태그의 디자인성을 살리면서 링크를 없엔다.
