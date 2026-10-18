"""
문서 사이트 만들기 — 원본 문서(프로젝트 폴더)를 이 저장소로 복사해 웹페이지로 감싼다.

  python3 build.py        → guide.html · process.html · chatbot.html · img/ 갱신
  그다음 git add -A && git commit && git push 하면 1~2분 뒤 사이트에 반영된다.

원본은 고치는 곳 한 곳뿐:
  ../운영가이드_창고매니저.html          → guide.html   (매니저 운영가이드)
  ../개편보고/홈페이지_신청결제_개편보고.html → process.html (창고 신청/결제 프로세스 개선 안내)
  ../운영가이드_챗봇.html                → chatbot.html (챗봇 운영가이드)
  ../개편보고/img/                       → img/
"""
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parent
SRC = HERE.parent
PAGES = {
    "guide.html": SRC / "운영가이드_창고매니저.html",
    "process.html": SRC / "개편보고" / "홈페이지_신청결제_개편보고.html",
    "chatbot.html": SRC / "운영가이드_챗봇.html",
}
HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
"""
BACK = """<a href="./" style="position:fixed;top:calc(env(safe-area-inset-top,0px) + 12px);left:12px;z-index:10;
font:600 13px/1 'IBM Plex Sans KR','Apple SD Gothic Neo',sans-serif;color:#171716;background:#ffd600;
padding:8px 12px;border-radius:999px;text-decoration:none;box-shadow:0 1px 4px rgba(0,0,0,.15)" class="no-print">← 목록</a>
<style>@media print{.no-print{display:none!important}}</style>
"""


def wrap(src: Path) -> str:
    s = src.read_text(encoding="utf-8")
    # 원본은 <title>·<link>·<style> 로 시작하고 본문이 이어진다 — head 와 body 로 나눠 감싼다
    cut = s.find("</style>") + len("</style>")
    return HEAD + s[:cut] + "\n</head>\n<body>\n" + BACK + s[cut:] + "\n</body>\n</html>\n"


for out, src in PAGES.items():
    (HERE / out).write_text(wrap(src), encoding="utf-8")
    print("갱신", out)

img_src, img_dst = SRC / "개편보고" / "img", HERE / "img"
img_dst.mkdir(exist_ok=True)
for f in sorted(img_src.glob("*.jpg")):
    shutil.copy2(f, img_dst / f.name)
print("이미지", len(list(img_dst.glob("*.jpg"))), "장")
