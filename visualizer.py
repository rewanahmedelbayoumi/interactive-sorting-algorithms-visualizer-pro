class Visualizer:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, arr, active_indices=[], action=""):

        self.canvas.delete("all")

        width = 500
        height = 500

        bar_width = width / len(arr)

        for i, val in enumerate(arr):

            x0 = i * bar_width
            y0 = height - (val * 4)

            x1 = (i + 1) * bar_width
            y1 = height

            color = "#a855f7"

            if i in active_indices:

                if action == "compare":
                    color = "#facc15"

                elif action == "swap":
                    color = "#ec4899"

            self.canvas.create_rectangle(
                x0,
                y0,
                x1,
                y1,
                fill=color,
                outline=""
            )

        self.canvas.update()