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


# 변경하신 이미지 파일명 설정
IMAGE_PATH = "baby.png"
img_base64 = get_base64_image(IMAGE_PATH)

# 이미지 파일이 없을 경우 경고 메시지 표시
if img_base64 is None:
    st.warning(
        f"⚠️ '{IMAGE_PATH}' 파일이 깃허브 메인 폴더(루트)에 없습니다. 파일명을 확인해 주세요."
    )

# 전체 화면 배경 및 UI 커스텀 CSS
st.markdown(
    f"""
    <style>
    /* 상단 헤더 및 기본 여백 제거 */
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
    
    /* 화면 전체에 baby.png 배경 설정 */
    .stApp {{
        background: url('data:image/png;base64,{img_base64 if img_base64 else ""}') no-repeat center center fixed !important;
        background-size: cover !important;
    }}

    /* 상태 표시줄 */
    .status-bar {{
        background: rgba(30, 30, 30, 0.85);
        color: white;
        text-align: center;
        padding: 8px 30px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 15px;
    }}

    /* 하단 버튼 스타일 */
    div.stButton > button {{
        width: 100%;
        height: 65px;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        background: rgba(255, 255, 255, 0.9) !important;
        color: #222222 !important;
        font-weight: bold !important;
        font-size: 15px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2) !important;
        transition: all 0.2s ease-in-out;
    }}

    div.stButton > button:hover {{
        background: rgba(255, 255, 255, 1.0) !important;
        transform: translateY(-3px);
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# 하단 UI 위치 맞춤용 여백
st.markdown('<div style="height: 70vh;"></div>', unsafe_allow_html=True)

# 1. 상태 표시줄 (나이, 기분)
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <div class="status-bar">
            나이: 1세 &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; 기분: 우는 중
        </div>
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
