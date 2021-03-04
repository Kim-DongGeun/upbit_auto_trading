## 업비트 자동 매매 프로그램
[변동성 돌파 전략](https://stock79.tistory.com/entry/%EC%8B%A4%EC%A0%84-%ED%88%AC%EC%9E%90-%EC%A0%84%EB%9E%B5-48-%EB%B3%80%EB%8F%99%EC%84%B1-%EB%8F%8C%ED%8C%8C-%EC%A0%84%EB%9E%B5%EC%9D%98-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-1)을 이용하여 파이썬으로 간단하게 업비트 openAPI와 연동한 비트코인 자동 매매 프로그램


## install

**"upbit.txt"라는 파일명으로 업비트 API KEY를 access key, secret key 순으로 저장** 

업비트 [openAPI 발급](https://upbit.com/service_center/open_api_guide)

```
upbit.txt
## aceess key
## secret key

```


```pip install pyupbit```

```python trading.py```

## 외부 소스

API 연동은 직접하지 않고 [여기](https://github.com/sharebook-kr/pyupbit)에서 제공하는 라이브러리 사용
