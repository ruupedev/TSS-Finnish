import tkinter as tk
from gtts import gTTS
import os
import tempfile


class MinimalTextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minimal Text-to-Speech")
        
        # Text input
        self.text_input = tk.Text(root, wrap=tk.WORD, height=5)
        self.text_input.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Render button
        self.render_button = tk.Button(root, text="Render & Play", command=self.render_audio)
        self.render_button.pack(pady=5)
        
        # Status label
        self.status_label = tk.Label(root, text="Status: Idle", fg="blue")
        self.status_label.pack()

    def render_audio(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            try:
                # Generate the MP3 file
                tts = gTTS(text=text, lang='fi')
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                    audio_file = temp_file.name
                    tts.save(audio_file)
                    print(f"Audio saved to: {audio_file}")
                
                # Play the MP3 file using the default system player
                os.system(f'"{audio_file}"')
                self.status_label.config(text="Status: Playing Audio", fg="green")
            except Exception as e:
                self.status_label.config(text=f"Error: {e}", fg="red")
        else:
            self.status_label.config(text="Error: No text entered", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = MinimalTextToSpeechApp(root)
    root.mainloop()
