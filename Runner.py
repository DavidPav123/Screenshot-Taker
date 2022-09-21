import tkinter as tk
from TakeScreenShot import take_screenshot

WIDTH: int = 1000
HEIGHT: int = 1000
X: int = 100
Y: int = 100

app = tk.Tk(className="Screenshot")


def make_client_rectangle():
    global window
    window = tk.Toplevel()
    window.resizable(False, False)
    window.attributes("-fullscreen", True)
    window.wm_attributes("-transparentcolor", window["bg"])
    window.attributes("-topmost", True)
    canvas = tk.Canvas(window, width=10000, height=10000)
    canvas.create_rectangle(
        X,
        Y,
        X + WIDTH,
        Y + HEIGHT,
        outline="green",
        width=5,
    )
    canvas.pack()
    window.mainloop()


def destroy_rectangle_window():
    window.destroy()


if __name__ == "__main__":
    buttonShowRectangle = tk.Button(
        text="Show Rectangle",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=make_client_rectangle,
    )
    buttonDestroyRectangle = tk.Button(
        text="Destroy Rectangle",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=destroy_rectangle_window,
    )
    buttonTakeScreenshot = tk.Button(
        text="Screeshot",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=lambda: take_screenshot(X, Y, WIDTH, HEIGHT),
    )

    buttonShowRectangle.pack()
    buttonDestroyRectangle.pack()
    buttonTakeScreenshot.pack()

    app.mainloop()
