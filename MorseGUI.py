import tkinter as tk
from tkinter import messagebox
import pyaudio
import wave

from MorseTranslator import MorseTranslator

class MorseTransGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Translator")

        self.setup_gui()


    def setup_gui(self):
        self.text_label = tk.Label(self.root, text="Text:")
        self.text_label.grid(row=0, column=0, padx=10, pady=5)

        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.grid(row=0, column=1, padx=10, pady=5)

        self.morse_label = tk.Label(self.root, text="Morse Code:")
        self.morse_label.grid(row=1, column=0, padx=10, pady=5)

        self.morse_entry = tk.Entry(self.root, width=50)
        self.morse_entry.grid(row=1, column=1, padx=10, pady=5)

        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def translate_text(self):
        text = self.text_entry.get()
        morse = self.morse_entry.get()

        translator = MorseTranslator()

        if text:
            morse_translation = translator.text_to_morse(text)
            self.morse_entry.delete(0, tk.END)
            self.morse_entry.insert(tk.END, morse_translation)
        elif morse:
            text_translation = translator.morse_to_text(morse)
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(tk.END, text_translation)
        else:
            messagebox.showinfo("Error", "Please enter either text or Morse code!")

    def listen_morse_audio(audio_filename):
        # Load Morse audio
        wf = wave.open(audio_filename, 'rb')

        # Initialize PyAudio
        p = pyaudio.PyAudio()

        # Open stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        print("Listening to Morse audio...")

        # Read data and play audio
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # Stop stream and close PyAudio
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseTransGUI(root)
    root.mainloop()

