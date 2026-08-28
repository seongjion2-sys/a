<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>인간 키우기 프로토타입</title>
    <style>
        /* 기본 스타일: UI 이미지와 유사하게 설정 */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            font-family: 'Malgun Gothic', sans-serif;
            overflow: hidden; /* 스크롤 방지 */
        }

        #game-container {
            width: 100vw;
            height: calc(100vw * (9/16)); /* 16:9 비율 유지 */
            max-width: 1920px;
            max-height: 1080px;
            background-image: url('background.jpg'); /* 거실 배경 이미지 */
            background-size: cover;
            background-position: center;
            position: relative;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        /* 아기 이미지 스타일 */
        #baby {
            position: absolute;
            bottom: 30%; /* 거실 바닥 쯤 위치 */
            left: 50%;
            transform: translateX(-50%);
            height: 25%; /* 아기 크기 */
            transition: transform 0.3s ease; /* 움직임 애니메이션 */
        }

        /* 하단 UI 패널 */
        #ui-panel {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 18%; /* 하단 UI 높이 */
            background-color: #f5f5f5; /* 밝은 회색 */
            border-top: 1px solid #dcdcdc;
            display: flex;
            flex-direction: column;
            padding: 1% 2%;
            box-sizing: border-box;
        }

        /* 상태 표시바 (나이, 기분) */
        #status-bar {
            background-color: #333;
            color: white;
            border-radius: 50px;
            padding: 5px 15px;
            display: inline-flex;
            gap: 20px;
            font-size: 1.2rem;
            align-self: center; /* 중앙 정렬 */
            margin-bottom: 1%;
        }

        /* 버튼 컨테이너 */
        #button-container {
            display: flex;
            justify-content: center;
            gap: 15px;
            width: 100%;
        }

        /* 기본 버튼 스타일 */
        .game-button {
            flex: 1; /* 동일 비율 크기 */
            max-width: 150px;
            height: 60px;
            background-color: white;
            border: 1px solid #dcdcdc;
            border-radius: 10px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: background 0.2s, transform 0.1s;
        }

        .game-button:hover { background-color: #e9e9e9; }
        .game-button:active { transform: scale(0.98); }

        .button-icon { font-size: 1.2rem; margin-bottom: 3px; }
        .button-text { font-size: 0.9rem; color: #333; font-weight: bold; }

    </style>
</head>
<body>

    <div id="game-container">
        <img src="baby.png" alt="아기" id="baby">

        <div id="ui-panel">
            <div id="status-bar">
                <span id="age-display">나이: 1세</span>
                <span id="mood-display">기분: 우는 중</span>
            </div>

            <div id="button-container">
                <div class="game-button" onclick="playGame('upgrade')">
                    <span class="button-icon">⚙️</span>
                    <span class="button-text">업그레이드</span>
                </div>
                <div class="game-button" onclick="playGame('grow')">
                    <span class="button-icon">📈</span>
                    <span class="button-text">성장</span>
                </div>
                <div class="game-button" onclick="playGame('status')">
                    <span class="button-icon">❤️</span>
                    <span class="button-text">상태</span>
                </div>
                <div class="game-button" onclick="playGame('bg')">
                    <span class="button-icon">🖼️</span>
                    <span class="button-text">배경</span>
                </div>
                <div class="game-button" onclick="playGame('option')">
                    <span class="button-icon">⚙️</span>
                    <span class="button-text">옵션</span>
                </div>
            </div>
        </div>
    </div>

    <script>
        // 간단한 게임 로직
        let age = 1;
        const babyEl = document.getElementById('baby');
        const ageDisplay = document.getElementById('age-display');
        const moodDisplay = document.getElementById('mood-display');

        function playGame(action) {
            switch(action) {
                case 'grow':
                    age++;
                    ageDisplay.innerText = `나이: ${age}세`;
                    moodDisplay.innerText = "기분: 행복함 😊";
                    // 성장 시 아기 크기가 조금 커짐
                    babyEl.style.height = `${25 + age}%`; 
                    break;
                case 'status':
                    alert(`현재 아기 상태\n나이: ${age}세\n기분: ${moodDisplay.innerText}`);
                    break;
                default:
                    moodDisplay.innerText = "기분: 궁금함 🤔";
                    break;
            }
        }
    </script>
</body>
</html>
