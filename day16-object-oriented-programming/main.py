from turtle import Turtle, Screen

# Create object from blueprint

#siri = Turtle()
#print(siri)
#siri.shape("turtle")
#siri.color("DarkSeaGreen")
#siri.forward(100)

#my_screen = Screen()
#print(my_screen.canvheight)

# Tap into screen objects methods (functions)

#my_screen.exitonclick() # Allow program to continue running until click on screen

from prettytable import PrettyTable

# Create object from the class
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]    # Use the objects methods
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

table.align["Pokemon Name"] = "l"
table.align["Type"] = "c"

print(table)


