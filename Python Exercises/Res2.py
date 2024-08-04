

from tabulate import tabulate
res_no= 0
reserv_list= []
reserv_list1=[]

while True:
    print("\n\n\t\t Welcome to Veejay's Buffet Restaurant \n System Menu:")
    print(" a. View all Reservations\n b. Make Reservations\n c. Delete Reservation\n d. Generate Report\n e. Exit ")
    
    choice= input("\nSelect: ")
    
    if choice == 'a' or choice == 'A':
         print(tabulate(reserv_list1,headers=['Res No.', 'Name', 'Date','Time', 'No. of Adults', 'No. Children', 'No. Senior Citizen','Total Guest']))

    elif choice == 'b' or choice == 'B':
         res_no += 1
         names= str(input('Name: '))
         date= str(input('Date: '))
         time= str(input('Time: '))
         no_adult= int(input('Number of Adults: '))
         no_children= int(input('Number of Children: '))
         no_seniors= int(input('Number of Senior Citizens: '))
         total_guest= no_adult + no_children + no_seniors
         sub_total= (no_adult*500) + (no_children*250) + (no_seniors*400)
         reserv_list1.append([res_no, names, date, time, no_adult, no_children, no_seniors, total_guest])
         reserv_list.append([res_no, names, date, time, no_adult, no_children, no_seniors, total_guest, sub_total])

    elif choice == 'c' or choice== 'C':
        delete_rev= int(input('Enter Reservation Number: '))
        reserv_list.remove(reserv_list[delete_rev-1])

    elif choice == 'd' or choice=='D':
        print('\n\n\nAdult – P500.00 \nChildren – P250.00 \nSenior Citizen – P400.00')
        print(tabulate(reserv_list,headers=['Res No.', 'Name', 'Date','Time', 'No. of Adults', 'No. Children', 'No. Senior Citizen','Total Guest', 'Total Amount']))

    elif choice == 'e': 
        print('Thank you!')
        break

