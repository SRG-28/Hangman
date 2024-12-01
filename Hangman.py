import tkinter as tk
import random

palabras = ["roger","esteban","diego","ronald","sofia" ]

HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

class Ahorcado:

   def __init__(self,root):
      self.root = root
      self.root.title("Ahorcado")

      self.palabra = random.choice(palabras)
      self.letras_adivinadas = set()
      self.intentos = 6

      self.crear_widgets()

   def crear_widgets(self):
      self.hangman_label = tk.Label(self.root, text=HANGMAN_PICS[6], font=("Courier", 12))
      self.hangman_label.pack()

      self.word_label = tk.Label(self.root, text=self.mostrar_palabra(), font=("Courier", 12))
      self.word_label.pack()

      self.attempts_label = tk.Label(self.root, text=f"Intentos faltantes: {self.intentos}", font=("Courier", 12))
      self.attempts_label.pack()

      self.guess_entry = tk.Entry(self.root)
      self.guess_entry.pack()

      self.guess_button = tk.Button(self.root, text="Adivinar", command=self.hacer_adivinar)
      self.guess_button.pack()

      self.result_label = tk.Label(self.root, text="", font=("Courier", 12))
      self.result_label.pack()

   def mostrar_palabra(self):
      return ' '.join([letra if letra in self.letras_adivinadas else '_' for letra in self.palabra])

   def hacer_adivinar(self):
      adivinar = self.guess_entry.get().lower()
      self.guess_entry.delete(0, tk.END)
      if len(adivinar) != 1 or not adivinar.isalpha():
         self.result_label.config(text="Por favor usa una letra.")
         return

      if adivinar in self.letras_adivinadas:
          self.result_label.config(text="Ya usaste esa letra.")
      elif adivinar in self.palabra:
          self.letras_adivinadas.add(adivinar)
          self.result_label.config(text="Adivinaste la letra.")
      else:
          self.intentos -= 1
          self.letras_adivinadas.add(adivinar)
          self.result_label.config(text="No es esa letra.")

      self.hangman_label.config(text=HANGMAN_PICS[6 - self.intentos])
      self.word_label.config(text=self.mostrar_palabra())
      self.attempts_label.config(text=f"Intentos restantes: {self.intentos}")

      if all(letra in self.letras_adivinadas for letra in self.palabra):
         self.guess_button.config(state=tk.DISABLED)
      elif self.intentos == 0:
         self.hangman_label.config(text=HANGMAN_PICS[6])
         self.result_label.config(text=f"Perdiste, la palabra era: {self.palabra}")
         self.guess_button.config(state=tk.DISABLED)  

root = tk.Tk()
juego = Ahorcado(root)
root.mainloop()
