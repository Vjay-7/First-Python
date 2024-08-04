

from tabulate import tabulate
res_no= 0
reserv_list= []

def all_reservation(reserv_list):
    for x in range(len(reserv_list)):        #---------------> I used for loop to print tabulated data execpt to the last data in every nested list
            if x == 0:
                print(tabulate([reserv_list[x][:8]],headers=['Res No.', 'Name', 'Date','Time', 'No. of Adults', \
                    'No. Children', 'No. Senior Citizen','Total Guest']))
            else:
                print(tabulate([reserv_list[x][:8]],headers=['       ', '    ', '    ','    ',\
                     '             ', '             ', '                 ','           ']))

def user_input():
         res_no += 1
         names= str(input('Name: '))
         date= str(input('Date: '))
         time= str(input('Time: '))
         no_adult= int(input('Number of Adults: '))
         no_children= int(input('Number of Children: '))
         no_seniors= int(input('Number of Senior Citizens: '))
         total_guest= no_adult + no_children + no_seniors
         sub_total= (no_adult*500) + (no_children*250) + (no_seniors*400)
         reserv_list.append([res_no, names, date, time, no_adult, no_children, no_seniors, total_guest, sub_total])
         return reserv_list

def user_delete(reserv_list):
        delete_rev= int(input('Enter Reservation Number: '))
        reserv_list.remove(reserv_list[delete_rev-1])               #--------> remove the list inside a list with specific index
        print("Reservation No.",delete_rev, "Deleted Successfully")

def print_all_choices(reserv_list):
        print('//////////////////////////////////////////////\nAdult – P500.00 \
            \nChildren – P250.00 \nSenior Citizen – P400.00')
        reserv_no= int(input('Enter Reservation Number: '))
        print(tabulate([reserv_list[(reserv_no-1)]],headers=['Res No.', 'Name', 'Date','Time', \
            'No. of Adults', 'No. Children', 'No. Senior Citizen','Total Guest', 'Total Amount'])) 


while True:    #------------------------------------> I used infinte while loop and it breaks if the user choose "e"
    print("\n\n\t\t Welcome to Veejay's Buffet Restaurant \n System Menu:")
    print(" a. View all Reservations\n b. Make Reservations\n c. Delete Reservation\n d. Generate Report\n e. Exit ")
    
    choice= input("\nSelect: ")
    
    if choice == 'a' or choice == 'A':
        all_reservation(user_input())

    elif choice == 'b' or choice == 'B':
        user_input()
    elif choice == 'c' or choice== 'C':
        user_delete(user_input)

    elif choice == 'd' or choice=='D':
        print_all_choices(user_input)    #-----> print the data using table inside the index selected

    elif choice == 'e':      #--------> breaks the infinite while loop as exit to the application
        print('~~~~~~~~~~~~~~~~~~~~~~ Thank you! ~~~~~~~~~~~~~~~~~~~~~~~~~')
        break

