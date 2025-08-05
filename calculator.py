"""
Модуль калькулятора ИМТ
Содержит основной функционал приложения
"""

import tkinter as tk
from tkinter import messagebox


class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор ИМТ")

        # Создание виджетов
        self.label_height = tk.Label(root, text="Рост (см):")
        self.label_weight = tk.Label(root, text="Вес (кг):")
        self.entry_height = tk.Entry(root)
        self.entry_weight = tk.Entry(root)
        self.button_calculate = tk.Button(root, text="Рассчитать", command=self.calculate)
        self.button_clear = tk.Button(root, text="Очистить", command=self.clear_fields)
        self.label_result = tk.Label(root, text="Результат:")
        self.label_interpretation = tk.Label(root, text="")

        # Размещение виджетов
        self.label_height.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_height.grid(row=0, column=1, padx=5, pady=5)
        self.label_weight.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_weight.grid(row=1, column=1, padx=5, pady=5)
        self.button_calculate.grid(row=2, column=0, padx=5, pady=10, sticky="w")
        self.button_clear.grid(row=2, column=1, padx=5, pady=10, sticky="e")
        self.label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.label_interpretation.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def calculate(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())

            if height <= 0 or weight <= 0:
                raise ValueError

            height_m = height / 100
            bmi = weight / (height_m ** 2)

            self.label_result.config(text=f"ИМТ: {bmi:.2f}")
            self.label_interpretation.config(text=self.get_interpretation(bmi))

        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числовые значения")

    def clear_fields(self):
        self.entry_height.delete(0, tk.END)
        self.entry_weight.delete(0, tk.END)
        self.label_result.config(text="Результат:")
        self.label_interpretation.config(text="")

    def get_interpretation(self, bmi):
        if bmi <= 16:
            return "Выраженный дефицит массы тела"
        elif 16 < bmi <= 18.5:
            return "Недостаточная масса тела"
        elif 18.5 < bmi <= 25:
            return "Нормальная масса тела"
        elif 25 < bmi <= 30:
            return "Избыточная масса тела (предожирение)"
        elif 30 < bmi <= 35:
            return "Ожирение первой степени"
        elif 35 < bmi <= 40:
            return "Ожирение второй степени"
        else:
            return "Ожирение третьей степени (морбидное)"
