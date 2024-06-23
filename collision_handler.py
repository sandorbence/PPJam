class CollisionHandler:
    @classmethod
    def check_collision(cls, object1, object2):
        hitbox_half_x_1 = (object1.hitbox_x / 2)
        hitbox_half_y_1 = (object1.hitbox_y / 2)
        hitbox_half_x_2 = (object2.hitbox_x / 2)
        hitbox_half_y_2 = (object2.hitbox_y / 2)

        object1_left = object1.position.x - hitbox_half_x_1
        object1_right = object1.position.x + hitbox_half_x_1
        object1_top = object1.position.y - hitbox_half_y_1
        object1_bot = object1.position.y + hitbox_half_y_1

        object2_left = object2.position.x - hitbox_half_x_2
        object2_right = object2.position.x + hitbox_half_x_2
        object2_top = object2.position.y - hitbox_half_y_2
        object2_bot = object2.position.y + hitbox_half_y_2

        if object1_left < object2_right and object1_right > object2_left and object1_top < object2_bot and object1_bot > object2_top:
            return True

        return False
