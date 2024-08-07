'''default:0
black:30
red:31
green:32
yellow:33
blue:34
purple:35
cyan:36
white:37'''

# print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")
# print("\033[30m","warning", "\033[31m", "\nwarning","\033[32m", "\nwarning","\033[33m", "\nwarning","\033[34m", "\nwarning","\033[35m", "\nwarning","\033[36m", "\nwarning","\033[37m", "\nwarning")


'''
"\033[31m": This is an escape sequence used to change the color of the text in the terminal. \033 is the escape character, [ starts the color code, 31 is the code for red, and m ends the code. When printed, it tells the terminal to switch the text color to red.
"\033[0m": This is another escape sequence used to reset the text color back to the terminal's default. \033 is the escape character, [ starts the reset code, 0 is the code for resetting all attributes, and m ends the code. When printed, it tells the terminal to switch back to the default text color.
'''
