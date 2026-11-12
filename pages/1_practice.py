import streamlit as st

st.title("11/12 실습")


with st.expander("기사 원문 보기"):
    st.write("""[데이터넷] 2027년에는 사이버 공격의 초점이 데이터 탈취에서 기업의 의사결정 조작으로 확대될 것으로 예상된다.


            구글 클라우드의 ‘2027년 보안 전망(Security Forecast for 2027)’에서는 “AI 에이전트가 계약 협상과 재고 관리, 자본 배분 등 핵심 업무를 자율적으로 수행하면서 공격자들도 데이터가 저장된 시스템을 넘어 기업의 의사결정 과정과 이를 뒷받침하는 데이터, 소프트웨어 공급망을 표적으로 삼기 시작했다”고 경고했다.


            크리스 베츠(Chris Betz) 구글 클라우드 CISO는 “2027년 기업용 소프트웨어는 가격 결정, 공급업체 계약 협상, 자본 배분, 공급망 재편 등을 실시간으로 수행하는 자율형 에이전트의 집합체로 변화할 것”이라며 “이러한 에이전트가 의존하는 데이터와 기술 기반을 보호하는 것이 중요하다”고 밝혔다.


            출처 : 데이터넷(https://www.datanet.co.kr)""")


a, b, c = st.tabs( ["문제1", "문제2", "문제3"] )
with a:
    st.write("문제1")
    st.subheader("1. 식 전개하기")
    st.latex(r"(x+y)^2")


    with st.form("forms1"):

        answer1 = st.radio("전개한 식을 선택해주세요.", 
        [r"$x^2+y^2$", r"$x^2+xy+y^2$", r"$x^2+2xy+y^2$", r"$x^2-2xy+y^2$"],
        index=None,)

        submit_button1 = st.form_submit_button("제출")

        if submit_button1:
            if answer1 == r"$x^2+2xy+y^2$":
                st.success("정답입니다!")
            elif answer1 == r"$x^2-2xy+y^2$":
                st.warning("앗! 부호를 다시 살펴볼까요?")
            elif answer1 == r"$x^2+xy+y^2$":
                st.info("앗! 두번째 항을 다시 살펴볼까요?")
            else:
                st.error("앗! 항이 부족한지 다시 확인해볼까요?")





with b:
    st.write("문제2")
    st.subheader("2. 정수의 덧셈과 뺄셈")


    with st.form("forms2"):

        answer2 = st.radio("다음 중 올바른 식을 고르세요.", 
        [r"$-5+7=12$", r"$13+(-9)=4$", r"$2-7=5$", r"$20+(-5)=25$"],
        index=None,
        )
        
        submit_button2 = st.form_submit_button("제출")


        if submit_button2:
            if answer2 == r"$-5+7=12$":
                st.warning("5 앞에 있는 부호를 잘 살펴보세요")
            elif answer2 == r"$13+(-9)=4$":
                st.success("정답이에요~!")
            elif answer2 == r"$2-7=5$":
                st.info("2에서 7을 뺀다는 건 풍선을 2개 달고 이후에 추를 7개 다는 것과 같아요. 다시 생각해보세요!")
            else:
                st.error("20에 -5를 더한다는 것은 20에서 5를 빼는 것과 똑같아요")





with c:
    st.write("문제3")




