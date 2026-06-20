class Iphone:

    logo = "APPLE"

    def __init__(self,name,size):
        print("this run first")
        self.name = name
        self.size = size

    def calling(self,person):
        return (f"Calling {person}.....")
    
    def endCall(self,person):
        return (f"End Call With {person}")

    def colour(self):
        return (f"colour is {self.colour}")


iphone13 = Iphone("IPHONE 13",5.5)
iphone14 = Iphone("IPHONE 14",6.5)
# print(iphone13.name)
# print(iphone13.size)

# print(iphone13.calling("PAPA"))
# print(iphone13.endCall("PAPA"))

# print(iphone13.logo)
# print(iphone14.logo)


print(Iphone.calling(iphone13,"PAPA"))