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