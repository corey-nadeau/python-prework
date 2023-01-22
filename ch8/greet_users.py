def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

potatoe = ['hannah','ty','margot']
greet_users(potatoe)