from PIL import ImageGrab


def take_screenshot(X_Cord, Y_Cord, Width, Height):
    count_file = open("Screenshots/Count.txt", "r")
    read_line: str = count_file.readline(10)
    count_file.close()
    next_count: int = int(read_line) + 1

    snapshot = ImageGrab.grab(bbox=(X_Cord, Y_Cord, X_Cord + Width, Y_Cord + Height))

    save_path: str = f"Screenshots/Image{read_line}.jpg"
    snapshot.save(save_path)

    count_file = open("Screenshots/Count.txt", "w")
    count_file.write(str(next_count))
