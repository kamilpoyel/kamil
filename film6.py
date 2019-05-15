produkty= ["mleko","ser","parówki", "mleko"]
prod= ["keczup", "balnal"]
produkty.extend(prod)
x= produkty.count("mleko")
produkty.remove("ser")
print(x)
print(produkty)
print(type(produkty))

produkty= ("mleko","ser","parówki", "mleko")

print(produkty)
print(type(produkty))

person={"wiek":20, "imie": "ania","azwisko":"Kowalska"}

print(person.get["wiek"])