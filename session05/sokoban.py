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
    {"x": 2," y":1},
    {"x": 3," y":2},
    {"x": 4," y":3}
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
            
            if play["x"] == x and play["y"] == y:
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

                print("P", end =" ")
            
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
    elif move == "S":
        dx = -1
    else:
        print("Buzzz")
        playing =False
    if player["x"] +dx >= 0 and player["x"] +dx < 4 and player["y"] +dy >= 0 and player["y"] +dy < 4:
        player['x'] += dx
        player ['y'] += dy
    for box in boxes:
        if box["x"] == player ["x"] and box["y"] == player ["y"]:
            