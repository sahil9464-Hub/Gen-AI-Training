class HouseManagement:
    class House:
        def __init__(self,house_id,location,price,rooms):
            self.house_id = house_id
            self.location = location
            self.price = price
            self.rooms = rooms

    def __init__(self):
        self.houses=[]

    def add_house(self):
        house_id = int(input("Enter House_Id:"))
        location = input("Enter House Location:")
        price = int(input("Enter House Price:"))
        rooms = int(input("Enter Number of Rooms:"))

        h = self.House(house_id,location,price,rooms)
        self.houses.append(h)
        print("House Added Successfully")

    def show_houses(self):
        for h in self.houses:
            print(h.location,h.price,h.rooms)

    def delete(self):
        house_id = int(input("Enter House_ID:"))
        for h in self.houses:
            if h.house_id == house_id:
                self.houses.remove(h)
                print("House Deleted Successfully !")
                return
        else:
            print("House is not Available !")


house = HouseManagement()

while True:
    print("1. Add House")
    print("2. Display Houses")
    print("3. Delete House")
    print("4. Exit")
    
    ch = int(input("Enter choice:"))

    if ch == 1:
        house.add_house()

    elif ch == 2:
        house.show_houses()

    elif ch == 3:
        house.delete()

    elif ch == 4:
        print("Exit From House Management !!!")
        break

    else:
        print("Invalid Choice !")