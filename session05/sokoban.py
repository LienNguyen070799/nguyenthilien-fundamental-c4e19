map = {
    "size_x": 5,
    "size_y" :5
}

player = {
    "x" : 3,
    "y": 4
}
boxes = [
    {"x" : 1,"y" :1},
    {"x" : 2, "y": 2},
    {"x" : 3,"y" : 3}
]
destinations = [
    {"x": 2,"y":1},
    {"x": 3,"y":2},
    {"x": 4,"y":3}
]
playing = True
while playing:

    for y in range(map["size_y"]):
        for x in range (map["size_x"]):
            destinations_is_here = False
            
            for destination in destinations:
                if destination["x"] == x and destination["y"] == y:
                    destinations_is_here = True
            player_is_here = False
            
            if player["x"] == x and player["y"] == y:
                    player_is_here =True
            box_is_here = False
            for box in boxes:
                if box["x"] == x  and box["y"] == y :
                    box_is_here = True

            if x == player["x"] and y == player["y"]:
                print("P", end =" ")
            elif box_is_here == True:
                print("B", end = " ")
            elif destinations_is_here == True:

                print("D", end =" ")
            
            else:
                print("-", end =" ")
            
        print()
    move = input(" Your move : ").upper()
    dx = 0
    dy = 0
    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "D":
        dx = 1
    elif move == "A":
        dx = -1
    else:
        print("Buzzz")
        playing =False
    if 0 <= player["x"] +dx <= map['size_x'] and 0 <= player["y"] +dy <= map['size_y'] :
        player['x'] += dx
        player ['y'] += dy
    # for box in boxes:
    #     if box["x"] == player ["x"] and box["y"] == player ["y"]:
            