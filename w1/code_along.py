print("\nPlease enter the following information:")
print()

first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email: ")
phone = input("Phone number: ")
job_title = input("Job title: ")
id_badge = input("Id badge: ")

print("\nThe id card is:")
print("----------------------------------------")

print(f"{last_name.upper()}, {first_name}")
print(f"{job_title.title()}")
print(f"ID: {id_badge}")
print(f"{email.lower()}")
print(f"{phone}")


print("----------------------------------------")