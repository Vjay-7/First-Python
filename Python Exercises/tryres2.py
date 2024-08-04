
#Restaurant Reservation


#from tabulate import tabulate
def view_reservation(r_list):
    reserv_list=[]
    reserv_list.append(r_list())
    print(reserv_list)

def make_reservation():
     names= str(input('Name: '))b
     date= str(input('Date: '))
     time= str(input('Time: '))
     no_adult= int(input('Number of Adults: '))
     no_children= int(input('Number of Children: '))
     no_seniors= int(input('Number of Senior Citizens: '))
     reserv= [names, date, time, no_adult, no_children, no_seniors]
     return reserv

def delete_reservation():
    delete_rev= input('Enter Reservatoin Number: ')
    #reserv_list[delete_rev-1].remove()

def generate_reservation():
    None

while True:
    print("\t\t Welcome to Veejay's Buffet Restaurant \n System Menu:")
    print(" a. View all Reservations\n b. Make Reservations\n c. Delete Reservation\n d. Generate Report\n e. Exit ")

    choice= input("\nSelect: ")

    if choice == 'a':
        view_reservation(make_reservation)
    elif choice == 'b':
        make_reservation()
    elif choice == 'c':
        delete_reservation()
    elif choice == 'd':
        generate_reservation()
    elif choice == 'e': break

