# Displays all available vehicle list

def show_vehicle_list(vehicle_list):
    """
    :param vehicle_list:
    :return:
    """
    id = 1
    for value in vehicle_list.values():
        print("------------------------------------------")
        print("VEHICLE NO. #", id)
        id += 1
        print(value)
