def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

potatoe = ['hannah']
greet_users(potatoe)