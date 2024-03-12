import tkinter as tk
from PIL import Image, ImageDraw

class SignatureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Signature App")

        self.canvas = tk.Canvas(self.master, width=400, height=200, bg="white")
        self.canvas.pack()

        self.signature_image = Image.new("RGB", (400, 200), "white")
        self.draw = ImageDraw.Draw(self.signature_image)

        self.prev_x = None
        self.prev_y = None

        self.canvas.bind("<B1-Motion>", self.draw_signature)
        self.canvas.bind("<ButtonRelease-1>", self.reset_prev_position)

        self.button_save = tk.Button(self.master, text="Save Signature", command=self.save_signature)
        self.button_save.pack()

        self.button_undo = tk.Button(self.master, text="Undo", command=self.undo)
        self.button_undo.pack()

    def draw_signature(self, event):
        x, y = event.x, event.y
        if self.prev_x is not None and self.prev_y is not None:
            self.canvas.create_line(self.prev_x, self.prev_y, x, y, fill="black", width=2)
            self.draw.line([self.prev_x, self.prev_y, x, y], fill="black", width=2)
        self.prev_x = x
        self.prev_y = y

    def reset_prev_position(self, event):
        self.prev_x = None
        self.prev_y = None

    def undo(self):
        self.canvas.delete("all")
        self.signature_image = Image.new("RGB", (400, 200), "white")
        self.draw = ImageDraw.Draw(self.signature_image)

    def save_signature(self):
        filename = "signature.png"
        self.signature_image.save(filename)
        print(f"Signature saved as {filename}")

def main():
    root = tk.Tk()
    app = SignatureApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
