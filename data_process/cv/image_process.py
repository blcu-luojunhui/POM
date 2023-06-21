import cv2


class ImageProcess:
    def __init__(self, path):
        self.path = path
        if path.endswith(".json"):
            self.json_to_img()
        else:
            self.draw_img()

    def json_to_img(self):
        print(self.path)
        return

    def draw_img(self):
        print(self.path)
        return
