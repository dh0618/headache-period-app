import streamlit as st

# 상태 저장
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def go_to_page(page_name):
    st.session_state.page = page_name

# 페이지 구성
def main_page():
    st.title("💊 두통/생리통 약 추천 시스템")
    st.write("어떤 통증을 겪고 계신가요?")
    if st.button("두통"):
        go_to_page('headache_q1')
    if st.button("생리통"):
        go_to_page('period_q1')

def back_button(prev_page):
    if st.button("⬅ 이전으로"):
        go_to_page(prev_page)

def headache_q1():
    st.header("Q1. 통증 위치는 어디인가요?")
    option = st.radio("", ["이마", "관자놀이", "머리 전체", "뒤통수"])
    st.session_state.hq1 = option
    if st.button("다음"):
        go_to_page("headache_q2")
    back_button("main")

def headache_q2():
    st.header("Q2. 통증을 유발하는 요인은 무엇인가요?")
    option = st.radio("", ["스트레스", "밝은 빛", "수면 부족", "생리 전후"])
    st.session_state.hq2 = option
    if st.button("다음"):
        go_to_page("headache_q3")
    back_button("headache_q1")

def headache_q3():
    st.header("Q3. 다음 중 어떤 증상이 함께 나타나나요?")
    option = st.radio("", ["구토", "눈부심", "목 뻣뻣함", "없음"])
    st.session_state.hq3 = option
    if st.button("다음"):
        go_to_page("headache_q4")
    back_button("headache_q2")

def headache_q4():
    st.header("Q4. 위장에 민감한 편인가요?")
    option = st.radio("", ["예", "아니오"])
    st.session_state.hq4 = option
    if st.button("추천 보기"):
        go_to_page("headache_result")
    back_button("headache_q3")

def period_q1():
    st.header("Q1. 통증이 시작되는 시점은?")
    option = st.radio("", ["생리 시작 전", "생리 시작 후", "둘 다 아님"])
    st.session_state.pq1 = option
    if st.button("다음"):
        go_to_page("period_q2")
    back_button("main")

def period_q2():
    st.header("Q2. 통증 부위는 어디인가요?")
    option = st.radio("", ["복부 전체", "허리", "골반 깊은 곳", "하복부"])
    st.session_state.pq2 = option
    if st.button("다음"):
        go_to_page("period_q3")
    back_button("period_q1")

def period_q3():
    st.header("Q3. 평소 위장이 민감한 편인가요?")
    option = st.radio("", ["예", "아니오"])
    st.session_state.pq3 = option
    if st.button("다음"):
        go_to_page("period_q4")
    back_button("period_q2")

def period_q4():
    st.header("Q4. 생리통 외에 다음 중 해당되는 증상이 있나요?")
    option = st.radio("", ["어지러움", "메스꺼움", "식욕 부진", "없음"])
    st.session_state.pq4 = option
    if st.button("추천 보기"):
        go_to_page("period_result")
    back_button("period_q3")

def headache_result():
    st.success("💡 두통에 적합한 약을 추천합니다!")
    t = ""
    if st.session_state.hq4 == "예":
        t = "아세트아미노펜"
        img = "acetaminophen.jpg"
    elif st.session_state.hq2 == "스트레스" or st.session_state.hq3 == "목 뻣뻣함":
        t = "이부프로펜"
        img = "ibuprofen1.jpg"
    elif st.session_state.hq2 == "밝은 빛" or st.session_state.hq3 in ["구토", "눈부심"]:
        t = "트립탄"
        img = "triptan.png"
    elif st.session_state.hq2 == "생리 전후":
        t = "나프록센"
        img = "naproxen.jpg"
    else:
        t = "이부프로펜"
        img = "ibuprofen1.jpg"

    st.write(f"**추천 약:** {t}")
    st.image(img, use_container_width=True)
    if st.button("🔄 처음으로 돌아가기"):
        go_to_page("main")

def period_result():
    st.success("💡 생리통에 적합한 약을 추천합니다!")
    t = ""
    if st.session_state.pq3 == "예":
        t = "아세트아미노펜"
        img = "acetaminophen.jpg"
    elif st.session_state.pq1 == "생리 시작 전":
        t = "나프록센"
        img = "naproxen.jpg"
    elif st.session_state.pq2 == "골반 깊은 곳" or st.session_state.pq4 in ["식욕 부진", "어지러움"]:
        t = "메페남산"
        img = "mefenamic.png"
    else:
        t = "이부프로펜"
        img = "ibuprofen2.jpg"

    st.write(f"**추천 약:** {t}")
    st.image(img, use_container_width=True)
    if st.button("🔄 처음으로 돌아가기"):
        go_to_page("main")

# 라우팅
pages = {
    "main": main_page,
    "headache_q1": headache_q1,
    "headache_q2": headache_q2,
    "headache_q3": headache_q3,
    "headache_q4": headache_q4,
    "period_q1": period_q1,
    "period_q2": period_q2,
    "period_q3": period_q3,
    "period_q4": period_q4,
    "headache_result": headache_result,
    "period_result": period_result,
}

pages[st.session_state.page]()