from abc import ABC, abstractmethod

class Product:
    def __init__(self):
        self.attribute1 = None
        self.attribute2 = None
        self.attribute3 = None
        self.attribute4 = None

    def __str__(self):
        return f"This product has {self.attribute1}, {self.attribute2}, {self.attribute3}, {self.attribute4}"

class ProductBuilder(ABC):
    @abstractmethod
    def set_attribute1(self, att1):
        pass
    @abstractmethod
    def set_attribute2(self, att2):
        pass
    @abstractmethod
    def set_attribute3(self, att3):
        pass
    @abstractmethod
    def set_attribute4(self, att4):
        pass
    @abstractmethod
    def build(self):
        pass

class CustomProductBuilder(ProductBuilder):
    def __init__(self):
        self.product = Product()

    def set_attribute1(self, att1):
        self.product.attribute1 = att1
        return self

    def set_attribute2(self, att2):
        self.product.attribute2 = att2
        return self

    def set_attribute3(self, att3):
        self.product.attribute3 = att3
        return self

    def set_attribute4(self, att4):
        self.product.attribute4 = att4
        return self

    def build(self):
        built_product = self.product
        self.product = Product()
        return built_product

class Director:
    _instance = None
    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, builder: ProductBuilder):
        self.builder = builder

    #Predefined products
    def buildProductA(self):
        return(
            self.builder
            .set_attribute1("att1_A")
            .set_attribute2("att2_A")
            .set_attribute3("att3_A")
            .set_attribute4("att4_A")
            .build()
        )

    def buildProductB(self):
        return(
            self.builder
            .set_attribute1("att1_B")
            .set_attribute2("att2_B")
            .set_attribute3("att3_B")
            .set_attribute4("att4_B")
            .build()
        )
    #Custom Products
    def buildCustomProduct(self,att1, att2, att3, att4):
        return(
            self.builder
            .set_attribute1(att1)
            .set_attribute2(att2)
            .set_attribute3(att3)
            .set_attribute4(att4)
            .build()
        )

sample_builder = CustomProductBuilder()
sample_director = Director(sample_builder)
sample_director2 = Director(sample_builder)
print(sample_director == sample_director2)

sample_productA = sample_director.buildProductA()
sample_productB = sample_director.buildProductB()
sample_custom_product = sample_director.buildCustomProduct("att1_cus", "att2_cus", "att3_cus", "att4_cus")

print(sample_productA)
print(sample_productB)
print(sample_custom_product)