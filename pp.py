class CarManagement:
  class Car:
    def __init__(self,car_ID,car_name,car_model,car_price):
      self.car_Id = car_ID
      self.car_name = car_name
      self.car_model = car_model
      self.car_price = car_price
      
  def __init__(self):
      self.cars = []
      
  def add_car(self):
      car_Id = int(input("Enter car Id :"))
      car_name = input("Enter car Name :")
      car_model = int(input("Enter car Model :"))
      car_price = int(input("Enter car Price :"))
      
      c = self.Car(car_Id,car_name,car_model,car_price)
      self.cars.append(c)
      print("cars added successfully !")
      
  def show_car(self):
      for c in self.cars:
        print("car_Id :",c.car_Id,
              "car_name :",c.car_name,
              "car_model :",c.car_model,
              "car_price : ",c.car_price)
        
  def delete_car(self):
      car_Id = int(input("Enter car ID :"))
      for c in self.cars:
        if c.car_Id == car_Id:
          self.cars.remove(c)
          
          print("car remove successfullt !")
          return
        
        else:
          print("invalid car Id")
        
car = CarManagement()

while(True):
  print("1. add car")
  print("2. show car")
  print("3. delete car")
  print("4. exit")
  
  ch = int(input("enter your choice : "))
  
  if ch == 1:
    car.add_car()
    
  elif ch == 2:
    car.show_car()
    
  elif ch == 3:
    car.delete_car()
    
  elif ch == 4:
    print("exit successfuly from carManagement")
    break
  
  else:
    print("invalid choice  !")
    
  
  
  
    
      
      
    
      