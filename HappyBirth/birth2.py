import tkinter as tk
import random


class BirthdayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Причины любви")

        # Начальная надпись
        self.current_text = tk.StringVar()
        self.current_text.set("11 друзей Оушэна")
        self.label = tk.Label(root, textvariable=self.current_text, font=("Helvetica", 25))
        self.label.pack(pady=50)

        # Кнопка для переключения надписей
        self.button = tk.Button(root, background="lightgreen", width=70, height=5, bd=5,
                                fg="black", text="Узнать друга",
                                command=self.change_text)
        self.button.pack()

    def change_text(self):
        # Список различных надписей
        phrases = ["Самая красивая!", "Умная!", "Смешная!", "Помогаешь мне во всём!", "Вкусно готовишь",
                   "Всё умеешь", "Твой голос завораживает", "Моя жизнь прекрасна с тобой",
                   "Когда держу твою руку, становлюсь сильнее", "Потому что нам не скучно вместе",
                   "С утра радостно видеть твоё лицо"]

        # Выбираем случайную надпись
        random_phrase = random.choice(phrases)

        # Обновляем текст на экране
        self.current_text.set(random_phrase)


if __name__ == "__main__":
    root = tk.Tk()
    app = BirthdayApp(root)
    root.mainloop()
