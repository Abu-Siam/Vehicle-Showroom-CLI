from sports_vehicle import SportsVehicle
from normal_vehicle import NormalVehicle
from heavy_vehicle import HeavyVehicle


def add_vehicle_to_showroom(vehicle_list, visitor_count):
    """
    From given choice vehicles are created and added to the vehiclelist.
    :param vehicle_list:
    :param visitor_count:
    :return: current visitors number
    """
    model_no = input("Model number of car: ")
    print("")
    if validate_model(model_no, vehicle_list) == False:                 # check given model_no already exists or not
        return 0
    while (True):
        print("Type of car : ")
        print("1.Normal Vehicle \t 2.Sports Vehicle \t 3.Heavy Vehicle")
        print("(Type '1/2/3' to select)")
        car_option = input()
        print("")
        if car_option == '1':
            vehicle_list[str(model_no)] = add_normal_vehicle(model_no)  # Add Normal vehicle to list
            break
        elif car_option == '2':
            visitor_count += 20                                          # visitor number increase by 20
            vehicle_list[str(model_no)] = add_sports_vehicle(model_no)   # Add sports vehicle to list
            break
        elif car_option == '3':

            vehicle_list[str(model_no)] = add_heavy_vehicle(model_no)    # Add heavy vehicle to list
            break
        else:
            print("Invalid choice. Please try again.")
            continue
    print("\nVehicle model no. ", model_no, " is added.")
    return visitor_count


def validate_model(model_no, vehicle_list):
    """
    :param model_no:
    :param vehicle_list:
    :return: checks if certain model no already exists.1 if exists ,0 if not
    """
    if not model_no:
        print("Invalid input")
        return False

    if model_no in vehicle_list:
        print("This model number already exists. Please try again.")
        return False
    else:
        return True


def add_normal_vehicle(model_no):
    """

    :param model_no:
    :return: a normal vehicle object
    """
    car_type = "Normal"
    engine_type = process_engine_type()
    engine_power = process_engine_power()
    tire_size = process_tire_size()

    new_vehicle = NormalVehicle(model_no, car_type, engine_type, engine_power, tire_size)
    return new_vehicle


def process_engine_type():
    """

    :return: A valid normal vehicle engine type option.(1-3)> oil,gas,diesel
    """
    while (True):
        print("Type of engine: ")
        print("1.Oil \t 2.Gas \t 3.Diesel")
        print("(Type '1/2/3' to select)")
        engine_option = input()
        print("")
        if engine_option == '1':
            engine_type = "Oil"
            break
        elif engine_option == '2':
            engine_type = "Gas"
            break
        elif engine_option == '3':
            engine_type = "Diesel"
            break
        else:
            print("Invalid choice. Please try again.")
            continue
    return engine_type


def process_engine_power():
    """

    :return: A valid engine power amount.Rejects characters.
    """
    while (True):
        try:
            engine_power = float(input("Power of engine(C.C.): "))
            print("")
            break
        except ValueError as ex:
            print("Invalid input. Please try again.")
            continue

    return engine_power


def process_tire_size():
    """

    :return: A valid tire size. Rejects characters.
    """
    while (True):
        try:
            tire_size = float(input("Size of tire (Inch) : "))
            print("")
            break;


        except ValueError as ex:
            print("Invalid input. Please try again.")
            continue
    return tire_size


def process_weight():
    """

    :return:A valid weight of heavy vehicle .Rejects characters.
    """
    while (True):
        try:
            weight = float(input("Weight of the vehicle(kg): "))

            break
        except ValueError as ex:
            print("Invalid input. Please try again.")
            continue
    return weight


def add_sports_vehicle(model_no):
    """
    :param model_no:
    :return: a sports vehicle object
    """
    car_type = "Sports"
    engine_type = "Oil"
    print("Default engine type of sports vehicle is oil.")
    engine_power = process_engine_power()
    tire_size = process_tire_size()
    while (True):

        turbo_option = input("Has turbo? (Type 'y/n') : ")
        if turbo_option == 'y':
            turbo = "Yes"
            break
        elif turbo_option == 'n':
            turbo = "No"
            break
        else:
            print("Invalid input.Please try again.")
            continue

    new_vehicle = SportsVehicle(model_no, car_type, engine_type, engine_power, tire_size, turbo)
    return new_vehicle


def add_heavy_vehicle(model_no):
    """

    :param model_no:
    :return: Returns a heavy vehicle object.
    """
    car_type = 'Heavy'
    engine_type = "Diesel"
    print("Default engine type of heavy vehicle is diesel.")
    engine_power = process_engine_power()
    tire_size = process_tire_size()
    weight = process_weight()

    new_vehicle = HeavyVehicle(model_no, car_type, engine_type, engine_power, tire_size, weight)
    return new_vehicle
