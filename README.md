# 미니창고짐 운영 문서

https://beyondspacezim.github.io/zim-docs/

- `index.html` — 목록(메인) 페이지
- `guide.html` — 매니저 운영가이드 (원본: `../운영가이드_창고매니저.html`)
- `process.html` — 창고 신청/결제 프로세스 개선 안내 (원본: `../개편보고/홈페이지_신청결제_개편보고.html`)
- `chatbot.html` — 챗봇 운영가이드 (원본: `../운영가이드_챗봇.html`)

## 업데이트

원본 파일을 고친 뒤:

```
python3 build.py
git add -A && git commit -m "문서 업데이트" && git push
```

1~2분 뒤 같은 주소에 반영된다. 검색엔진 노출은 막아 두었다 (`robots.txt`, `noindex`). 비밀값·고객 실명·연락처는 넣지 않는다.
