import tkinter as tk
import random

# Constants
WIDTH = 600
HEIGHT = 400
SEG_SIZE = 20
IN_GAME = True

# Create the canvas
canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

# Snake class
class Snake:
    def __init__(self):
        self.segments = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food_position = self.set_food_position()
        self.score = 0
        self.speed = 100
        self.draw()

    def draw(self):
        canvas.delete("snake", "food", "score")
        for segment in self.segments:
            canvas.create_rectangle(segment[0], segment[1], segment[0] + SEG_SIZE, segment[1] + SEG_SIZE, fill='green', tags="snake")
        canvas.create_oval(self.food_position[0], self.food_position[1], self.food_position[0] + SEG_SIZE, self.food_position[1] + SEG_SIZE, fill='red', tags="food")
        canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white", tags="score")

    def move(self):
        head_x, head_y = self.segments[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - SEG_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + SEG_SIZE)
        elif self.direction == "Left":
            new_head = (head_x - SEG_SIZE, head_y)
        elif self.direction == "Right":
            new_head = (head_x + SEG_SIZE, head_y)

        self.segments = [new_head] + self.segments[:-1]

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            new_direction = event.keysym
            opposite_direction = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if new_direction != opposite_direction[self.direction]:
                self.direction = new_direction

    def check_collisions(self):
        head_x, head_y = self.segments[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True
        elif (head_x, head_y) in self.segments[1:]:
            return True
        elif (head_x, head_y) == self.food_position:
            self.segments.append(self.segments[-1])
            self.score += 1
            self.speed -= 1
            self.food_position = self.set_food_position()
        return False

    def set_food_position(self):
        x = random.randint(0, (WIDTH - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        y = random.randint(0, (HEIGHT - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        return x, y

# Main loop
def game_loop():
    global IN_GAME
    if IN_GAME:
        snake.move()
        if snake.check_collisions():
            IN_GAME = False
        snake.draw()
        root.after(snake.speed, game_loop)
    else:
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"Game Over! Score: {snake.score}", fill="white", font=("Helvetica", 20))

# Create the snake object
snake = Snake()

# Bind arrow keys for controlling the snake
root = tk.Tk()
root.title("Snake Game")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.bind("<Key>", snake.change_direction)

# Start the game loop
game_loop()

# Run the Tkinter event loop
root.mainloop()
