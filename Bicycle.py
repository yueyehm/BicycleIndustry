from enum import Enum
WheelMode = Enum("WheelMode", 'W16, W20, W28')
FrameMaterial = Enum("FrameMaterial", 'aluminum carbon steel')
BikeModels = Enum("BikeModels", 'A B C D E F G')
PriceWheel = {WheelMode.W16 : 100, WheelMode.W20 : 150, WheelMode.W28 : 200}
PriceFrame = {FrameMaterial.steel : 100, FrameMaterial.aluminum : 200, FrameMaterial.carbon : 300}
WeightWheel = {WheelMode.W16 : 25, WheelMode.W20 : 30, WheelMode.W28 : 35}
WeightFrame = {FrameMaterial.steel : 100, FrameMaterial.aluminum : 60, FrameMaterial.carbon : 40}

class Bicycle():
    def __init__(self, name, bikeModel, manufacturer):
        self.name = name
        if(isinstance(bikeModel, BikeModels)):
            self.bikeModel = bikeModel
            if(bikeModel == BikeModels.A):
                self.wheelMode = WheelMode.W16
                self.FrameMaterial = FrameMaterial.aluminum
            elif(bikeModel == BikeModels.B):
                self.wheelMode = WheelMode.W16
                self.FrameMaterial = FrameMaterial.carbon
            elif(bikeModel == BikeModels.C):
                self.wheelMode = WheelMode.W20
                self.FrameMaterial = FrameMaterial.aluminum
            elif(bikeModel == BikeModels.D):
                self.wheelMode = WheelMode.W20
                self.FrameMaterial = FrameMaterial.carbon
            elif(bikeModel == BikeModels.E):
                self.wheelMode = WheelMode.W28
                self.FrameMaterial = FrameMaterial.aluminum
            elif(bikeModel == BikeModels.F):
                self.wheelMode = WheelMode.W28
                self.FrameMaterial = FrameMaterial.steel
        else:
            print("Invalid bike model")
        self.cost = PriceWheel[self.wheelMode] * 2 + PriceFrame[self.FrameMaterial]
        self.weight = WeightWheel[self.wheelMode] * 2 + WeightFrame[self.FrameMaterial]
        self.manufacturer = manufacturer
    
class BikeShops():
    def __init__(self, name, inventory=[]):
        self.name = name
        self.inventory = inventory
        self.profit = 0
        self.dicInventory = {}
    
    def sellBike(self, bikeModel):
        biketoSell = [ item for item in self.inventory if item.bikeModel == bikeModel and self.dicInventory[bikeModel]]
        if(biketoSell):
            bike = biketoSell.pop()
            print("sell bike: {}".format(bike.name))
            self.profit += bike.cost * 0.2
            self.dicInventory[bikeModel] -= 1
            return bike
        else:
            print("Get more bike to the inventory")
            return None
    
    def purchaseBike(self, manufacturer, bikeModel, number):
        if(isinstance(manufacturer, Manufacturer) and isinstance(bikeModel, BikeModels) and isinstance(number, int)):
            if(bikeModel in manufacturer.bikeModels):
                bike = manufacturer.sellBike(bikeModel)
                self.inventory.append(bike)
                if(bike.bikeModel in self.dicInventory.keys()):
                    self.dicInventory[bike.bikeModel] += number
                else:
                    self.dicInventory[bike.bikeModel] = number
            else:
                print("Invalid BikeModels")
    
    def queryCost(self, bikeModel):
        bike = [item for item in self.inventory if item.bikeModel == bikeModel].pop()
        if(bike):
            return bike.cost
        else:
            return None
            
    def offerList(self, cost):
        bikes = {item for item in self.dicInventory if self.queryCost(item) <= cost and self.dicInventory[item] >= 1}
        if(bikes):
            return bikes
        else:
            return None
        
class Customers():
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bikes = []
        
    def Buy(self, bikeModel, bikeShop):
        if(self.money >= bikeShop.queryCost(bikeModel)):
            bikeBought = bikeShop.sellBike(bikeModel)
            if(bikeBought is not None):
                self.bikes.append(bikeBought)
                self.money -= bikeBought.cost
            else:
                print("{} Fail in bought action".format(self.name))
        else:
            print("{} should get more money".format(self.name))
            

class BikeComponent():
    def __init__(self, cost, weight):
        self.cost = cost
        self.weight = weight

class Wheel(BikeComponent):
    def __init__(self, model, weight, cost):
        super.__init__(cost)
        if(isinstance(model, WheelMode)):
            self.model = model
        else:
            print("Invalid model")
        
class Frame(BikeComponent):
    def __init__(self, material, weight, cost):
        super.__init__(cost)
        if(isinstance(material, FrameMaterial)):
            self.material = material
        else:
            print("Invalid material")
        
class Manufacturer():
    def __init__(self, name, bikeModels, percentage):
        if(len(bikeModels) == 3):
            self.bikeModels = bikeModels
        else:
            print("Invalid Models")
        self.name = name
        self.percentage = percentage
        
    def sellBike(self, bikeModel):
        if(isinstance(bikeModel, BikeModels)):
            bikeTobeSold = Bicycle(bikeModel, bikeModel, self.name)
            bikeTobeSold.cost = bikeTobeSold.cost * (1 + self.percentage)
        else:
            print("Invalid Models")
        return bikeTobeSold
                
        
        