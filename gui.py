import tkinter as tk
from tkinter import messagebox
from ai_engine import predict_disease
from knowledge_base import symptoms_list


class MedicalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Medical Expert System")
        self.root.geometry("980x650")
        self.root.configure(bg="#f3f6fb")

        self.result = None
        self.vars = {}

        # THEME COLORS (SINGLE CONSISTENT THEME)
        self.PRIMARY = "#1e3a8a"   # dark blue
        self.SECONDARY = "#2563eb" # blue
        self.BG = "#f3f6fb"        # light background
        self.CARD = "#ffffff"

        self.build_home()

    # ---------------- HOME PAGE ----------------
    def build_home(self):
        self.clear()

        header = tk.Frame(self.root, bg=self.PRIMARY, height=100)
        header.pack(fill="x")

        tk.Label(
            header,
            text="AI MEDICAL EXPERT SYSTEM",
            font=("Helvetica", 24, "bold"),
            fg="white",
            bg=self.PRIMARY
        ).pack(pady=25)

        body = tk.Frame(self.root, bg=self.BG)
        body.pack(expand=True)

        card = tk.Frame(body, bg=self.CARD, bd=1, relief="solid")
        card.pack(pady=80, ipadx=60, ipady=50)

        tk.Label(
            card,
            text="Smart AI Symptom Checker",
            font=("Helvetica", 16, "bold"),
            bg=self.CARD,
            fg=self.PRIMARY
        ).pack(pady=10)

        tk.Label(
            card,
            text="Select symptoms and get instant medical analysis",
            font=("Helvetica", 12),
            bg=self.CARD,
            fg="#555"
        ).pack(pady=10)

        tk.Button(
            card,
            text="START DIAGNOSIS",
            font=("Helvetica", 14, "bold"),
            bg=self.SECONDARY,
            fg="white",
            padx=25,
            pady=10,
            command=self.symptom_page
        ).pack(pady=20)

    # ---------------- SYMPTOM PAGE ----------------
    def symptom_page(self):
        self.clear()

        header = tk.Frame(self.root, bg=self.PRIMARY, height=80)
        header.pack(fill="x")

        tk.Label(
            header,
            text="SELECT SYMPTOMS",
            font=("Helvetica", 20, "bold"),
            fg="white",
            bg=self.PRIMARY
        ).pack(pady=20)

        container = tk.Frame(self.root, bg=self.BG)
        container.pack(expand=True)

        card = tk.Frame(container, bg=self.CARD, bd=1, relief="solid")
        card.pack(pady=20, ipadx=40, ipady=20)

        self.vars = {}

        tk.Label(
            card,
            text="Choose all applicable symptoms:",
            font=("Helvetica", 13, "bold"),
            bg=self.CARD,
            fg=self.PRIMARY
        ).pack(pady=10)

        for s in symptoms_list:
            var = tk.IntVar()

            tk.Checkbutton(
                card,
                text=s,
                variable=var,
                font=("Helvetica", 12),
                bg=self.CARD,
                fg="#333",
                anchor="w"
            ).pack(anchor="w", padx=20, pady=4)

            self.vars[s] = var

        tk.Button(
            container,
            text="RUN AI DIAGNOSIS",
            font=("Helvetica", 13, "bold"),
            bg=self.SECONDARY,
            fg="white",
            padx=20,
            pady=8,
            command=self.result_page
        ).pack(pady=15)

        tk.Button(
            container,
            text="BACK",
            font=("Helvetica", 11),
            command=self.build_home
        ).pack()

    # ---------------- RESULT PAGE ----------------
    def result_page(self):
        selected = [s for s, v in self.vars.items() if v.get() == 1]

        if not selected:
            messagebox.showwarning("Warning", "Please select symptoms first!")
            return

        self.result = predict_disease(selected)

        self.clear()

        header = tk.Frame(self.root, bg=self.SECONDARY, height=80)
        header.pack(fill="x")

        tk.Label(
            header,
            text="DIAGNOSIS RESULT",
            font=("Helvetica", 20, "bold"),
            fg="white",
            bg=self.SECONDARY
        ).pack(pady=20)

        body = tk.Frame(self.root, bg=self.BG)
        body.pack(expand=True)

        card = tk.Frame(body, bg=self.CARD, bd=1, relief="solid")
        card.pack(pady=30, ipadx=40, ipady=25)

        top = self.result[0]["disease"]

        tk.Label(
            card,
            text=f"Most Likely Condition: {top}",
            font=("Helvetica", 16, "bold"),
            bg=self.CARD,
            fg=self.PRIMARY
        ).pack(pady=10)

        for r in self.result[:3]:
            tk.Label(
                card,
                text=f"{r['disease']} → {r['score']}%",
                font=("Helvetica", 12),
                bg=self.CARD
            ).pack(pady=2)

        tk.Button(
            body,
            text="VIEW TREATMENT PLAN",
            font=("Helvetica", 13, "bold"),
            bg=self.SECONDARY,
            fg="white",
            padx=20,
            pady=8,
            command=self.treatment_page
        ).pack(pady=10)

    # ---------------- TREATMENT PAGE ----------------
    def treatment_page(self):
        self.clear()

        data = next(r for r in self.result if r["disease"] == self.result[0]["disease"])

        header = tk.Frame(self.root, bg=self.PRIMARY, height=80)
        header.pack(fill="x")

        tk.Label(
            header,
            text="TREATMENT PLAN",
            font=("Helvetica", 20, "bold"),
            fg="white",
            bg=self.PRIMARY
        ).pack(pady=20)

        body = tk.Frame(self.root, bg=self.BG)
        body.pack(expand=True)

        card = tk.Frame(body, bg=self.CARD, bd=1, relief="solid")
        card.pack(pady=25, ipadx=50, ipady=30)

        tk.Label(
            card,
            text=f"Disease: {self.result[0]['disease']}",
            font=("Helvetica", 16, "bold"),
            bg=self.CARD,
            fg=self.PRIMARY
        ).pack(pady=10)

        tk.Label(
            card,
            text=data["advice"],
            font=("Helvetica", 12),
            bg=self.CARD,
            wraplength=700
        ).pack(pady=10)

        tk.Label(
            card,
            text=data["treatment"],
            font=("Helvetica", 12),
            bg=self.CARD,
            fg="#333",
            wraplength=700
        ).pack(pady=10)

        tk.Button(
            body,
            text="GO TO HOME",
            font=("Helvetica", 13, "bold"),
            bg=self.SECONDARY,
            fg="white",
            padx=20,
            pady=8,
            command=self.build_home
        ).pack(pady=15)

    # ---------------- CLEAR ----------------
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()