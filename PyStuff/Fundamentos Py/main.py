from user import User

""" user = User("Alice", 30, "alice@example.com")

for x in range (1,11):
  print(f"Hello, {user.name}! This is message number {x}.") """


running = 1
user_list = []

while running!= 0:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    user = User(name, age, email)
    user_list.append(user)
    try:
        cont = input("Do you want to add another user? (yes/no): ")
        if cont.lower() != 'yes':
            running = 0
    except:
        print("Invalid input.")
print("\nUser Information:")
for user in user_list:
    print(user.get_info())