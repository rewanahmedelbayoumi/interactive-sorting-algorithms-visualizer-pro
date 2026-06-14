# ================= ui.py =================

import customtkinter as ctk
from tkinter import Canvas
from visualizer import Visualizer
from algorithms import *
from utils import generate_array
from extras import export_report
import time
import winsound

# ================= THEME =================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ================= APP =================

class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        # ================= WINDOW =================

        self.title("Sorting Visualizer PRO")

        self.geometry("1500x900")

        self.configure(
            fg_color="#07070a"
        )

        # ================= DATA =================

        self.array = generate_array(40)

        self.history = []

        self.steps_history1 = []

        self.steps_history2 = []

        # ================= LEFT PANEL =================

        self.controls = ctk.CTkFrame(
            self,
            width=330,
            corner_radius=25,
            fg_color="#111827",
            border_width=1,
            border_color="#7c3aed"
        )

        self.controls.pack(
            side="left",
            fill="y",
            padx=15,
            pady=15
        )

        # ================= TITLE =================

        title = ctk.CTkLabel(
            self.controls,
            text="Sorting Visualizer",
            font=("Poppins", 30, "bold"),
            text_color="#e9d5ff"
        )

        title.pack(
            pady=(25, 20)
        )

        # ================= MODE SWITCH =================

        mode_frame = ctk.CTkFrame(
            self.controls,
            fg_color="transparent"
        )

        mode_frame.pack(pady=10)

        dark_label = ctk.CTkLabel(
            mode_frame,
            text="Dark",
            text_color="#c4b5fd",
            font=("Poppins", 13, "bold")
        )

        dark_label.pack(side="left", padx=5)

        self.mode_switch = ctk.CTkSwitch(
            mode_frame,
            text="",
            command=self.toggle_mode,
            progress_color="#7c3aed",
            button_color="#ffffff"
        )

        self.mode_switch.pack(side="left", padx=5)

        light_label = ctk.CTkLabel(
            mode_frame,
            text="Light",
            text_color="#c4b5fd",
            font=("Poppins", 13, "bold")
        )

        light_label.pack(side="left", padx=5)

        # ================= ARRAY INPUT =================

        ctk.CTkLabel(
            self.controls,
            text="Enter Array",
            font=("Poppins", 14, "bold"),
            text_color="#e9d5ff"
        ).pack(pady=(20, 5))

        self.array_entry = ctk.CTkEntry(
            self.controls,
            placeholder_text="Example: 5,2,9,1",
            height=42,
            corner_radius=12,
            fg_color="#1e293b",
            border_color="#7c3aed",
            text_color="white"
        )

        self.array_entry.pack(
            padx=12,
            fill="x"
        )

        # ================= ALGORITHM 1 =================

        ctk.CTkLabel(
            self.controls,
            text="Algorithm 1",
            font=("Poppins", 14, "bold"),
            text_color="#e9d5ff"
        ).pack(pady=(20, 5))

        self.algo1 = ctk.CTkOptionMenu(

            self.controls,

            values=[
                "Bubble",
                "Quick",
                "Selection",
                "Insertion",
                "Merge"
            ],

            command=self.show_preview,

            fg_color="#7c3aed",

            button_color="#6d28d9",

            button_hover_color="#5b21b6",

            dropdown_fg_color="#111827",

            dropdown_hover_color="#7c3aed",

            corner_radius=12,

            height=42,

            font=("Poppins", 13, "bold")
        )

        self.algo1.pack(
            padx=12,
            fill="x"
        )

        # ================= ALGORITHM 2 =================

        ctk.CTkLabel(
            self.controls,
            text="Algorithm 2",
            font=("Poppins", 14, "bold"),
            text_color="#e9d5ff"
        ).pack(pady=(20, 5))

        self.algo2 = ctk.CTkOptionMenu(

            self.controls,

            values=[
                "Bubble",
                "Quick",
                "Selection",
                "Insertion",
                "Merge"
            ],

            fg_color="#7c3aed",

            button_color="#6d28d9",

            button_hover_color="#5b21b6",

            dropdown_fg_color="#111827",

            dropdown_hover_color="#7c3aed",

            corner_radius=12,

            height=42,

            font=("Poppins", 13, "bold")
        )

        self.algo2.pack(
            padx=12,
            fill="x"
        )

        # ================= COMPLEXITY =================

        self.complexity_label = ctk.CTkLabel(
            self.controls,
            text="Complexity: O(n²)",
            font=("Poppins", 13, "bold"),
            text_color="#c4b5fd"
        )

        self.complexity_label.pack(pady=15)

        # ================= BUTTONS =================

        self.create_button(
            "Start Sorting",
            self.start_sort
        )

        self.create_button(
            "Replay",
            self.replay
        )

        self.create_button(
            "Reset",
            self.reset_array
        )

        self.create_button(
            "Export PDF",
            self.export
        )

        # ================= SPEED =================

        ctk.CTkLabel(
            self.controls,
            text="Animation Speed",
            font=("Poppins", 14, "bold"),
            text_color="#e9d5ff"
        ).pack(pady=(20, 5))

        self.speed = ctk.CTkSlider(
            self.controls,
            from_=1,
            to=200,
            progress_color="#7c3aed",
            button_color="#a855f7"
        )

        self.speed.set(80)

        self.speed.pack(
            padx=12,
            fill="x"
        )

        # ================= STATS =================

        self.stats = ctk.CTkLabel(
            self.controls,
            text="",
            justify="left",
            font=("Consolas", 13),
            text_color="#e9d5ff"
        )

        self.stats.pack(pady=15)

        # ================= PREVIEW =================

        self.preview = Canvas(
            self.controls,
            width=250,
            height=160,
            bg="#020617",
            highlightthickness=0
        )

        self.preview.pack(pady=10)

        # ================= RIGHT SIDE =================

        self.canvas_frame = ctk.CTkFrame(
            self,
            corner_radius=25,
            fg_color="#0f172a",
            border_width=1,
            border_color="#7c3aed"
        )

        self.canvas_frame.pack(
            side="right",
            expand=True,
            fill="both",
            padx=15,
            pady=15
        )

        container = ctk.CTkFrame(
            self.canvas_frame,
            fg_color="transparent"
        )

        container.pack(expand=True)

        # ================= LEFT CANVAS =================

        left = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        left.pack(side="left", padx=20)

        self.canvas1 = Canvas(
            left,
            width=520,
            height=520,
            bg="#020617",
            highlightthickness=0
        )

        self.canvas1.pack()

        self.show_steps_btn1 = ctk.CTkButton(
            left,
            text="Show Steps",
            command=self.toggle_steps1,
            fg_color="#7c3aed",
            hover_color="#5b21b6",
            corner_radius=12
        )

        self.show_steps_btn1.pack(pady=10)

        # ================= RIGHT CANVAS =================

        right = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        right.pack(side="right", padx=20)

        self.canvas2 = Canvas(
            right,
            width=520,
            height=520,
            bg="#020617",
            highlightthickness=0
        )

        self.canvas2.pack()

        self.show_steps_btn2 = ctk.CTkButton(
            right,
            text="Show Steps",
            command=self.toggle_steps2,
            fg_color="#7c3aed",
            hover_color="#5b21b6",
            corner_radius=12
        )

        self.show_steps_btn2.pack(pady=10)

        # ================= VISUALIZER =================

        self.vis1 = Visualizer(self.canvas1)

        self.vis2 = Visualizer(self.canvas2)

        self.draw()

    # =====================================================

    def create_button(self, text, command):

        btn = ctk.CTkButton(

            self.controls,

            text=text,

            command=command,

            fg_color="#7c3aed",

            hover_color="#5b21b6",

            text_color="white",

            corner_radius=15,

            height=45,

            font=("Poppins", 14, "bold"),

            border_width=1,

            border_color="#a855f7"
        )

        btn.pack(
            padx=12,
            pady=7,
            fill="x"
        )

    # =====================================================

    def toggle_mode(self):

        if self.mode_switch.get() == 1:

            ctk.set_appearance_mode("light")

            self.configure(fg_color="#f3f4f6")

        else:

            ctk.set_appearance_mode("dark")

            self.configure(fg_color="#07070a")

    # =====================================================

    def draw(self):

        self.vis1.draw(self.array)

        self.vis2.draw(self.array)

    # =====================================================

    def reset_array(self):

        self.array = generate_array(40)

        self.draw()

    # =====================================================

    def play_sound(self, action):

        try:

            if action == "compare":

                winsound.Beep(500, 40)

            elif action == "swap":

                winsound.Beep(900, 60)

        except:
            pass

    # =====================================================

    def start_sort(self):

        text = self.array_entry.get()

        if text:

            try:

                self.array = list(
                    map(int, text.split(","))
                )

            except:
                return

        algo_map = {

            "Bubble": bubble_sort,

            "Quick": quick_sort,

            "Selection": selection_sort,

            "Insertion": insertion_sort,

            "Merge": merge_sort
        }

        self.gen1 = algo_map[
            self.algo1.get()
        ](self.array.copy())

        self.gen2 = algo_map[
            self.algo2.get()
        ](self.array.copy())

        self.start_time = time.time()

        self.animate()

    # =====================================================

    def animate(self):

        try:

            a1 = next(self.gen1)

            a2 = next(self.gen2)

            self.vis1.draw(
                a1[0],
                [a1[1], a1[2]],
                a1[3]
            )

            self.vis2.draw(
                a2[0],
                [a2[1], a2[2]],
                a2[3]
            )

            self.play_sound(a1[3])

            elapsed = round(
                time.time() - self.start_time,
                2
            )

            self.stats.configure(
                text=f"""
{self.algo1.get()}
Comparisons: {a1[4]}
Swaps: {a1[5]}

{self.algo2.get()}
Comparisons: {a2[4]}
Swaps: {a2[5]}

Time: {elapsed}s
"""
            )

            self.steps_history1.append(
                f"{a1[3]} -> {a1[0]}\n"
            )

            self.steps_history2.append(
                f"{a2[3]} -> {a2[0]}\n"
            )

            delay = max(
                5,
                int(200 - self.speed.get())
            )

            self.after(delay, self.animate)

        except:
            pass

    # =====================================================

    def replay(self):

        pass

    # =====================================================

    def export(self):

        export_report(100, 50, 2)

    # =====================================================

    def toggle_steps1(self):

        window = ctk.CTkToplevel(self)

        window.title("Algorithm 1 Steps")

        window.geometry("700x600")

        textbox = ctk.CTkTextbox(
            window,
            font=("Consolas", 13)
        )

        textbox.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=10
        )

        textbox.insert(
            "0.0",
            "".join(self.steps_history1)
        )

    # =====================================================

    def toggle_steps2(self):

        window = ctk.CTkToplevel(self)

        window.title("Algorithm 2 Steps")

        window.geometry("700x600")

        textbox = ctk.CTkTextbox(
            window,
            font=("Consolas", 13)
        )

        textbox.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=10
        )

        textbox.insert(
            "0.0",
            "".join(self.steps_history2)
        )

    # =====================================================

    def show_preview(self, choice):

        complexity = {

            "Bubble": "O(n²)",

            "Quick": "O(n log n)",

            "Selection": "O(n²)",

            "Insertion": "O(n²)",

            "Merge": "O(n log n)"
        }

        self.complexity_label.configure(
            text=f"Complexity: {complexity[choice]}"
        )