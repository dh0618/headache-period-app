
import streamlit as st

st.set_page_config(page_title="두통/생리통 약 추천기", layout="centered")

# 앱 상태를 저장하기 위한 세션 스테이트 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'answers' not in st.session_state:
    st.session_state.answers = {}

def go_home():
    st.session_state.page = 'home'
    st.session_state.answers = {}

def submit_answers():
    st.session_state.page = 'result'

# 약 정보 사전
drug_info = {
    '이부프로펜': {
        '효능': '비스테로이드성 소염진통제(NSAID). 염증을 억제하고 통증과 열을 완화함. 두통, 생리통, 근육통 등 다양한 통증에 효과적.',
        '부작용': '위장장애(속쓰림, 위염), 두통, 어지러움, 간기능·신장 문제 (장기복용 시)',
        '의사상담': '❌',
        '추천이유': '긴장성 두통: 스트레스 유발, 근육 긴장에 의한 염증 완화\n일반 생리통형: 하복부 통증, 경련성 통증 완화',
        '이미지': ['ibuprofen1.jpg', 'ibuprofen2.jpg']
    },
    '트립탄': {
        '효능': '편두통 전용 약. 혈관 수축 및 삼차신경 억제를 통해 편두통 증상 완화.',
        '부작용': '어지러움, 졸림, 가슴 통증, 심장질환 환자 금지',
        '의사상담': '✅',
        '추천이유': '편두통: 빛·소리에 민감하고 구토 동반, 일반 진통제 효과 없음.',
        '이미지': ['triptan.png']
    },
    '아세트아미노펜': {
        '효능': '해열·진통 효과 있음. 위장 부담이 적고 간에 주로 작용. 경미한 두통, 감기, 생리통 등에 사용.',
        '부작용': '간 손상(과량 복용 시), 드물게 알레르기 반응',
        '의사상담': '❌',
        '추천이유': '위장 민감형 두통·생리통에 추천. 위장 자극이 거의 없어 위장장애 있는 사람에게 적합.',
        '이미지': ['acetaminophen.jpg']
    },
    '나프록센': {
        '효능': 'NSAID 계열. 이부프로펜보다 지속시간이 길며 생리 전 통증 조절에 효과적. 항염작용 우수.',
        '부작용': '위장장애, 현기증, 졸림, 신장 기능 영향',
        '의사상담': '❌',
        '추천이유': '생리 관련 두통, 호르몬형 생리통에 적합. 생리 전·후 장기 통증 억제에 효과적.',
        '이미지': ['naproxen.jpg']
    },
    '메페남산': {
        '효능': 'NSAID 중 강한 진통 효과 보임. 복부 깊은 통증이나 통상 진통제로 안 되는 경우에 사용.',
        '부작용': '위장장애, 설사, 어지럼증, 간기능 저하 (드물게)',
        '의사상담': '✅',
        '추천이유': '내분비 민감형 생리통: 강한 복부·골반 통증, 식욕 저하 등 동반 시 사용.',
        '이미지': ['mefenamic.png']
    }
}

def headache_questions():
    st.header("🧠 두통 질문")
    q1 = st.radio("1. 통증 위치는 어디인가요?", ["이마", "관자놀이", "머리 전체", "뒤통수"])
    q2 = st.radio("2. 통증을 유발하는 요인은 무엇인가요?", ["스트레스", "밝은 빛", "수면 부족", "생리 전후"])
    q3 = st.radio("3. 다음 중 어떤 증상이 함께 나타나나요?", ["구토", "눈부심", "목 뻣뻣함", "없음"])
    q4 = st.radio("4. 위장에 민감한 편인가요?", ["예", "아니오"])
    if st.button("약 추천 받기"):
        st.session_state.answers = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'type': '두통'}
        submit_answers()
    st.button("처음으로 돌아가기", on_click=go_home)

def period_questions():
    st.header("🩸 생리통 질문")
    q1 = st.radio("1. 통증이 시작되는 시점은?", ["생리 시작 전", "생리 시작 후", "둘 다 아님"])
    q2 = st.radio("2. 통증 부위는 어디인가요?", ["복부 전체", "허리", "골반 깊은 곳", "하복부"])
    q3 = st.radio("3. 평소 위장이 민감한 편인가요?", ["예", "아니오"])
    q4 = st.radio("4. 생리통 외에 다음 중 해당되는 증상이 있나요?", ["어지러움", "메스꺼움", "식욕 부진", "없음"])
    if st.button("약 추천 받기"):
        st.session_state.answers = {'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'type': '생리통'}
        submit_answers()
    st.button("처음으로 돌아가기", on_click=go_home)

def show_result():
    answers = st.session_state.answers
    t = answers['type']

    # 간단한 규칙 기반 추천
    if t == '두통':
        if answers['q1'] == '관자놀이' or answers['q2'] == '밝은 빛' or answers['q3'] in ['구토', '눈부심']:
            drug = '트립탄'
        elif answers['q4'] == '예':
            drug = '아세트아미노펜'
        elif answers['q2'] == '스트레스' or answers['q3'] == '목 뻣뻣함':
            drug = '이부프로펜'
        elif answers['q2'] == '생리 전후':
            drug = '나프록센'
        else:
            drug = '이부프로펜'
    else:
        if answers['q4'] == '식욕 부진' or answers['q2'] == '골반 깊은 곳':
            drug = '메페남산'
        elif answers['q3'] == '예':
            drug = '아세트아미노펜'
        elif answers['q1'] == '생리 시작 전':
            drug = '나프록센'
        else:
            drug = '이부프로펜'

    info = drug_info[drug]

    st.success(f"추천 약: 💊 **{drug}**")
    for img in info['이미지']:
        st.image(img, use_container_width=True)
    st.subheader("📌 약 정보")
    st.markdown(f"**효능:** {info['효능']}")
    st.markdown(f"**대표적인 부작용:** {info['부작용']}")
    st.markdown(f"**의사 상담 필요 여부:** {info['의사상담']}")
    st.markdown(f"**왜 추천됐는지:** {info['추천이유']}")

    st.button("🔁 처음으로 돌아가기", on_click=go_home)

def main():
    if st.session_state.page == 'home':
        st.title("🤖 두통 & 생리통 약 추천 시스템")
        st.write("원하는 통증 유형을 선택하고, 간단한 질문에 답해보세요!")
        if st.button("🧠 두통 약 추천 시작"):
            st.session_state.page = 'headache'
        if st.button("🩸 생리통 약 추천 시작"):
            st.session_state.page = 'period'
    elif st.session_state.page == 'headache':
        headache_questions()
    elif st.session_state.page == 'period':
        period_questions()
    elif st.session_state.page == 'result':
        show_result()

main()
