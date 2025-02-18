import customtkinter as ctk
from functools import partial

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.geometry('450x700')  
root.title("OLL Solver")

sequence = ''

squares = [
    [1, 1, 0], [1, 2, 0], [1, 3, 0],
    [2, 1, 0], [2, 2, 0], [2, 3, 0],
    [3, 1, 0], [3, 2, 0], [3, 3, 0]
]

edges = [
    [0, 1, 0], [0, 2, 0], [0, 3, 0],
    [1, 0, 0], [2, 0, 0], [3, 0, 0],
    [1, 4, 0], [2, 4, 0], [3, 4, 0],
    [4, 1, 0], [4, 2, 0], [4, 3, 0]
]

touching_center = [
    [1, 2, 1], [2, 1, 1],
    [2, 3, 1], [3, 2, 1]
]

corners = [
    [1, 1, 1], [1, 3, 1],
    [3, 1, 1], [3, 3, 1]
]

def solve_sequence():

    global sequence
    sequence = ''
    active_corners = 0
    centertouchers = 0

    active_squares = []
    for square in squares:
        if square[2] == 1: 
            active_squares.append(square)
    
    active_edges = []
    for edge in edges:
        if edge[2] == 1:
            active_edges.append(edge)

    for square in corners:
        if square in active_squares:
            active_corners += 1
    for square in touching_center:
        if square in active_squares:
            centertouchers += 1
            
    if len(active_edges) + len(active_squares) != 9:
            sequence = "Error! Must be 9 active squares."
    
    else:
        #dot pattern
        if centertouchers == 0:
            if len(active_squares) >= 1:
                sequence = "F, R, U, R', U', F'"
        #l patterns        
        if centertouchers == 2:
            if all(square in active_squares for square in [squares[3], squares[4], squares[5]]):
                sequence = "F, R, U, R', U', F'"
            elif all(square in active_squares for square in [squares[1], squares[4], squares[7]]):
                sequence = "U, F, R, U, R', U', F'"
            elif all(square in active_squares for square in [squares[1], squares[4], squares[3]]):
                sequence = "U2, f, R, U, R', U', f'"
            elif all(square in active_squares for square in [squares[1], squares[4], squares[5]]):
                sequence = "U', f, R, U, R', U', f'"   
            elif all(square in active_squares for square in [squares[3], squares[4], squares[7]]):
                sequence = "U, f, R, U, R', U', f'"   
            elif all(square in active_squares for square in [squares[5], squares[4], squares[7]]):
                sequence = "f, R, U, R', U', f'"   
        #other patterns
        if centertouchers == 4:
            #crosspatterns
            if active_corners == 0:
                if all(square in active_edges for square in [edges[3], edges[5], edges[6], edges[8]]):
                    sequence = "R, U, R', U, R, U', R', U, R, U2, R'"
                elif all(square in active_edges for square in [edges[0], edges[2], edges[9], edges[11]]):
                    sequence = "U, R, U, R', U, R, U', R', U, R, U2, R'"
                elif all(square in active_edges for square in [edges[3], edges[5], edges[2], edges[11]]):
                    sequence = "R, U, R', U, R, U2, R', U' R, U, R', U, R, U2, R'"
                elif all(square in active_edges for square in [edges[0], edges[2], edges[5], edges[8]]):
                    sequence = "U', R, U, R', U, R, U2, R', U' R, U, R', U, R, U2, R'"    
                elif all(square in active_edges for square in [edges[0], edges[6], edges[8], edges[9]]):
                    sequence = "U2, R, U, R', U, R, U2, R', U' R, U, R', U, R, U2, R'"    
                elif all(square in active_edges for square in [edges[3], edges[6], edges[11], edges[9]]):
                    sequence = "U, R, U, R', U, R, U2, R', U' R, U, R', U, R, U2, R'"         
            #left fishpatterns
            if active_corners == 1:
                if edges[9] in active_edges and squares[8] in active_squares:
                    sequence = "L', U', L, U', L', U2, L"
                elif edges[8] in active_edges and squares[2] in active_squares:
                    sequence = "U, L', U', L, U', L', U2, L"    
                elif edges[3] in active_edges and squares[6] in active_squares:
                    sequence = "U', L', U', L, U', L', U2, L" 
                elif edges[2] in active_edges and squares[0] in active_squares:
                    sequence = "U2, L', U, L, U, L', U2, L" 
            #right fishpatterns
                elif edges[11] in active_edges and squares[6] in active_squares:
                    sequence = "R, U, R', U, R, U2, R'"
                elif edges[5] in active_edges and squares[0] in active_squares:
                    sequence = "U', R, U, R', U, R, U2, R'"    
                elif edges[0] in active_edges and squares[2] in active_squares:
                    sequence = "U2, R, U, R', U, R, U2, R'"  
                elif edges[6] in active_edges and squares[8] in active_squares:
                    sequence = "U, R, U, R', U, R, U2, R'"  
            #weird patterns
            if active_corners == 2:
                # Bad G
                if edges[5] in active_edges and edges[3] in active_edges and squares[8] in active_squares and squares[2] in active_squares:
                    sequence = "r, U, R', U', r', F, R, F'"
                elif edges[9] in active_edges and edges[11] in active_edges and squares[0] in active_squares and squares[2] in active_squares:
                    sequence = "U, r, U, R', U', r', F, R, F'"
                elif edges[6] in active_edges and edges[8] in active_edges and squares[0] in active_squares and squares[6] in active_squares:
                    sequence = "U2, r, U, R', U', r', F, R, F'"
                elif edges[0] in active_edges and edges[2] in active_edges and squares[6] in active_squares and squares[8] in active_squares:
                    sequence = "U', r, U, R', U', r', F, R, F'"
                # Good G
                elif edges[0] in active_edges and edges[9] in active_edges and squares[8] in active_squares and squares[2] in active_squares:
                    sequence = "r, U, R', U', r', F, R, F'"
                elif edges[5] in active_edges and edges[8] in active_edges and squares[0] in active_squares and squares[2] in active_squares:
                    sequence = "U, r, U, R', U', r', F, R, F'"
                elif edges[2] in active_edges and edges[11] in active_edges and squares[0] in active_squares and squares[6] in active_squares:
                    sequence = "U2, r, U, R', U', r', F, R, F'"
                elif edges[3] in active_edges and edges[6] in active_edges and squares[6] in active_squares and squares[8] in active_squares:
                    sequence = "U', r, U, R', U', r', F, R, F'"
                # S pattern
                elif edges[2] in active_edges and edges[5] in active_edges and squares[0] in active_squares and squares[8] in active_squares:
                    sequence = "R, U, R', U, R, U', R', U, R, U', R', U, R, U2, R'"
                elif edges[0] in active_edges and edges[8] in active_edges and squares[2] in active_squares and squares[6] in active_squares:
                    sequence = "U', R, U, R', U, R, U', R', U, R, U', R', U, R, U2, R'"
                elif edges[6] in active_edges and edges[9] in active_edges and squares[0] in active_squares and squares[8] in active_squares:
                    sequence = "U2, R, U, R', U, R, U', R', U, R, U', R', U, R, U2, R'"
                elif edges[3] in active_edges and edges[11] in active_edges and squares[2] in active_squares and squares[6] in active_squares:
                    sequence = "U, R, U, R', U, R, U', R', U, R, U', R', U, R, U2, R'"

        if sequence == '':
            sequence = 'Invalid Pattern'
    

    print(sequence)
    solve_label.configure(text=sequence)
    

    
def toggle_color(list, button, i):
    if list[i][2] == 0:
        button.configure(fg_color="yellow")  
        list[i][2] = 1  
    else:
        button.configure(fg_color="white")  
        list[i][2] = 0  
    print(f"Changed item: {list[i]}")

square_buttons = []
for i, square in enumerate(squares):
    row, col, _ = square  
    square = ctk.CTkButton(root, text='', width=100, height=100, fg_color="white", hover=False)  
    square.configure(command=lambda btn=square, idx=i, list=squares: toggle_color(list, btn, idx))  
    square.grid(row=row, column=col, padx=5, pady=5)
    square_buttons.append(square)

edge_buttons = []
for i, edge in enumerate(edges):
    row, col, _ = edge
    if col == 0 or col == 4:  
        edge_width, edge_height = 35, 75  
    else:  
        edge_width, edge_height = 75, 35  
    edge = ctk.CTkButton(root, text='', width = edge_width, height=edge_height, fg_color="white", hover=False)
    edge.configure(command= lambda btn = edge, idx=i, list=edges: toggle_color(list, btn, idx))
    edge.grid(row=row, column=col, padx=10, pady=10)
    edge_buttons.append(edge)
    
solve_button = ctk.CTkButton(root, text="Solve", command=solve_sequence)
solve_button.grid(row=6, column=0, columnspan=6, pady=10, sticky='ew')
solve_label = ctk.CTkLabel(root, text=sequence, font=("Arial", 18))
solve_label.grid(row=7, column=0, columnspan=7, pady=10, sticky='ew')
info_label = ctk.CTkLabel(root, text="If not fully solved, enter pattern and solve again", font=("Arial", 14))
info_label.grid(row=9, column=0, columnspan=7, pady=10, sticky='ew')

root.mainloop()