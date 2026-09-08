# Write greet(name, time_of_day="morning") using a default parameter, and call it two different ways.
def greet(name, time_of_day="morning") :
    return f"Hello, I am {name} and its {time_of_day}."

print(greet(name="Javeria"))
print(greet(name="Maha",time_of_day="Evening"))