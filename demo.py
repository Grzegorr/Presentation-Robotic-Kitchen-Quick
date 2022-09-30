from Jerrys_Main import *
import time


################### GLOBAL VARIABLES ############################
salt_amount = 1.0
water_amount = 2.0

ready_position_waypoint = [0.27, 0.12, 0.66, 0, 0, 1.61]

dip_sensor = [0.27, 0.12, 0.70, 0, 0, 1.61]

above_ready_waypoint = [0.27, 0.12, 0.46, 0, 0, 1.61]
above_rotate_waypoint_j = [-177 * 3.14/180, -118 * 3.14/180, 131 * 3.14/180, -102 * 3.14/180, -90 * 3.14/180, 0 * 3.14/180]
down_to_mix = [0.269, 0.124, 0.4, 2.270, -2.152, 0] #start z is 0.292

#mixing
to_the_soup = [0.269, 0.124, 0.46, 2.270, -2.152, 0]
zigzag_waypoint_1 = [0.30, 0.15, 0.46, 2.270, -2.152, 0]
zigzag_waypoint_2 = [0.22, 0.20, 0.46, 2.270, -2.152, 0]
zigzag_waypoint_3 = [0.2, 0.06, 0.46, 2.270, -2.152, 0]

up_after_mix = [0.269, 0.124, 0.292, 2.270, -2.152, 0]
above_unrotate_waypoint_j = [-177 * 3.14/180, -118 * 3.14/180, 131 * 3.14/180, -102 * 3.14/180, 90 * 3.14/180, 0 * 3.14/180]

##adding water and salt
out_of_pot = above_ready_waypoint = [0.27, 0.12, 0.56, 0, 0, 1.61]


################### PRE-PROGRAMMED MOVES ########################
def add_salt(Robot):
    Robot.A.sendSignal(salt_amount, 0.0)

def add_water(Robot):
    Robot.A.sendSignal(0.0, water_amount)

def ready_position(Robot):
    Robot.UR.moveL(ready_position_waypoint)

def dip_sensors_from_ready(Robot):
    Robot.UR.moveL(dip_sensor)
    time.sleep(5)
    Robot.UR.moveL(ready_position_waypoint)


def from_ready_mix(Robot):
    ## Ready position
    Robot.UR.moveL(above_ready_waypoint)
    Robot.UR.moveJ(above_rotate_waypoint_j)
    Robot.UR.moveL(down_to_mix)
    #mixing
    Robot.UR.moveL(to_the_soup)
    Robot.UR.moveL(zigzag_waypoint_1)
    Robot.UR.moveL(zigzag_waypoint_2)
    Robot.UR.moveL(zigzag_waypoint_1)
    Robot.UR.moveL(zigzag_waypoint_3)

    Robot.UR.moveL(to_the_soup)
    Robot.UR.moveL(zigzag_waypoint_1)
    Robot.UR.moveL(zigzag_waypoint_2)
    Robot.UR.moveL(zigzag_waypoint_1)
    Robot.UR.moveL(zigzag_waypoint_3)
    Robot.UR.moveL(to_the_soup)

    Robot.UR.moveL(zigzag_waypoint_1)
    Robot.UR.moveL(zigzag_waypoint_2)
    Robot.UR.moveL(zigzag_waypoint_1)
    Robot.UR.moveL(zigzag_waypoint_3)

    Robot.UR.moveL(zigzag_waypoint_1)

    #going back to ready
    Robot.UR.moveL(up_after_mix)
    Robot.UR.moveJ(above_unrotate_waypoint_j)
    Robot.UR.moveL(ready_position_waypoint)

def from_ready_mix_short(Robot):
    ## Ready position
    Robot.UR.moveL(above_ready_waypoint)
    Robot.UR.moveJ(above_rotate_waypoint_j)
    Robot.UR.moveL(down_to_mix)
    #mixing
    Robot.UR.moveL(to_the_soup)
    Robot.UR.moveL(zigzag_waypoint_1)
    Robot.UR.moveL(zigzag_waypoint_2)
    Robot.UR.moveL(zigzag_waypoint_1)
    Robot.UR.moveL(zigzag_waypoint_3)

    Robot.UR.moveL(zigzag_waypoint_1)

    #going back to ready
    Robot.UR.moveL(up_after_mix)
    Robot.UR.moveJ(above_unrotate_waypoint_j)
    Robot.UR.moveL(ready_position_waypoint)

def add_ingredients_from_ready(Robot):
    Robot.UR.moveL(out_of_pot)
    add_water(Robot)
    time.sleep(3)
    add_salt(Robot)
    time.sleep(3)
    Robot.UR.moveL(ready_position_waypoint)

################### DEMO SEQUENCE ###############################
def demo_sequence(Robot):
    # Presentation loop - runs for a long time without human input
    while True:
        ready_position(Robot)
        from_ready_mix_short(Robot)
        dip_sensors_from_ready(Robot)
        add_ingredients_from_ready(Robot)

def test_salt_water(Robot):
    # Startup Sequence
    Robot.UR.moveToSetupPosition()
    print("This is the setup position.")
    time.sleep(2)
    #Robot.UR.moveToReadyPosition()
    print("This is the ready position.")
    time.sleep(2)

    add_water(Robot)
    add_salt(Robot)

    Robot.UR.moveToReadyPosition()

def moves_only(Robot):
    while True:
        ready_position(Robot)
        dip_sensors_from_ready(Robot)
        from_ready_mix(Robot)



if __name__ == "__main__":
    print("Running demo as main")
    Robot = cookingRobot(enableArduino = True, enableDaq = False, enableUR = True)
    #test_salt_water(Robot)
    demo_sequence(Robot)
