### Class Player
This file contains the logic of the Player class.

__Attributes__

* `name`
    - data: str
    - description: ship's name

*  `enemy_ocean_representation`
    - data: Ocean
    - description: create instance class Ocean 
                    
*   `player_ocean`
    - data: Ocean
    - description: create instance class Ocean

*   `init_ships_dict`
    - data: dict
    - description: call method init_ships_dict 

*   `sunken_ships`
    - data: list 
    - description: create list

__Instance methods__

* `__init__(self) `

  Constructs a *Player* object.

* `append_sunken_ship(self, hit_object)`

    

* `init_ships_dict(self)`

  

* `add_ship_to_ocean(self, ship_name, coordinates, turn=True)`

   

* `check_is_water(self, column, row, ship_length, turn)`

    

* `check_range(self, column, row, ship_length, turn)`


* `shoot_ship(self, enemy, shooted_object)`

    

* `_copy_object(self, object_to_shoot, shoot_coordinates)`

    

