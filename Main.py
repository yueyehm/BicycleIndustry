from Bicycle import *
if __name__ == "__main__":
    # Initial Manufacturer
    Giant = Manufacturer("Giant", (BikeModels.A, BikeModels.D, BikeModels.E), 0.15)
    Merinda = Manufacturer("Merinda", (BikeModels.B, BikeModels.C, BikeModels.F), 0.2)

    # Initial Customers
    John = Customers("John", 200)
    Peter = Customers("Peter", 500)
    Nancy = Customers("Nancy", 1000)

    # Initial BikeShop
    BikeClubShop = BikeShops("BikeClubShop")
    BikeClubShop.purchaseBike(Giant, BikeModels.A, 3)
    BikeClubShop.purchaseBike(Merinda, BikeModels.B, 4)
    BikeClubShop.purchaseBike(Merinda, BikeModels.C, 3)
    BikeClubShop.purchaseBike(Giant, BikeModels.D, 6)
    BikeClubShop.purchaseBike(Giant, BikeModels.E, 3)
    BikeClubShop.purchaseBike(Merinda, BikeModels.F, 1)

    # Offer List
    print("Output Offer List");
    print(John.name, BikeClubShop.offerList(John.money))
    print(Peter.name, BikeClubShop.offerList(Peter.money))
    print(Nancy.name, BikeClubShop.offerList(Nancy.money))

    # Print the inventory of Bike Shop
    print("Output Inventory")
    print(BikeClubShop.dicInventory)

    # Customers buy bikes
    John.Buy(BikeModels.A, BikeClubShop)
    Peter.Buy(BikeModels.A, BikeClubShop)
    Nancy.Buy(BikeModels.F, BikeClubShop)

    # Print the inventory of Bike Shop
    print("Output Inventory Again")
    print(BikeClubShop.dicInventory)

    # Print the profit of Bike Shop
    print("Bike Profit: {}".format(BikeClubShop.profit))
    
    # Re-buy
    Nancy.money = 2000
    Nancy.Buy(BikeModels.F, BikeClubShop)
    print(Nancy.bikes)

    # Print the inventory of Bike Shop
    print("Output Inventory Again")
    print(BikeClubShop.dicInventory)
