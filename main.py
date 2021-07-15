# Author: Abu Siam
# Developed for: DSinnovators

import add as add_v
import remove as rmv_v
import show as shw_v





# main
if __name__ == '__main__':

    print("***************************************************")
    print("DSINNOVATORS VEHICLE SHOWROOM COMMAND LINE SYSTEM")
    print("By- Abu Siam ")
    print("***************************************************")
    print("Press Ctrl + F2 (For PyCharm) / Ctrl + c  to exit the program.")
    visitor_count = 30
    vehicle_list = {}


    while (True):
        print("------------------------------------------")
        print("Select Operation:")
        print("1.Add Vehicle")
        print("2.Remove Vehicle")
        print("3.Show Vehicles")
        print("4.Show current visitor number and vehicle list")
        print("(Type '1/2/3/4' to select)")
        print("------------------------------------------")
        op_input = input("Option: ")
        print()
        if op_input == '1':  # add vehicle option

            visitor_count = add_v.add_vehicle_to_showroom(vehicle_list, visitor_count)
        elif op_input == '2':  # remove vehicle option

            if len(vehicle_list) == 0:
                print("Sorry there is no vehicle available currently in the showroom. Please add one.")
                continue
            rmv_v.remove_vehicle(vehicle_list)
        elif op_input == '3':  # show vehicle list

            if len(vehicle_list) == 0:
                print("Sorry there is no vehicle available currently in the showroom. Please add one.")
                continue
            shw_v.show_vehicle_list(vehicle_list)
        elif op_input == '4':  # show vehicle list and visitor number

            if len(vehicle_list) == 0:
                print("Sorry there is no vehicle available currently in the showroom. Please add one.")
                print("------------------------------------------")
                print("Total number of visitors are: ", int(visitor_count), ".")
                print("------------------------------------------")
                continue


            shw_v.show_vehicle_list(vehicle_list)
            print("------------------------------------------")
            print("Total number of visitors are: ", int(visitor_count), ".")
            print("------------------------------------------")
        else:  # out of scope option

            print("Invalid option. Please try again.")
# type ctrl+c to exit from while true loop.
