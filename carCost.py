class CarCost(object):
    def __init__(self, costOfCar, milesPerYear, totalYears, carMpg, costPerGallon, insurancePerYear):
        self.costOfCar = costOfCar
        self.milesPerYear = milesPerYear
        self.totalYears = totalYears
        self.carMpg = carMpg
        self.costPerGallon = costPerGallon
        self.insurancePerYear = insurancePerYear

    def calculateTotalMiles(self):
        return self.totalYears * self.milesPerYear
    
    def calculateLifetimeGas(self):
        return (1/self.carMpg) * self.calculateTotalMiles() * self.costPerGallon 

    def calculateLifetimeInsurance(self):
        return self.insurancePerYear * self.totalYears

    def calculateTotalCost(self):
        return self.costOfCar + self.calculateLifetimeGas() + self.calculateLifetimeInsurance()

    def calculateTotalCostPerMile(self):
        return self.calculateTotalCost() / self.calculateTotalMiles()

    

def main():
    ourHonda = CarCost(25000, 10000, 20, 30, 3, 2000)
    totalCost = ourHonda.calculateTotalCost()
    totalCostPerMile = ourHonda.calculateTotalCostPerMile()

    print("total cost:", totalCost)
    print("total cost per mile:", totalCostPerMile)

main()
