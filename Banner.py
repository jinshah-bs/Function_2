def banner(text='', setScreenWidth = 60):
    if len(text)-4 > setScreenWidth:
        print("the text entered '{}' is long enough to print".format(text))
    elif text == '*':
        print(text * setScreenWidth)
    else:
        centered_text = text.center(setScreenWidth-4)
        print(f"**{centered_text}**")

banner('*',80)
banner('Today we had a good session on python',80)
banner('We did banner',80)
banner(setScreenWidth=80)
banner('today is our 11th day of class',80)
banner('*',80)






# print("*******************************************")
# print("**            How is going               **")
# print("**      my python class is going well    **")
# print("*******************************************")