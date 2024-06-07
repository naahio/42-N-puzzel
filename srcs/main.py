import os

def print_map(map_data):
    graph_map = ""
    num_rows = len(map_data)
    num_cols = len(map_data[0])

    node_labels = {}
    for row_idx, row in enumerate(map_data):
        for col_idx, cell in enumerate(row):
            node_labels[(row_idx, col_idx)] = cell
    
    for row_idx, row in enumerate(map_data):
        for col_idx, cell in enumerate(row):
            node_label = node_labels[(row_idx, col_idx)]
            graph_map += f"{node_label} -> "

            if row_idx > 0:
                neighbor_label = node_labels[(row_idx-1, col_idx)]
                graph_map += f"{neighbor_label} "
            if row_idx < num_rows - 1:
                neighbor_label = node_labels[(row_idx+1, col_idx)]
                graph_map += f"{neighbor_label} "
            if col_idx > 0:
                neighbor_label = node_labels[(row_idx, col_idx-1)]
                graph_map += f"{neighbor_label} "
            if col_idx < num_cols - 1:
                neighbor_label = node_labels[(row_idx, col_idx+1)]
                graph_map += f"{neighbor_label} "
            
            graph_map += "\n"
    
    print(graph_map)


def file_parser(file_name):
    default_path = "../maps/"

    if not os.path.isabs(file_name):
        file_name = os.path.join(default_path, file_name)
    
    try:
        with open(file_name, 'r') as file:
            data = []
            empty_case = None
            for row_idx, line in enumerate(file):
                integers = [int(num) for num in line.split()]
                data.append(integers)

                if 0 in integers:
                    col_idx = integers.index(0)
                    empty_case = (row_idx, col_idx)

            print_map(data)
    
    except FileNotFoundError:
        print("File not found:", file_name)

file_parser("3x3.txt")
