import tkinter as tk
from counterclockwise import Points 
from counterclockwise import Lines 

class Drawing:
    def __init__(self, root):
        self.root = root
        self.root.title("Line Segments Intersection")
        
        # Canvas setup
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()

        # Labels and input entries for line coordinates
        self.label = tk.Label(self.root, text="Enter coordinates for line 1:")
        self.label.pack()

        self.entry_label_A = tk.Label(self.root, text="Point 1: (x1, y1): ")
        self.entry_label_A.pack()
        self.entry_A = tk.Entry(self.root)
        self.entry_A.pack()

        self.entry_label_B = tk.Label(self.root, text="Point 2: (x2, y2): ")
        self.entry_label_B.pack()
        self.entry_B = tk.Entry(self.root)
        self.entry_B.pack()

        self.label = tk.Label(self.root, text="Enter coordinates for line 2:")
        self.label.pack()

        self.entry_label_C = tk.Label(self.root, text="Point 3: (x1, y1): ")
        self.entry_label_C.pack()
        self.entry_C = tk.Entry(self.root)
        self.entry_C.pack()

        self.entry_label_D = tk.Label(self.root, text="Point 4: (x2, y2): ")
        self.entry_label_D.pack()
        self.entry_D = tk.Entry(self.root)
        self.entry_D.pack()

        self.l = Lines()

        # Button to check intersection
        self.check_button = tk.Button(self.root, text="Check Intersection", command=self.check_intersection)
        self.check_button.pack()

        # Canvas to display time and space complexity
        self.time_complexity_canvas = tk.Canvas(self.root, width=200, height=50, bg="white")
        self.time_complexity_canvas.pack()

    def close_window(self):
        """Close the window."""
        self.root.destroy()

    def check_intersection(self):
        """Check intersection of two line segments."""
        # Fetch input coordinates
        x1, y1 = map(int, self.entry_A.get().split(','))
        x2, y2 = map(int, self.entry_B.get().split(','))
        x3, y3 = map(int, self.entry_C.get().split(','))
        x4, y4 = map(int, self.entry_D.get().split(','))

        # Set points for line segments
        self.l.p1.set_point(x1, y1)
        self.l.p2.set_point(x2, y2)
        self.l.p3.set_point(x3, y3)
        self.l.p4.set_point(x4, y4)

        # Check for intersection
        intersection = self.l.check_points()

        # Display result label
        if intersection:
            result_text = "Line segments intersect!"
        else:
            result_text = "Line segments do not intersect."

        self.result_label = tk.Label(self.root, text=result_text)
        self.result_label.pack()

        # Draw line segments on canvas
        self.canvas.create_line(self.l.p1.x, self.l.p1.y, self.l.p2.x, self.l.p2.y, fill="white", width=2)
        self.canvas.create_line(self.l.p3.x, self.l.p3.y, self.l.p4.x, self.l.p4.y, fill="yellow", width=2)

        # Display time and space complexity
        time_complexity_text = "Time Complexity: O(1)\nSpace complexity: O(1)"
        self.time_complexity_canvas.create_text(100, 25, text=time_complexity_text, font=("Arial", 10))

        # Close window after 5 seconds
        self.root.after(5000, self.close_window)

# Create tkinter root window and run the application
root = tk.Tk()
app = Drawing(root)
root.mainloop()
