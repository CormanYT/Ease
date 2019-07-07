import copy
class UnaccessibleError(Exception):
    pass
class AccessError(Exception):
    pass
class DatabaseError(Exception):
    pass
class Database:
    class User:
        def __init__(self, name, password, database, **kwargs):
            self.username = name
            try:
                self.perms = kwargs["permissions"]
            except:
                self.perms = []
            self.database = database
            self.password = password
        def __str__(self):
            return "User " + self.username
        def dataCheck(self, user):
            if not self.database == user.database:
                raise DatabaseError("Cannot perform actions on separate databases.")
        def owner(self, user):
            self.dataCheck(user)
            if self.hasPermission("owner"):
                self.perms.remove("owner")
                user.perms.append("owner")
                self.database.owner = user
            else: raise PermissionError("No permissions.")
        def permissions(self):
            return self.perms
        def addPermission(self, user, perm):
            self.dataCheck(user)
            if self.hasPermission("locked"):
                raise AccessError("Locked users cannot perform actions.")
            if self.hasPermission("add_permission"):
                user.perms.append(perm)
            else:  raise PermissionError("No permissions.")
        def removePermission(self, user, perm):
            self.dataCheck(user)
            badperms = ["owner", "*"]
            if self.hasPermission("locked"):
                raise AccessError("Locked users cannot perform actions.")
            if self.hasPermission("remove_permission") and perm not in badperms:
                if user.hasPermission(perm):
                    user.perms.remove(perm)
            elif perm is "*" and self.hasPermission("owner"):
                if user.hasPermission(perm):
                    user.perms.remove(perm)
            else:
                raise PermissionError("Cannot take away 'owner' permission.")
            
        def hasPermission(self, perm):
            badperms = ["owner", "locked"]
            if not perm in badperms:
                return "*" in self.perms or perm in self.perms
            else:
                return perm in self.perms
        def register(self, name, password):
            if self.hasPermission("locked"):
                raise AccessError("Locked users cannot perform actions.")
            if self.hasPermission("register"):
                self.database.users.append(Database.User(name, password, self.database))
        def remove(self, user):
            self.dataCheck(user)
            if self.hasPermission("locked"):
                raise AccessError("Locked users cannot perform actions.")
            if user.hasPermission("safe") or user.hasPermission("owner"):
                raise PermissionError("Not enough permissions to delete this user's account.")
            if self.hasPermission("remove"):
                self.database.users.remove(user)
            else:raise PermissionError("No permissions.")
        def lock(self, user):
            self.dataCheck(user)
            if self.hasPermission("locked"):
                raise AccessError("Locked users cannot perform actions.")
            if self.hasPermission("lock"):
                self.addPermission(user, "locked")
        def unlock(self, user):
            self.dataCheck(user)
            if self.hasPermission("locked"):
                raise AccessError("Locked users cannot perform actions.")
            if self.hasPermission("unlock"):
                self.removePermission(user, "locked")
        def upload(self=None, name=None, item=None, *args):
            if self.hasPermission("locked"):
                raise AccessError("Locked users cannot perform actions.")
            try:
                user = args[0]
                try:
                    user = list(user[:])
                except:
                    user = args[0]
            except:
                user = [self, ]
            if self.hasPermission("upload"):
                for itemer in self.database.data:
                    if itemer[0] == name:
                        raise ValueError("Item {} already exists in this database.".format(name))
                self.database.data.append((name, item, user))
            else: raise PermissionError("No permissions.")
        def get(self, name):
            if self.hasPermission("locked"):
                raise AccessError("Locked users cannot perform actions.")
            for item in self.database.data:
                try:
                    spasjdf = item[2][:]
                    if item[0] == name and self in item[2]:
                        return item[1]
                    elif item[0] == name and not self in item[2]:
                         raise PermissionError("No permissions to access this item.")
                except:
                    if item[2] == "public":
                        return item[1]
                    else:
                        raise PermissionError("No permissions to access this item.")
            raise ValueError("No item {}".format(item[0]))
        def download(self, name):
            if self.hasPermission("locked"):
                raise AccessError("Locked users cannot perform actions.")
            return copy.deepcopy(self.get(name))
        def items(self):
            returns = {}
            for item in self.database.data:
                if self in item[2] or item[2] == "public":
                    returns.update({item[0]: item[1]})
            return returns
                
        def __getitem__(self, name):
            return self.get(name)
    def __init__(self, ownerName, ownerPass):
        self.data = []
        owner = Database.User(ownerName, ownerPass, self, permissions=["owner", "*"])
        self.users = [owner]
        self.owner = owner
    def usernames(self):
        lister = []
        for item in self.users:
            lister.append(item.username)
        return tuple(lister)
    def login(self, name, password):
        user = None
        for item in self.users:
            if item.username == name:
                user = item
                break
        if user == None:
            return ValueError("Invalid username.")
        if user.password == password:
            return user
        else:
            return ValueError("Invalid password.")
        
data = Database("Corman", "Enderman5675")
owner = data.login("Corman", "Enderman5675")
import random
from generate import generate
for x in range(100):
    owner.register(generate(str, 5), "Bot585")
this = data.usernames()
for item in data.users:
    for x in range(random.randint(1, 10)):
        owner.upload(generate(str, 5), generate(random.choice([str, int, bool, list]), 5), [item, owner])
for item in data.users:
    print(item.username)
    print()
    print(item.items())
    print()
