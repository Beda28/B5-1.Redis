# 1. 문서 개요
> 본 문서는 mini redis를 제작하면서, 자료구조에 대해서 공부한 과정을 정리한 문서입니다.

# 2. 폴더 구조
```bash
B5-1.Redis/
├─ main.py          # CLI 입력 및 명령어 분기
├─ service.py       # Redis 기능 통합 로직
|
├─ HashMap.py       # Chaining 기반 HashMap
├─ LinkedList.py    # Doubly Linked List + LRU 순서 관리
├─ Heap.py          # TTL 관리를 위한 Min Heap
|
├─ README.md        # 프로젝트 설명 및 사용법
└─ .gitignore
```

# 3. 명령어
```bash
# 첫 명령어는 소문자로 입력해도 자동으로 대문자로 반환됩니다.

SET [KEY] [value]
GET [KEY]
DEL [KEY]
EXISTS [KEY]
DBSIZE
KEYS

CONFIG SET maxmemory [value]
INFO memory

EXPIRE [KEY] [value]
TTL [KEY]
```
