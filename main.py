import base64
import os
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="아기 키우기 게임",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# 이미지를 Base64로 변환하는 함수
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None


# 이미지 파일명 설정 (baby.png)
IMAGE_PATH = "baby.png"
img_base64 = get_base64_image(IMAGE_PATH)

if img_base64 is None:
    st.warning(
        f"⚠️ '{IMAGE_PATH}' 파일이 깃허브 메인 폴더(루트)에 없습니다. 파일명을 확인해 주세요."
    )

# CSS 스타일 적용
st.markdown(
    f"""
    <style>
    /* 여백 및 헤더 제거 */
    header {{
        visibility: hidden;
    }}
    .stAppViewContainer {{
        padding: 0 !important;
        margin: 0 !important;
    }}
    .stMainBlockContainer {{
        padding: 0 !important;
        max-width: 100% !important;
    }}
    
    /* 화면 전체 영역 설정 (어두운 배경색으로 여백 처리) */
    .stApp {{
        background-color: #1a1a1a !important;
        background-image: url('data:image/png;base64,{img_base64 if img_base64 else ""}');
        background-repeat: no-repeat !important;
        background-position: center center !important;
        /* contain 옵션을 사용해 이미지가 짤리지 않고 전체가 다 나오도록 설정 */
        background-size: contain !important;
    }}

    /* 하단 UI 컨테이너 스타일 */
    .bottom-ui {{
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 800px;
        z-index: 999;
    }}

    /* 상태 표시줄 */
    .status-bar {{
        background: rgba(0, 0, 0, 0.75);
        color: white;
        text-align: center;
        padding: 8px 25px;
        font-size: 15px;
        font-weight: 600;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 0 auto 12px auto;
        width: fit-content;
    }}

    /* 버튼 스타일 */
    div.stButton > button {{
        width: 100%;
        height: 60px;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        background: rgba(255, 255, 255, 0.85) !important;
        backdrop-filter: blur(4px);
        color: #111111 !important;
        font-weight: bold !important;
        font-size: 14px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
        transition: all 0.2s ease-in-out;
    }}

    div.stButton > button:hover {{
        background: rgba(255, 255, 255, 1.0) !important;
        transform: translateY(-2px);
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# 하단 버튼 레이아웃 구성
st.markdown('<div class="bottom-ui">', unsafe_allow_html=True)

# 1. 상태 표시줄 (나이, 기분)
st.markdown(
    """
    <div class="status-bar">
        나이: 1세 &nbsp;&nbsp;|&nbsp;&nbsp; 기분: 우는 중
    </div>
""",
    unsafe_allow_html=True,
)

# 2. 하단 메뉴 버튼 5개
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("⚙️\n업그레이드"):
        st.toast("업그레이드 메뉴 클릭!")

with col2:
    if st.button("📈\n성장"):
        st.toast("성장 메뉴 클릭!")

with col3:
    if st.button("❤️\n상태"):
        st.toast("상태 메뉴 클릭!")

with col4:
    if st.button("🖼️\n배경"):
        st.toast("배경 변경 클릭!")

with col5:
    if st.button("⚙️\n옵션"):
        st.toast("옵션 메뉴 클릭!")

st.markdown("</div>", unsafe_allow_html=True)
