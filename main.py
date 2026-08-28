import streamlit as st

st.set_page_config(
    page_title="Baby in the Living Room", page_icon="👶", layout="centered"
)

st.title("👶 거실에 앉아있는 아기")

# HTML5 Canvas를 활용해 화면을 그리는 코드
canvas_html = """
<div style="display: flex; justify-content: center; align-items: center;">
    <canvas id="gameCanvas" width="800" height="600" style="border: 2px solid #333; border-radius: 8px; background-color: #F5E6CA;"></canvas>
</div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

function drawRoom() {
    // 벽과 바닥
    ctx.fillStyle = '#FFF8E7';
    ctx.fillRect(0, 0, 800, 420); // 벽
    ctx.fillStyle = '#D2B48C';
    ctx.fillRect(0, 420, 800, 180); // 바닥
    
    ctx.strokeStyle = '#A0522D';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(0, 420);
    ctx.lineTo(800, 420);
    ctx.stroke();

    // 창문
    ctx.fillStyle = '#E0F7FA';
    ctx.strokeStyle = '#8D6E63';
    ctx.lineWidth = 6;
    ctx.fillRect(100, 80, 160, 160);
    ctx.strokeRect(100, 80, 160, 160);

    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(180, 80); ctx.lineTo(180, 240);
    ctx.moveTo(100, 160); ctx.lineTo(260, 160);
    ctx.stroke();

    // 구름
    ctx.fillStyle = '#FFFFFF';
    ctx.beginPath();
    ctx.arc(150, 125, 20, 0, Math.PI * 2);
    ctx.arc(180, 130, 25, 0, Math.PI * 2);
    ctx.fill();

    // 러그
    ctx.fillStyle = '#E6E6FA';
    ctx.strokeStyle = '#D8BFD8';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.ellipse(400, 480, 120, 50, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // 액자
    ctx.fillStyle = '#FFF8DC';
    ctx.strokeStyle = '#5D4037';
    ctx.lineWidth = 5;
    ctx.fillRect(580, 100, 120, 100);
    ctx.strokeRect(580, 100, 120, 100);

    ctx.fillStyle = '#81C784';
    ctx.beginPath();
    ctx.moveTo(600, 180);
    ctx.lineTo(640, 130);
    ctx.lineTo(680, 180);
    ctx.fill();

    // 화분
    ctx.fillStyle = '#A0522D';
    ctx.beginPath();
    ctx.moveTo(680, 440);
    ctx.lineTo(700, 370);
    ctx.lineTo(740, 370);
    ctx.lineTo(760, 440);
    ctx.fill();

    ctx.fillStyle = '#4CAF50';
    ctx.beginPath();
    ctx.arc(720, 340, 30, 0, Math.PI * 2);
    ctx.fill();
}

function drawBaby() {
    const cx = 400;
    const cy = 440;

    // 몸통 (분홍색 옷)
    ctx.fillStyle = '#FFB7C5';
    ctx.strokeStyle = '#E91E63';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.ellipse(cx, cy + 15, 35, 25, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // 다리
    ctx.beginPath();
    ctx.ellipse(cx - 35, cy + 28, 15, 12, 0, 0, Math.PI * 2);
    ctx.ellipse(cx + 35, cy + 28, 15, 12, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // 팔
    ctx.fillStyle = '#FF8A80';
    ctx.beginPath();
    ctx.arc(cx - 30, cy + 12, 10, 0, Math.PI * 2);
    ctx.arc(cx + 30, cy + 12, 10, 0, Math.PI * 2);
    ctx.fill();

    // 머리
    ctx.fillStyle = '#FFD1DC';
    ctx.strokeStyle = '#FF8A80';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(cx, cy - 40, 40, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    // 머리카락
    ctx.strokeStyle = '#424242';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.arc(cx + 5, cy - 82, 10, Math.PI * 0.8, Math.PI * 1.5);
    ctx.stroke();

    // 눈 (무표정)
    ctx.fillStyle = '#212121';
    ctx.beginPath();
    ctx.arc(cx - 16, cy - 46, 4, 0, Math.PI * 2);
    ctx.arc(cx + 16, cy - 46, 4, 0, Math.PI * 2);
    ctx.fill();

    // 코
    ctx.fillStyle = '#E57373';
    ctx.beginPath();
    ctx.arc(cx, cy - 36, 2, 0, Math.PI * 2);
    ctx.fill();

    // 입 (일자)
    ctx.strokeStyle = '#212121';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(cx - 10, cy - 25);
    ctx.lineTo(cx + 10, cy - 25);
    ctx.stroke();

    // 볼터치
    ctx.fillStyle = '#FF8A80';
    ctx.beginPath();
    ctx.arc(cx - 25, cy - 34, 5, 0, Math.PI * 2);
    ctx.arc(cx + 25, cy - 34, 5, 0, Math.PI * 2);
    ctx.fill();
}

drawRoom();
drawBaby();
</script>
"""

st.components.v1.html(canvas_html, height=650)
