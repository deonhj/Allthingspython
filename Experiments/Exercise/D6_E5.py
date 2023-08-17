file = open('members.txt', 'r')
users = file.readlines()
file.close()
print(users)

user = input("specify a user to add:") + '\n'

users.append(user)
file = open('members.txt', 'w')
file.writelines(users)
file.close()