import tkinter as tk
from tkinter import font
import time
import math

N = 6

maze = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

cell_size = 80
border_radius = 12

root = tk.Tk()
root.title("🐭 Rat in a Maze Adventure 🧀")
root.geometry("600x700")
root.configure(bg="#1a1a2e")

canvas_bg = tk.Canvas(root, width=N*cell_size+40, height=N*cell_size+40, bg="#16213e", highlightthickness=0)
canvas_bg.pack(pady=20)

canvas = tk.Canvas(canvas_bg, width=N*cell_size+20, height=N*cell_size+20, 
                   bg="#0f3460", highlightthickness=0)
canvas.pack(pady=10)

title_font = font.Font(family="Segoe UI", size=20, weight="bold")
btn_font = font.Font(family="Segoe UI", size=14, weight="bold")

header_frame = tk.Frame(root, bg="#1a1a2e")
header_frame.pack(pady=(0,10))

title_label = tk.Label(header_frame, text="🐭 Maze Runner 🧀", 
                      font=title_font, fg="#e94560", bg="#1a1a2e")
title_label.pack()

status_label = tk.Label(header_frame, text="Click START to guide the rat! 🐁", 
                       font=("Segoe UI", 12), fg="#00d4aa", bg="#1a1a2e")
status_label.pack()

rects = [[None]*N for _ in range(N)]
current_rat_pos = None

def draw_rounded_rect(x1, y1, x2, y2, radius, fill_color, outline_color="#ffffff", width=2):
    try:
        canvas.create_oval(x1, y1, x1+2*radius, y1+2*radius, fill=fill_color, outline=outline_color, width=width)
        canvas.create_oval(x2-2*radius, y1, x2, y1+2*radius, fill=fill_color, outline=outline_color, width=width)
        canvas.create_oval(x1, y2-2*radius, x1+2*radius, y2, fill=fill_color, outline=outline_color, width=width)
        canvas.create_oval(x2-2*radius, y2-2*radius, x2, y2, fill=fill_color, outline=outline_color, width=width)
        
        canvas.create_rectangle(x1+radius, y1, x2-radius, y1+2*radius, fill=fill_color, outline=outline_color, width=width)
        canvas.create_rectangle(x1+radius, y1+radius, x2-radius, y2-radius, fill=fill_color, outline=outline_color, width=width)
        canvas.create_rectangle(x1, y1+radius, x1+2*radius, y2-radius, fill=fill_color, outline=outline_color, width=width)
        canvas.create_rectangle(x2-2*radius, y1+radius, x2, y2-radius, fill=fill_color, outline=outline_color, width=width)
    except:
        pass

def draw_grid():
    global rects, current_rat_pos
    
    canvas.delete("all")
    
    for i in range(N):
        for j in range(N):
            x1 = j * cell_size + 10
            y1 = i * cell_size + 10
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            rects[i][j] = (x1, y1, x2, y2)
    
    for i in range(N):
        for j in range(N):
            x1, y1, x2, y2 = rects[i][j]
            shadow_x1 = x1 + 2
            shadow_y1 = y1 + 2
            if maze[i][j] == 0:
                draw_rounded_rect(shadow_x1, shadow_y1, x2, y2, border_radius, "#2d1b69")
    
    for i in range(N):
        for j in range(N):
            x1, y1, x2, y2 = rects[i][j]

            if maze[i][j] == 0:
                draw_rounded_rect(x1, y1, x2, y2, border_radius, "#533483", "#7b2cbf", 4)
                canvas.create_oval(x1+5, y1+5, x1+15, y1+15, fill="#a8b4ff", outline="")
            else:
                draw_rounded_rect(x1, y1, x2, y2, border_radius, "#00d4aa", "#00f5d4", 3)
                canvas.create_oval(x1+cell_size//2-3, y1+cell_size//2-3, 
                                 x1+cell_size//2+3, y1+cell_size//2+3, fill="#ffffff", outline="")
    
    draw_cheese(N-1, N-1)
    
    current_rat_pos = (0, 0)
    draw_rat(0, 0)

def draw_rat(i, j):
    global current_rat_pos
    
    if i >= N or j >= N or i < 0 or j < 0:
        return
        
    try:
        x1, y1, x2, y2 = rects[i][j]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        
        canvas.delete("rat")
        
        canvas.create_oval(cx-18, cy-12, cx+18, cy+12, fill="#ff9f43", outline="#ff8c00", width=3, tags="rat")
        
        canvas.create_oval(cx-12, cy-20, cx+12, cy-2, fill="#ffcc99", outline="#ff8c00", width=3, tags="rat")
        
        canvas.create_oval(cx-14, cy-25, cx-8, cy-18, fill="#ff9f43", outline="#ff8c00", tags="rat")
        canvas.create_oval(cx+6, cy-25, cx+12, cy-18, fill="#ff9f43", outline="#ff8c00", tags="rat")
        
        canvas.create_oval(cx-6, cy-12, cx-2, cy-8, fill="white", outline="black", width=1, tags="rat")
        canvas.create_oval(cx+2, cy-12, cx+6, cy-8, fill="white", outline="black", width=1, tags="rat")
        canvas.create_oval(cx-5, cy-11, cx-3, cy-9, fill="black", tags="rat")
        canvas.create_oval(cx+3, cy-11, cx+5, cy-9, fill="black", tags="rat")
        
        canvas.create_polygon(cx-1, cy-6, cx+1, cy-6, cx, cy-4, fill="#ff69b4", outline="", tags="rat")
        
        for k in range(8):
            x_tail = cx+20 + k*3
            y_tail = cy + math.sin(k*0.5)*3
            canvas.create_oval(x_tail, y_tail-2, x_tail+6, y_tail+2, fill="#ffcc99", outline="#ff8c00", tags="rat")
        
        current_rat_pos = (i, j)
    except:
        pass

def draw_cheese(i, j):
    try:
        x1, y1, x2, y2 = rects[i][j]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        
        canvas.create_polygon(cx-20, cy-10, cx+20, cy-10, cx+15, cy+15, 
                             cx-15, cy+15, fill="#ffd700", outline="#ffed4e", width=4, tags="cheese")
        
        canvas.create_oval(cx-12, cy, cx-6, cy+6, fill="#ffed4e", outline="", tags="cheese")
        canvas.create_oval(cx+5, cy-3, cx+11, cy+3, fill="#ffed4e", outline="", tags="cheese")
        canvas.create_oval(cx-8, cy+8, cx-2, cy+14, fill="#ffed4e", outline="", tags="cheese")
        
        canvas.create_oval(cx-15, cy-15, cx-10, cy-10, fill="white", outline="", tags="cheese")
    except:
        pass

def color_cell(i, j, cell_type):
    try:
        x1, y1, x2, y2 = rects[i][j]
        
        if cell_type == "path":
            draw_rounded_rect(x1, y1, x2, y2, border_radius, "#11998e", "#38ef7d", 4)
            canvas.create_oval(x1+cell_size//2-5, y1+cell_size//2-5, 
                              x1+cell_size//2+5, y1+cell_size//2+5, fill="#ffffff", outline="")
        elif cell_type == "deadend":
            draw_rounded_rect(x1, y1, x2, y2, border_radius, "#cb2d3e", "#ef476f", 4)
        elif cell_type == "success":
            glow_colors = ["#00ff88", "#00ff99", "#00ffaa", "#00ffbb", "#00ffcc"]
            for glow_color in glow_colors:
                canvas.delete("glow")
                canvas.create_oval(x1-20, y1-20, x2+20, y2+20, fill=glow_color, outline="", tags="glow")
                root.update()
                time.sleep(0.1)
        
        root.update()
        time.sleep(0.4)
    except:
        root.update()
        time.sleep(0.4)

def solve(x, y):
    try:
        status_label.config(text="🧭 Exploring... Keep going little rat! 🐭")
        
        if x < 0 or y < 0 or x >= N or y >= N or maze[x][y] == 0:
            return False

        if (x, y) == (N-1, N-1):
            color_cell(x, y, "success")
            draw_rat(x, y)
            status_label.config(text="🎉 SUCCESS! The rat found the cheese! 🧀✨")
            return True

        color_cell(x, y, "path")
        maze[x][y] = 2
        draw_rat(x, y)
        status_label.config(text=f"🐭 at ({x},{y}) - Path found!")

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dx, dy in directions:
            if solve(x + dx, y + dy):
                return True
        
        color_cell(x, y, "deadend")
        status_label.config(text=f"💔 Dead end at ({x},{y}) - Backtracking...")
        time.sleep(0.2)
        return False
    except:
        return False

def reset_maze():
    global maze, current_rat_pos, rects
    maze = [
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    current_rat_pos = None
    canvas.delete("all")
    draw_grid()
    status_label.config(text="Ready! Click START 🐁")

def start():
    reset_maze()
    root.after(1000, solve, 0, 0)

draw_grid()

button_frame = tk.Frame(root, bg="#1a1a2e")
button_frame.pack(pady=20)

btn_start = tk.Button(button_frame, text="🚀 START ADVENTURE", command=start,
                     font=btn_font, bg="#00d4aa", fg="white",
                     activebackground="#00f5d4", activeforeground="white",
                     relief="flat", bd=0, padx=30, pady=12,
                     cursor="hand2")
btn_start.pack(side=tk.LEFT, padx=10)

btn_reset = tk.Button(button_frame, text="🔄 RESET", command=reset_maze,
                     font=btn_font, bg="#e94560", fg="white",
                     activebackground="#f05454", activeforeground="white",
                     relief="flat", bd=0, padx=30, pady=12,
                     cursor="hand2")
btn_reset.pack(side=tk.LEFT, padx=10)

instr_frame = tk.Frame(root, bg="#1a1a2e")
instr_frame.pack(pady=(10,0))

tk.Label(instr_frame, text="💡 Watch the rat explore using backtracking algorithm!", 
         font=("Segoe UI", 10), fg="#a8b4ff", bg="#1a1a2e").pack()

root.mainloop()
