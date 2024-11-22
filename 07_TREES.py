



















# # Problem : As a senior backend engineer at jovian, you are tasked with developing a fast in memory data structure to manage profile information(username, name and email) for 100 million users. IT showuld allow the following operation  to be performed efficiently
# # 1. Inset the profile information  for a new user
# # 2. find the profile information of a user, given their username
# # 3. update the profile information for a user , given their username
# # 4. list all the user of the platform , sorted by username
# # You can assume that the usernames are unique



# # solving: we need to create a data structure which can store 100 million record and perform insertion , search, update, and list operations efficiently


# class User:
#     def __init__(self, username, name, email):
#         self.username = username
#         self.name = name
#         self.email = email
#     def __repr__(self):
#         return f"Username :{self.username}, name :{self.name}, email : {self.email}"
    
#     def __str__(self):
#         return self.__repr__()
    


# class UserDatabase:
#     def __init__(self):
#         self.users = []
#     def insert(self, User):
#         i = 0
#         while i<len(self.users):
#             if User.username < self.users[i].username:
#                 break
#             i = i + 1
#         self.users.insert(i, User)
        
#     def find(self, username):
#         for user in self.users
#     def update(self, user):
#         pass
#     def list_all(self):
#         pass




# obj = UserDatabase()

# sourov = User('sourov', 'sourov Talukder', 'sourov@gamil.com')
# abir = User('Abir', 'Abir Talukder', 'Abir@gamil.com' )
# jeny = User('Jeny', 'jeny Akter', 'Jeny@gmail.com')
# delwar = User('Delwar', 'Delwar Hossain', 'Delwar@gmail.com')

# users = [sourov, abir, jeny, delwar]

