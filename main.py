import os
from PIL import Image
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Baby in the Living Room", page_icon="👶", layout="centered"
)

st.title("👶 거실에 앉아있는 아기")

# 이미지 파일 경로 설정
image_path = "baby.png"

# 이미지가 존재하는지 확인 후 표시
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption="거실 한가운데 무표정으로 앉아있는 아기", use_column_width=True)
else:
    st.error(
        f"'{image_path}' 이미지를 찾을 수 없습니다. 깃허브 리포지토리에 'baby.png' 파일을 업로드했는지 확인해 주세요."
    )
