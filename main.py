import tkinter as tk


class BabyGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Baby in the Living Room")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # 캔버스 생성
        self.canvas = tk.Canvas(root, width=800, height=600, bg="#F5E6CA")
        self.canvas.pack()

        self.draw_room()
        self.draw_baby()

    def draw_room(self):
        """거실 배경 그리기"""
        # 벽과 바닥 구분선
        self.canvas.create_rectangle(
            0, 0, 800, 420, fill="#FFF8E7", outline=""
        )  # 벽
        self.canvas.create_rectangle(
            0, 420, 800, 600, fill="#D2B48C", outline=""
        )  # 목재 바닥
        self.canvas.create_line(0, 420, 800, 420, fill="#A0522D", width=4)

        # 창문
        self.canvas.create_rectangle(
            100, 80, 260, 240, fill="#E0F7FA", outline="#8D6E63", width=6
        )
        self.canvas.create_line(
            180, 80, 180, 240, fill="#8D6E63", width=4
        )  # 창틀 세로
        self.canvas.create_line(
            100, 160, 260, 160, fill="#8D6E63", width=4
        )  # 창틀 가로

        # 창밖 구름
        self.canvas.create_oval(
            130, 110, 190, 140, fill="#FFFFFF", outline=""
        )
        self.canvas.create_oval(
            160, 120, 220, 150, fill="#FFFFFF", outline=""
        )

        # 거실 러그 (아기가 앉아있는 곳)
        self.canvas.create_oval(
            280, 430, 520, 530, fill="#E6E6FA", outline="#D8BFD8", width=3
        )

        # 액자
        self.canvas.create_rectangle(
            580, 100, 700, 200, fill="#FFF8DC", outline="#5D4037", width=5
        )
        self.canvas.create_polygon(
            600, 180, 640, 130, 680, 180, fill="#81C784", outline=""
        )  # 액자 속 산

        # 화분
        self.canvas.create_polygon(
            680, 440, 700, 370, 740, 370, 760, 440, fill="#A0522D", outline=""
        )  # 화분
        self.canvas.create_oval(
            690, 300, 750, 380, fill="#4CAF50", outline=""
        )  # 식물 잎

    def draw_baby(self):
        """무표정으로 앉아있는 아기 그리기"""
        cx, cy = 400, 440  # 아기의 중심 좌표

        # 몸통 (앉아있는 자세)
        self.canvas.create_oval(
            cx - 35, cy - 10, cx + 35, cy + 40, fill="#FFB7C5", outline="#E91E63"
        )  # 분홍색 우주복

        # 다리 (양쪽으로 펴고 앉음)
        self.canvas.create_oval(
            cx - 50, cy + 15, cx - 20, cy + 40, fill="#FFB7C5", outline="#E91E63"
        )
        self.canvas.create_oval(
            cx + 20, cy + 15, cx + 50, cy + 40, fill="#FFB7C5", outline="#E91E63"
        )

        # 팔
        self.canvas.create_oval(
            cx - 40, cy, cx - 20, cy + 25, fill="#FF8A80", outline=""
        )
        self.canvas.create_oval(
            cx + 20, cy, cx + 40, cy + 25, fill="#FF8A80", outline=""
        )

        # 머리
        self.canvas.create_oval(
            cx - 40,
            cy - 80,
            cx + 40,
            cy,
            fill="#FFD1DC",
            outline="#FF8A80",
            width=2,
        )

        # 머리카락 한 가닥
        self.canvas.create_arc(
            cx - 5,
            cy - 95,
            cx + 15,
            cy - 75,
            start=40,
            extent=120,
            style=tk.ARC,
            width=3,
            outline="#424242",
        )

        # --- 무표정 얼굴 ---
        # 눈 (동그랗고 일자 느낌의 무표정한 눈)
        self.canvas.create_oval(
            cx - 20, cy - 50, cx - 12, cy - 42, fill="#212121", outline=""
        )
        self.canvas.create_oval(
            cx + 12, cy - 50, cx + 20, cy - 42, fill="#212121", outline=""
        )

        # 코 (작은 점)
        self.canvas.create_oval(
            cx - 2, cy - 38, cx + 2, cy - 34, fill="#E57373", outline=""
        )

        # 입 (일자 무표정)
        self.canvas.create_line(
            cx - 10, cy - 25, cx + 10, cy - 25, fill="#212121", width=3
        )

        # 볼터치 (약간의 온기)
        self.canvas.create_oval(
            cx - 30, cy - 38, cx - 20, cy - 30, fill="#FF8A80", outline=""
        )
        self.canvas.create_oval(
            cx + 20, cy - 38, cx + 30, cy - 30, fill="#FF8A80", outline=""
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = BabyGame(root)
    root.mainloop()
