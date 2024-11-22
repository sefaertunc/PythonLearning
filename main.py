from Utilities import general_supplier

supplier = general_supplier.GeneralSupplier()
a = 0
while not a == 100:
	a = supplier.get_random_integer(1, 100)
	print(a)
