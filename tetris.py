class tet:
    def __init__(self):
        self.tetramino_types = ['i', 'j', 'l', 'o', 's', 't', 'z']
        self.gameboard_dimensions = [10, 20]
        self.x_min = 1
        self.x_max = self.gameboard_dimensions[0]
        self.y_min = 1
        self.y_max = self.gameboard_dimensions[1]
    
    def gen_tetramino(self):
        import random
        self.tetramino_type = random.choice(self.tetramino_types)
        return self.tetramino_type
    
    def gen_initial_coords(self, tetramino_type):
        import random
        self.coords=[]
        if self.tetramino_type == 'i':
            self.initial_coord = random.randint(self.x_min,self.x_max-3)
            self.coords.append([self.initial_coord + 0, 1])
            self.coords.append([self.initial_coord + 1, 1])
            self.coords.append([self.initial_coord + 2, 1])
            self.coords.append([self.initial_coord + 3, 1])
            return self.coords
        if self.tetramino_type == 'j':
            self.initial_coord = random.randint(self.x_min,self.x_max-2)
            self.coords.append([self.initial_coord + 0, 1])
            self.coords.append([self.initial_coord + 1, 1])
            self.coords.append([self.initial_coord + 2, 1])
            self.coords.append([self.initial_coord + 2, 2])
            return self.coords
        if self.tetramino_type == 'l':
            self.initial_coord = random.randint(self.x_min,self.x_max-2)
            self.coords.append([self.initial_coord + 0, 1])
            self.coords.append([self.initial_coord + 1, 1])
            self.coords.append([self.initial_coord + 2, 1])
            self.coords.append([self.initial_coord + 0, 2])
            return self.coords
        if self.tetramino_type == 'o':
            self.initial_coord = random.randint(self.x_min,self.x_max-1)
            self.coords.append([self.initial_coord + 0, 1])
            self.coords.append([self.initial_coord + 1, 1])
            self.coords.append([self.initial_coord + 0, 2])
            self.coords.append([self.initial_coord + 1, 2])
            return self.coords
        if self.tetramino_type == 's':
            self.initial_coord = random.randint(self.x_min+1,self.x_max-1)
            self.coords.append([self.initial_coord + 1, 1])
            self.coords.append([self.initial_coord + 2, 1])
            self.coords.append([self.initial_coord + 0, 2])
            self.coords.append([self.initial_coord + 1, 2])
            return self.coords
        if self.tetramino_type == 't':
            self.initial_coord = random.randint(self.x_min,self.x_max-2)
            self.coords.append([self.initial_coord + 0, 1])
            self.coords.append([self.initial_coord + 1, 1])
            self.coords.append([self.initial_coord + 2, 1])
            self.coords.append([self.initial_coord + 1, 2])
            return self.coords
        if self.tetramino_type == 'z':
            self.initial_coord = random.randint(self.x_min,self.x_max-2)
            self.coords.append([self.initial_coord + 0, 1])
            self.coords.append([self.initial_coord + 1, 1])
            self.coords.append([self.initial_coord + 1, 2])
            self.coords.append([self.initial_coord + 2, 3])
            return self.coords
    
    def drop (self, coords):
        temp=[]
        for i in range(len(self.coords)):
            temp.append([self.coords[i][0], self.coords[i][1]+1])
        self.dropped_coords = temp
        return self.dropped_coords
               
    
    def move_horizontal(self, coords, delta):
        temp=[]
        for i in range(len(self.coords)):
            temp.append([self.coords[i][0]+delta, self.coords[i][1]])
        self.slid_ocords = temp
        return self.slid_coords
   
    def rotate(self, tetramino_type, coords, direction):
        subtractor = []
        temp = []
        temp2 = []
        rotated_coords = []
        if self.tetramino_type == 'i' or 'j' or 'l' or 't' or 'z':
            subtractor=self.coords[1]
        elif self.tetramino_type == 's':
            subtractor=self.coords[0]            
        for i in range(len(self.coords)):
            if direction == "cw":
                temp.append([self.coords[i][0]-subtractor[0], self.coords[i][1]-subtractor[1]])
                temp2.append([-temp[i][0], temp[i][1]])
                rotated_coords.append([temp2[i][0]+subtractor[0], temp2[i][1]+subtractor[1]])
            elif direction == "ccw":
                temp.append([self.coords[i][0]-subtractor[0], self.coords[i][1]-subtractor[1]])
                temp2.append([temp[i][0], -temp[i][1]])
                rotated_coords.append([temp2[i][0]+subtractor[0], temp2[i][1]+subtractor[1]])
        return rotated_coords
    
    def collision_check(self):
    #returns True if collision, False if no collision
        collision = False
    #checks for duplicate coordinates i.e. overlapping tetramino blocks
        for i in range(len(self.dropped_coords)):
            for j in range(len(game_pieces)):
                if self.dropped_coords[i] in game_pieces[j]:
                    collision = True
                    break
    #checks for tetramino block are out of bounds
        for coordinate_pair in self.dropped_coords:
            if coordinate_pair[0] > game_instance.x_max or coordinate_pair[0] < game_instance.x_min or coordinate_pair[1] > game_instance.y_max or coordinate_pair[1] < game_instance.y_min:
                collision = True
                break
        return collision
    
    def coord_change(self, collision, operation):
        if collision == False:
            if operation == 'rotate':
                self.coords = self.rotated_coords
            if operation == 'drop':
                self.coords = self.dropped_coords
            if operation == 'slide':
                self.coords = self.slid_coords
                return self.coords
        if collision == True or operation == 'none':
                return self.coords
          
    def draw_gameboard(self):
        self.gen_tetramino()
        self.gen_initial_coords(self.tetramino_type)

def gamepiece_append():
    game_pieces.append(game_instance.coords)
    return game_pieces
   
def row_clear_check():
    import itertools
    reduced_game_pieces = list(itertools.chain.from_iterable(game_pieces))
    i = game_instance.y_min
    for j in range(game_instance.y_min, game_instance.y_max+1):
        while i <= game_instance.x_max:
            if [i, j] in reduced_game_pieces:
                i+=1
                if i == game_instance.x_max:
                    for i in range(game_instance.x_min, game_instance.x_max+1):
                        reduced_game_pieces.remove([i, j])
            else:
                break

game_pieces=[]
game_instance = tet()

game_instance.draw_gameboard()
for i in range(0,42):
    game_instance.drop(game_instance.coords)
    game_instance.collision_check()
    row_clear_check()
    #print("running game_instance.collision_check() with")
    #print("game_instance.dropped_coords = %s" % game_instance.dropped_coords)
    #print("result of game_instance.collision_check() = %s " % game_instance.collision_check())
    if game_instance.collision_check() == False:
        #allow rotation
        print("No collision detected, so dropping one space.")
        #print("Current game_instance.coords are %s" % game_instance.coords)
        print("Current game_instance.dropped_coords are %s" % game_instance.dropped_coords)
        game_instance.coord_change(False, 'drop')
        #print("New game_instance.coords are %s" % game_instance.coords)
        #print("New game_instance.dropped_coords are %s" % game_instance.dropped_coords)
        print("Set of all coords is: %s" % game_pieces)
        print("\n")
    if game_instance.collision_check() == True:
        #print("Collision detected, so appending game piece with coords %s" % game_instance.coords)
        #print("Current game_instance.dropped_coords are %s" % game_instance.dropped_coords)
        #print("Current game_instance.coords are %s" % game_instance.coords)
        game_instance.coord_change(True, 'none')
        gamepiece_append()
        #print("game_instance.coords set equal to game_instance.dropped cords")
        print("Set of all coords is %s" % game_pieces)
        game_instance.draw_gameboard()
        print("\n")

'''
    Pass other working coord sets (dropped_coords, rotated_coords, slid_coords) to collision_check()
    DON'T append coords if collision is found for rotate/slide AND the coord still has room to fall;
        instead, disallow rotate/slide but let it continue to fall until there is no more room
    
    Flatten game_pieces by default so no need for reduced_game_pieces in row_clear_check().
        Rework any functions that use game_pieces?
    
    Game end is signaled by collision of tetramino as soon as it is created. How to check for this?
    
    Scan for inputs 30 times/sec
    Get input, store input type for passing as operation argument to coord_change
    For drop every 1 second
'''