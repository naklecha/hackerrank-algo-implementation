rows, cols, rotations = [int(x) for x in input().strip().split(" ")]
num_layers = int(min(rows, cols)/2)
layers = [[] for x in range(num_layers)]
data = []
for row in range(rows):
    data.append([int(x) for x in input().strip().split(" ")])

rows -= 1
cols -= 1

for current_layer in range(num_layers):
    i = j = current_layer
    while i < rows-current_layer:
        layers[current_layer].append(data[i][j])
        i += 1
    while j < cols-current_layer:
        layers[current_layer].append(data[i][j])
        j += 1
    while i > current_layer:
        layers[current_layer].append(data[i][j])
        i -= 1
    while j > current_layer:
        layers[current_layer].append(data[i][j])
        j -= 1

new_layers = []
for layer in layers:
    rots = rotations%len(layer)
    new_layers.append(list(layer[-rots:] + layer[:-rots]))

for current_layer in range(num_layers):
    i = j = current_layer
    while i < rows-current_layer:
        data[i][j] = new_layers[current_layer].pop(0)
        i += 1
    while j < cols-current_layer:
        data[i][j] = new_layers[current_layer].pop(0)
        j += 1
    while i > current_layer:
        data[i][j] = new_layers[current_layer].pop(0)
        i -= 1
    while j > current_layer:
        data[i][j] = new_layers[current_layer].pop(0)
        j -= 1  

for row in range(rows+1):
    for col in range(cols+1):
        print(data[row][col], end=" ")
    print()
