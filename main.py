import base64
import os
import streamlit as st

# 페이지 구성
st.set_page_config(
    page_title="아기 키우기 게임", page_icon="👶", layout="centered"
)


# 이미지를 Base64로 변환하는 함수 (HTML/CSS 사용용)
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""


# 이미지 파일 경로 (깃허브 리포지토리에 포함되어야 함)
BG_IMAGE_PATH = "living_room.jpg"  # 거실 배경 이미지
BABY_IMAGE_PATH = "baby.png"  # 울고 있는 아기 이미지 (배경 투명 PNG 권장)

bg_base64 = get_base64_image(BG_IMAGE_PATH)
baby_base64 = get_base64_image(BABY_IMAGE_PATH)

# 화면 스타일링 (Custom CSS)
st.markdown(
    f"""
    <style>
    /* 전체 배경 스타일 */
    .stApp {{
        background-color: #eef2f5;
    }}
    
    /* 게임 메인 컨테이너 */
    .game-container {{
        position: relative;
        width: 100%;
        max-width: 900px;
        height: 520px;
        margin: 0 auto;
        background-image: url('data:image/jpeg;base64,{bg_base64}');
        background-size: cover;
        background-position: center;
        border-radius: 12px 12px 0 0;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
        overflow: hidden;
    }}

    /* 테이블 위 아기 이미지 위치 */
    .baby-image {{
        position: absolute;
        bottom: 80px;
        left: 50%;
        transform: translateX(-50%);
        width: 180px;
        z-index: 10;
    }}

    /* 상태 표시줄 (나이, 기분) */
    .status-bar {{
        background-color: #2b2b2b;
        color: white;
        text-align: center;
        padding: 8px 20px;
        font-size: 15px;
        font-weight: 500;
        border-radius: 20px;
        width: 60%;
        margin: -20px auto 15px auto;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        position: relative;
        z-index: 20;
    }}

    /* Streamlit 버튼 스타일 커스텀 */
    div.stButton > button {{
        width: 100%;
        height: 60px;
        border-radius: 12px !important;
        border: 1px solid #dcdcdc !important;
        background-color: #ffffff !important;
        color: #333333 !important;
        font-weight: bold !important;
        font-size: 15px !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08) !important;
        transition: all 0.2s ease-in-out;
    }}

    div.stButton > button:hover {{
        background-color: #f0f4f8 !important;
        border-color: #b0bec5 !important;
        transform: translateY(-2px);
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# 1. 게임 메인 화면 (거실 배경 + 아기)
st.markdown(
    f"""
    <div class="game-container">
        {"<img src='data:image/png;base64," + baby_base64 + "' class='baby-image'>" if baby_base64 else ""}
    </div>
""",
    unsafe_allow_html=True,
)

# 2. 상태 표시줄
st.markdown(
    """
    <div class="status-bar">
        나이: 1세 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 기분: 우는 중
    </div>
""",
    unsafe_allow_html=True,
)

# 3. 하단 메뉴 버튼 (5개 컬럼)
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
