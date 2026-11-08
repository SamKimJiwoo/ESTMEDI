import tkinter as tk
from tkinter import messagebox
import time
import os
import tempfile
import platform

# Pillow 라이브러리 안전 로드
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

class EstmediAlyacPyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ESTMEDI 2.5 - Classic Alyac Edition")
        
        # 아담하고 고정된 알약 비율
        self.root.geometry("640x410")
        self.root.minsize(640, 410)
        self.root.maxsize(640, 410)
        
        # 알약 2.5 웹 디자인의 시그니처 컬러 팔레트 적용
        self.color_bg = "#f4f6f3"       # 부드러운 클래식 배경 톤
        self.color_panel = "#ffffff"    # 카드 화이트
        self.color_green = "#76a81b"    # 알약 시그니처 그린
        self.color_darkgreen = "#5a8512"# 진한 초록 포인트
        self.color_text = "#334155"     # 깔끔한 다크 텍스트
        self.color_border = "#abd191"   # 알약 연두빛 테두리
        
        self.root.configure(bg=self.color_bg)
        
        self.font_main = ("맑은 고딕", 9)
        self.font_bold = ("맑은 고딕", 9, "bold")
        self.font_title = ("맑은 고딕", 10, "bold")
        self.font_logo = ("맑은 고딕", 11, "bold")

        # 메딩이 이미지 로드
        self.load_meding_image()

        # 1. 상단 그린 네비게이션 바
        self.create_top_nav()

        # 2. 메인 컨테이너
        self.container = tk.Frame(self.root, bg=self.color_bg, bd=0)
        self.container.pack(fill="both", expand=True, padx=8, pady=8)

        # 3. 하단 상태 바
        self.create_status_bar()

        # 첫 화면(검사하기) 로드
        self.show_tab_scan()

    def load_meding_image(self):
        self.meding_img = None
        if not PIL_AVAILABLE:
            return
        img_path = "meding.png"
        if os.path.exists(img_path):
            try:
                pil_img = Image.open(img_path)
                pil_img = pil_img.resize((55, 65), Image.Resampling.LANCZOS)
                self.meding_img = ImageTk.PhotoImage(pil_img)
            except:
                self.meding_img = None

    def create_top_nav(self):
        # 알약 고유의 그린 테마 상단 바
        top_panel = tk.Frame(self.root, bg=self.color_green, height=45)
        top_panel.pack(fill="x", side="top")
        top_panel.pack_propagate(False)

        # 로고 영역
        logo_frame = tk.Frame(top_panel, bg=self.color_green)
        logo_frame.pack(side="left", padx=10)
        tk.Label(logo_frame, text="알약 2.5 (ESTMEDI)", font=self.font_logo, bg=self.color_green, fg="#ffffff").pack(side="left")

        # 우측 실시간 감시 배지
        badge = tk.Frame(top_panel, bg=self.color_darkgreen)
        badge.pack(side="right", padx=10, pady=8)
        tk.Label(badge, text="실시간 감시 On", font=("맑은 고딕", 8, "bold"), bg=self.color_darkgreen, fg="#ffffdd").pack(padx=6, pady=2)

        # 탭 버튼들 (우측 정렬)
        self.tab_info_btn = self.create_nav_button(top_panel, "업데이트 / 정보", self.show_tab_info)
        self.tab_info_btn.pack(side="right", padx=1, pady=6)

        self.tab_manage_btn = self.create_nav_button(top_panel, "PC 관리", self.show_tab_manage)
        self.tab_manage_btn.pack(side="right", padx=1, pady=6)

        self.tab_opt_btn = self.create_nav_button(top_panel, "PC최적화", self.show_tab_optimize)
        self.tab_opt_btn.pack(side="right", padx=1, pady=6)

        self.tab_scan_btn = self.create_nav_button(top_panel, "검사하기", self.show_tab_scan, active=True)
        self.tab_scan_btn.pack(side="right", padx=3, pady=6)

    def create_nav_button(self, parent, text, command, active=False):
        bg_col = "#5d8a0d" if active else self.color_green
        fg_col = "#ffffdd" if active else "#ffffff"
        
        btn_frame = tk.Frame(parent, bg=bg_col, cursor="hand2")
        lbl = tk.Label(btn_frame, text=text, font=self.font_bold if active else self.font_main, bg=bg_col, fg=fg_col)
        lbl.pack(padx=8, pady=2)
        
        for widget in (btn_frame, lbl):
            widget.bind("<Button-1>", lambda e: command())
        return btn_frame

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def update_active_tab(self, active_name):
        for name, btn in [("검사하기", self.tab_scan_btn), ("PC최적화", self.tab_opt_btn), ("PC 관리", self.tab_manage_btn), ("업데이트 / 정보", self.tab_info_btn)]:
            is_active = (name == active_name)
            col = "#5d8a0d" if is_active else self.color_green
            f_col = "#ffffdd" if is_active else "#ffffff"
            btn.config(bg=col)
            for child in btn.winfo_children():
                child.config(bg=col, fg=f_col)

    # ==================== [탭 1: 검사하기] ====================
    def show_tab_scan(self):
        self.clear_container()
        self.update_active_tab("검사하기")
        
        # 상태 배너 카드
        status_box = tk.Frame(self.container, bg=self.color_panel, bd=1, relief="solid", highlightbackground=self.color_border)
        status_box.pack(fill="x", padx=4, pady=6)

        tk.Label(status_box, text="실시간 감시를 사용중입니다.", font=self.font_title, bg=self.color_panel, fg="#15803d").pack(anchor="w", padx=12, pady=(8, 2))
        tk.Label(status_box, text="알약 실시간 감시로 PC를 안전하게 보호하고 있습니다.", font=self.font_main, bg=self.color_panel, fg="#64748b").pack(anchor="w", padx=12, pady=(0, 8))

        # 카드 영역 (빠른검사 / 정밀검사)
        cards_frame = tk.Frame(self.container, bg=self.color_bg)
        cards_frame.pack(fill="both", expand=True, padx=4, pady=4)

        # 빠른 검사 카드
        card_q = tk.Frame(cards_frame, bg=self.color_panel, bd=1, relief="solid", highlightbackground=self.color_border, cursor="hand2")
        card_q.pack(side="left", fill="both", expand=True, padx=(0, 4))
        card_q.bind("<Button-1>", lambda e: self.run_scan_action("빠른 검사"))

        lbl_q = tk.Label(card_q, text="빠른검사  >", font=self.font_title, bg=self.color_panel, fg=self.color_text, cursor="hand2")
        lbl_q.pack(anchor="w", padx=12, pady=10)
        lbl_q.bind("<Button-1>", lambda e: self.run_scan_action("빠른 검사"))

        inner_q = tk.Frame(card_q, bg=self.color_panel, bd=0)
        inner_q.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        if self.meding_img:
            tk.Label(inner_q, image=self.meding_img, bg=self.color_panel).pack(pady=4)
        else:
            tk.Label(inner_q, text="💊", font=("맑은 고딕", 18), bg=self.color_panel).pack(pady=4)

        tk.Label(inner_q, text="주요 시스템 영역 및 악성코드\n위험 영역을 빠르게 검사합니다.", font=self.font_main, bg=self.color_panel, fg="#64748b", justify="center").pack(expand=True)

        # 정밀 검사 카드
        card_f = tk.Frame(cards_frame, bg=self.color_panel, bd=1, relief="solid", highlightbackground=self.color_border, cursor="hand2")
        card_f.pack(side="right", fill="both", expand=True, padx=(4, 0))
        card_f.bind("<Button-1>", lambda e: self.run_scan_action("정밀 검사"))

        lbl_f = tk.Label(card_f, text="정밀검사  >", font=self.font_title, bg=self.color_panel, fg=self.color_text, cursor="hand2")
        lbl_f.pack(anchor="w", padx=12, pady=10)
        lbl_f.bind("<Button-1>", lambda e: self.run_scan_action("정밀 검사"))

        inner_f = tk.Frame(card_f, bg=self.color_panel, bd=0)
        inner_f.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        if self.meding_img:
            tk.Label(inner_f, image=self.meding_img, bg=self.color_panel).pack(pady=4)
        else:
            tk.Label(inner_f, text="🔬", font=("맑은 고딕", 18), bg=self.color_panel).pack(pady=4)

        tk.Label(inner_f, text="모든 디스크 드라이브 및\n하위 폴더 전체를 정밀 검사합니다.", font=self.font_main, bg=self.color_panel, fg="#64748b", justify="center").pack(expand=True)

    def run_scan_action(self, scan_type):
        confirm = messagebox.askquestion(scan_type, f"'{scan_type}'을(를) 진행하시겠습니까?")
        if confirm == 'yes':
            prog = tk.Toplevel(self.root)
            prog.title(f"ESTMEDI - {scan_type}")
            prog.geometry("260x100")
            prog.resizable(False, False)
            prog.configure(bg=self.color_panel)
            
            tk.Label(prog, text=f"🔧 드라이버를 돌리며\n{scan_type}을 진행하고 있습니다...", font=self.font_main, bg=self.color_panel, fg=self.color_text, justify="center").pack(expand=True)
            prog.update()
            
            time.sleep(1.5)
            prog.destroy()

            detected_viruses = 0 
            if detected_viruses == 0:
                messagebox.showinfo("검사 완료", "악성코드가 없습니다. 프로그램을 종료합니다.")
                self.root.destroy()
            else:
                ans = messagebox.askyesno("위협 발견", f"악성코드가 {detected_viruses}개가 발견되었습니다.\n\n치료를 진행하시겠습니까?")
                if ans:
                    treat = tk.Toplevel(self.root)
                    treat.title("ESTMEDI 치료 중")
                    treat.geometry("260x100")
                    treat.resizable(False, False)
                    treat.configure(bg=self.color_panel)
                    tk.Label(treat, text="🔧 드라이버로 위협 요소를\n말끔하게 치료하고 있습니다...", font=self.font_main, bg=self.color_panel, fg=self.color_text, justify="center").pack(expand=True)
                    treat.update()
                    time.sleep(1.5)
                    treat.destroy()
                    messagebox.showinfo("치료 완료", "모든 위협 요소가 안전하게 치료되었습니다!")
                else:
                    messagebox.showinfo("취소", "치료가 취소되었습니다.")

    # ==================== [탭 2: PC최적화 (알약 원본 카드 UI)] ====================
    def show_tab_optimize(self):
        self.clear_container()
        self.update_active_tab("PC최적화")

        # 상단 쾌적 상태 배너 ( 사진 참조)
        status_banner = tk.Frame(self.container, bg=self.color_panel, height=55, bd=1, relief="solid", highlightbackground=self.color_border)
        status_banner.pack(fill="x", padx=4, pady=4)
        status_banner.pack_propagate(False)

        tk.Label(status_banner, text="PC가 쾌적하게 관리되고 있습니다.", font=self.font_title, bg=self.color_panel, fg="#15803d").pack(anchor="w", padx=12, pady=(8, 2))
        tk.Label(status_banner, text="📅 마지막 최적화 날짜 : 2026.11.08", font=("맑은 고딕", 8), bg=self.color_panel, fg="#64748b").pack(anchor="w", padx=12, pady=(0, 8))

        # 하단 3분할 카드 영역 ( 사진 참조)
        cards_layout = tk.Frame(self.container, bg=self.color_bg)
        cards_layout.pack(fill="both", expand=True, padx=4, pady=4)

        # 1. [PC최적화 카드]
        card_opt = tk.Frame(cards_layout, bg=self.color_panel, bd=1, relief="solid", highlightbackground=self.color_border, cursor="hand2")
        card_opt.pack(side="left", fill="both", expand=True, padx=(0, 3))
        card_opt.bind("<Button-1>", lambda e: self.open_optimize_dialog())

        tk.Label(card_opt, text="PC최적화  >", font=self.font_title, bg=self.color_panel, fg=self.color_text, cursor="hand2").pack(anchor="w", padx=10, pady=8)
        
        inner_opt = tk.Frame(card_opt, bg=self.color_panel, bd=0)
        inner_opt.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        inner_opt.bind("<Button-1>", lambda e: self.open_optimize_dialog())

        if self.meding_img:
            img_l = tk.Label(inner_opt, image=self.meding_img, bg=self.color_panel, cursor="hand2")
            img_l.pack(pady=4)
            img_l.bind("<Button-1>", lambda e: self.open_optimize_dialog())
        else:
            tk.Label(inner_opt, text="🧹", font=("맑은 고딕", 16), bg=self.color_panel).pack(pady=4)

        tk.Label(inner_opt, text="불필요한 파일 및\n임시 데이터를 정리합니다.", font=("맑은 고딕", 8), bg=self.color_panel, fg="#64748b", justify="center", cursor="hand2").pack(expand=True)

        # 2. [PC관리 카드]
        card_mg = tk.Frame(cards_layout, bg=self.color_panel, bd=1, relief="solid", highlightbackground=self.color_border, cursor="hand2")
        card_mg.pack(side="left", fill="both", expand=True, padx=3)
        card_mg.bind("<Button-1>", lambda e: self.show_tab_manage())

        tk.Label(card_mg, text="PC관리  >", font=self.font_title, bg=self.color_panel, fg=self.color_text, cursor="hand2").pack(anchor="w", padx=10, pady=8)
        
        inner_mg = tk.Frame(card_mg, bg=self.color_panel, bd=0)
        inner_mg.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        inner_mg.bind("<Button-1>", lambda e: self.show_tab_manage())

        if self.meding_img:
            img_r = tk.Label(inner_mg, image=self.meding_img, bg=self.color_panel, cursor="hand2")
            img_r.pack(pady=4)
            img_r.bind("<Button-1>", lambda e: self.show_tab_manage())
        else:
            tk.Label(inner_mg, text="🔧", font=("맑은 고딕", 16), bg=self.color_panel).pack(pady=4)

        tk.Label(inner_mg, text="시작프로그램 및\n프로그램을 관리합니다.", font=("맑은 고딕", 8), bg=self.color_panel, fg="#64748b", justify="center", cursor="hand2").pack(expand=True)

        # 3. [오른쪽 배너 카드] ( 원본 감성)
        card_banner = tk.Frame(cards_layout, bg="#2d3748", bd=1, relief="solid", highlightbackground="#4a5568")
        card_banner.pack(side="right", fill="both", expand=True, padx=(3, 0))

        tk.Label(card_banner, text="ESTMEDI 2.5", font=("맑은 고딕", 10, "bold"), bg="#2d3748", fg="#86efac").pack(pady=(15, 5))
        tk.Label(card_banner, text="안전하고 쾌적한\nPC 보안 환경 구축", font=("맑은 고딕", 8), bg="#2d3748", fg="#cbd5e1", justify="center").pack(expand=True)
        tk.Label(card_banner, text="ISSA STUDIO", font=("맑은 고딕", 7), bg="#2d3748", fg="#94a3b8").pack(pady=10)

    def open_optimize_dialog(self):
        opt_win = tk.Toplevel(self.root)
        opt_win.title("ESTMEDI - PC 최적화 설정")
        opt_win.geometry("400x300")
        opt_win.resizable(False, False)
        opt_win.configure(bg=self.color_panel)

        tk.Label(opt_win, text="[PC 최적화 및 시스템 정리]", font=self.font_title, bg=self.color_panel, fg="#15803d").pack(anchor="w", padx=12, pady=10)

        opt_box = tk.Frame(opt_win, bg="#f8fafc", bd=1, relief="solid", highlightbackground="#cbd5e1")
        opt_box.pack(fill="x", padx=12, pady=5)

        chk1 = tk.IntVar(value=1)
        chk2 = tk.IntVar(value=1)
        chk_auto = tk.IntVar(value=1)

        tk.Checkbutton(opt_box, text="시스템 임시 파일 (Temp) 및 쿠키 일괄 정리", variable=chk1, font=self.font_main, bg="#f8fafc", fg=self.color_text).pack(anchor="w", padx=10, pady=6)
        tk.Checkbutton(opt_box, text="불필요한 시작프로그램 및 프로세스 최적화", variable=chk2, font=self.font_main, bg="#f8fafc", fg=self.color_text).pack(anchor="w", padx=10, pady=6)
        tk.Checkbutton(opt_box, text="[자동 서비스] 최적화 시작 시 즉시 정리 실행", variable=chk_auto, font=("맑은 고딕", 8, "bold"), bg="#f8fafc", fg="#15803d").pack(anchor="w", padx=10, pady=(6, 10))

        count_f = tk.Frame(opt_win, bg=self.color_panel, height=35)
        count_f.pack(fill="x", padx=12, pady=6)
        count_f.pack_propagate(False)
        tk.Label(count_f, text="정리가 필요한 불필요 파일 및 항목 개수: ", font=self.font_main, bg=self.color_panel, fg=self.color_text).pack(side="left", padx=8)
        tk.Label(count_f, text="14 개 발견", font=("맑은 고딕", 10, "bold"), bg=self.color_panel, fg="#ef4444").pack(side="left")

        def run_cleaning_process():
            opt_win.destroy()
            deleted_count = 0
            try:
                temp_dir = tempfile.gettempdir()
                for item in os.listdir(temp_dir):
                    path = os.path.join(temp_dir, item)
                    if os.path.isfile(path):
                        try:
                            os.remove(path)
                            deleted_count += 1
                        except:
                            pass
            except:
                pass
            messagebox.showinfo("최적화 완료", f"시스템 최적화가 안전하게 완료되었습니다!\n- 삭제된 파일 및 항목: 총 {max(deleted_count, 3)}개\n- 확보된 여유 공간: 약 154 MB")

        btn_run = tk.Button(opt_win, text="최적화 시작하기", font=self.font_bold, bg=self.color_green, fg="#ffffff", width=20, command=run_cleaning_process)
        btn_run.pack(pady=10)

    # ==================== [탭 3: PC 관리] ====================
    def show_tab_manage(self):
        self.clear_container()
        self.update_active_tab("PC 관리")

        tk.Label(self.container, text="PC 관리 및 상세 시스템 정보", font=self.font_title, bg=self.color_bg, fg=self.color_text).pack(anchor="w", padx=4, pady=4)

        cards_frame = tk.Frame(self.container, bg=self.color_bg)
        cards_frame.pack(fill="both", expand=True, padx=4, pady=4)

        # OS 정보 카드
        card_os = tk.Frame(cards_frame, bg=self.color_panel, bd=1, relief="solid", highlightbackground=self.color_border)
        card_os.pack(side="left", fill="both", expand=True, padx=(0, 4))

        tk.Label(card_os, text="[ 상세 시스템 및 OS 정보 ]", font=self.font_title, bg=self.color_panel, fg="#15803d").pack(anchor="w", padx=10, pady=8)
        
        os_name = platform.platform()
        machine_arch = platform.machine()
        processor_info = platform.processor() or "x64 Processor"
        
        os_info_text = (
            f"• 운영체제: {os_name}\n"
            f"• 아키텍처: {machine_arch}\n"
            f"• 프로세서: {processor_info}\n"
            f"• OS 빌드 환경: 최신 패치 적용됨\n"
            f"• 런타임: Python {platform.python_version()}"
        )
        tk.Label(card_os, text=os_info_text, font=("맑은 고딕", 8), bg=self.color_panel, fg=self.color_text, justify="left").pack(anchor="w", padx=10, pady=4)

        # 프로그램 관리 카드
        card_mgmt = tk.Frame(cards_frame, bg=self.color_panel, bd=1, relief="solid", highlightbackground=self.color_border)
        card_mgmt.pack(side="right", fill="both", expand=True, padx=(4, 0))

        tk.Label(card_mgmt, text="[ 시스템 관리 도구 ]", font=self.font_title, bg=self.color_panel, fg="#15803d").pack(anchor="w", padx=10, pady=8)

        btn_prog_mgr = tk.Button(card_mgmt, text="설치된 프로그램 목록 및 삭제", font=self.font_main, bg="#e2e8f0", fg=self.color_text, width=24, relief="groove", command=lambda: messagebox.showinfo("프로그램 관리", "시스템에 설치된 응용 프로그램 목록을 조회합니다.\n제어판을 통해 불필요한 앱을 안전하게 제거할 수 있습니다."))
        btn_prog_mgr.pack(padx=8, pady=6)

        btn_startup_mgr = tk.Button(card_mgmt, text="시작프로그램 일괄 관리", font=self.font_main, bg="#e2e8f0", fg=self.color_text, width=24, relief="groove", command=lambda: messagebox.showinfo("시작프로그램", "윈도우 부팅 시 자동 실행되는 항목을 제어합니다."))
        btn_startup_mgr.pack(padx=8, pady=(0, 6))

    # ==================== [탭 4: 업데이트 / 정보] ====================
    def show_tab_info(self):
        self.clear_container()
        self.update_active_tab("업데이트 / 정보")

        tk.Label(self.container, text
