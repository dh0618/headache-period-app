
import streamlit as st
from PIL import Image

st.set_page_config(page_title="두통/생리통 약 추천", layout="centered")

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# 질문 구성
headache_questions = [
    ("통증 위치는 어디인가요?", ["이마", "관자놀이", "머리 전체", "뒤통수"]),
    ("통증을 유발하는 요인은 무엇인가요?", ["스트레스", "밝은 빛", "수면 부족", "생리 전후"]),
    ("다음 중 어떤 증상이 함께 나타나나요?", ["구토", "눈부심", "목 뻣뻣함", "없음"]),
    ("위장에 민감한 편인가요?", ["예", "아니오"]),
]

period_questions = [
    ("통증이 시작되는 시점은?", ["생리 시작 전", "생리 시작 후", "둘 다 아님"]),
    ("통증 부위는 어디인가요?", ["복부 전체", "허리", "골반 깊은 곳", "하복부"]),
    ("평소 위장이 민감한 편인가요?", ["예", "아니오"]),
    ("생리통 외에 다음 중 해당되는 증상이 있나요?", ["어지러움", "메스꺼움", "식욕 부진", "없음"]),
]

# 약 정보
medications = {
    "이부프로펜": {
        "효능": "염증을 억제하고 통증과 열을 완화함. 두통, 생리통, 근육통 등 다양한 통증에 효과적.",
        "부작용": "위장장애(속쓰림, 위염), 어지러움, 간기능·신장 문제 (장기복용 시)",
        "의사상담": "❌",
        "이유": "긴장성 두통 또는 일반 생리통에 적합. 근육 긴장, 경련성 통증 완화.",
        "이미지": ["ibuprofen1.jpg", "ibuprofen2.jpg"]
    },
    "트립탄": {
        "효능": "편두통 전용 약. 혈관 수축 및 신경 억제를 통해 편두통 증상 완화.",
        "부작용": "어지러움, 졸림, 가슴 통증, 심장질환 환자 금지",
        "의사상담": "✅",
        "이유": "편두통: 빛·소리에 민감하고 구토 동반, 일반 진통제 효과 없음.",
        "이미지": ["triptan.png"]
    },
    "아세트아미노펜": {
        "효능": "해열·진통 효과. 위장 부담 적고 간에 작용. 경미한 두통, 감기, 생리통 등에 사용.",
        "부작용": "간 손상(과량 복용 시), 드물게 알레르기 반응",
        "의사상담": "❌",
        "이유": "위장이 민감한 경우에 적합. 일반적인 경증 통증에도 무난.",
        "이미지": ["acetaminophen.jpg"]
    },
    "나프록센": {
        "효능": "염증 억제 및 지속 시간 긴 진통 작용. 생리 전후 통증 완화에 효과적.",
        "부작용": "위장장애, 졸림, 신장 기능 영향",
        "의사상담": "❌",
        "이유": "생리 관련 두통 또는 호르몬형 생리통에 적합. 장기 통증 억제에 도움.",
        "이미지": ["naproxen.jpg"]
    },
    "메페남산": {
        "효능": "강한 진통 작용. 일반 진통제로 효과 없을 때 적합.",
        "부작용": "위장장애, 설사, 어지럼증, 간기능 저하 (드물게)",
        "의사상담": "✅",
        "이유": "내분비 민감형 생리통: 강한 복부·골반 통증 및 식욕 저하에 사용.",
        "이미지": ["mefenamic.png"]
    }
}

# 증상 분류 함수
def classify(sym_type, answers):
    if sym_type == "두통":
        if answers[0] == "관자놀이" and answers[1] == "밝은 빛" and answers[2] in ["구토", "눈부심"]:
            return "트립탄"
        elif answers[3] == "예":
            return "아세트아미노펜"
        elif answers[0] == "머리 전체" or answers[1] == "스트레스" or answers[2] == "목 뻣뻣함":
            return "이부프로펜"
        else:
            return "나프록센"
    else:
        if answers[2] == "예":
            return "아세트아미노펜"
        elif answers[3] in ["어지러움", "식욕 부진"] or answers[1] == "골반 깊은 곳":
            return "메페남산"
        elif answers[0] == "생리 시작 전":
            return "나프록센"
        else:
            return "이부프로펜"

# 앱 동작 흐름
def main():
    if st.session_state.page == 'home':
        st.title("두통 / 생리통 약 추천")
        if st.button("🧠 두통"):
            st.session_state.answers["선택"] = "두통"
            st.session_state.page = "질문"
            st.session_state.step = 0
        if st.button("🩸 생리통"):
            st.session_state.answers["선택"] = "생리통"
            st.session_state.page = "질문"
            st.session_state.step = 0

    elif st.session_state.page == "질문":
        typ = st.session_state.answers["선택"]
        questions = headache_questions if typ == "두통" else period_questions
        step = st.session_state.step

        st.header(f"{typ} 증상 질문 ({step+1}/4)")
        q, options = questions[step]
        selected = st.radio(q, options, key=f"{typ}_{step}")

        if st.button("다음"):
            st.session_state.answers[f"{typ}_{step}"] = selected
            st.session_state.step += 1
            if st.session_state.step >= 4:
                st.session_state.page = "결과"

    elif st.session_state.page == "결과":
        typ = st.session_state.answers["선택"]
        answers = [st.session_state.answers[f"{typ}_{i}"] for i in range(4)]
        med_key = classify(typ, answers)
        med = medications[med_key]

        st.title("💊 추천 약")
        st.subheader(med_key)
        for img in med["이미지"]:
            try:
                st.image(img, use_container_width=True)
            except:
                st.warning(f"{img} 이미지를 불러올 수 없습니다.")

        st.markdown(f"**📌 효능:** {med['효능']}")
        st.markdown(f"**⚠️ 부작용:** {med['부작용']}")
        st.markdown(f"**🩺 의사 상담 필요 여부:** {med['의사상담']}")
        st.markdown(f"**✅ 추천 이유:** {med['이유']}")

        if st.button("🔁 처음으로 돌아가기"):
            st.session_state.page = "home"
            st.session_state.answers = {}
            st.session_state.step = 0

main()
