import base64
import os
import streamlit as st

# 페이지 기본 설정 (와이드 레이아웃 사용)
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
    return ""


# 합성된 이미지 파일명 (깃허브 리포지토리에 이 파일명으로 저장해주세요)
IMAGE_PATH = "combined_image.png"
img_base64 = get_base64_image(IMAGE_PATH)

# 화면 전체를 채우는 CSS 및 UI 스타일링
st.markdown(
    f"""
    <style>
    /* Streamlit 기본 여백 제거 및 전체 화면 설정 */
    #root > div:nth-child(1) > div > div > div {{
        padding: 0px !important;
    }}
    .stAppHeader {{
        display: none;
    }}
    .stMainBlockContainer {{
        padding: 0px !important;
        max-width: 100% !important;
    }}
    
    /* 전체 화면 배경 이미지 */
    .full-screen-bg {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-image: url('data:image/png;base64,{img_base64}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        z-index: 0;
    }}

    /* 하단 오버레이 레이아웃 컨테이너 */
    .bottom-ui-container {{
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 800px;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    /* 상태 표시줄 */
    .status-bar {{
        background: rgba(30, 30, 30, 0.85);
        backdrop-filter: blur(5px);
        color: white;
        text-align: center;
        padding: 8px 30px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 20px;
        margin-bottom: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}

    /* 버튼 스타일 Custom */
    div.stButton > button {{
        width: 100%;
        height: 65px;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        background: rgba(255, 255, 255, 0.85) !important;
        backdrop-filter: blur(8px) !important;
        color: #222222 !important;
        font-weight: bold !important;
        font-size: 15px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
        transition: all 0.2s ease-in-out;
    }}

    div.stButton > button:hover {{
        background: rgba(255, 255, 255, 1.0) !important;
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.25) !important;
    }}
    </style>

    <!-- 배경 이미지 래퍼 -->
    <div class="full-screen-bg"></div>
""",
    unsafe_allow_html=True,
)

# 하단 UI 위치 구성을 위한 레이아웃
st.markdown('<div style="height: 72vh;"></div>', unsafe_allow_html=True)

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
