def print_kwargs(name,**kwargs):
    print("Printing keyword arguments:")
    print(f"Name :{name}")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs("Rama", age=30, country="India")
print_kwargs(age=30, country="India", name="Rama")

