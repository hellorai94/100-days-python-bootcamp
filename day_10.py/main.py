# Functions with Outputs

""" def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

format_name("raissa", "carneiro")
 """

# Functions with Outputs

""" def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    print(f"{formated_f_name} {formated_l_name}")

format_name("raISsa", "carnEirO")
 """

# Functions with Outputs

""" def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return(f"{formated_f_name} {formated_l_name}")

print(format_name("raISsa", "carnEirO"))

 """


# Functions with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result:{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), 
input("Whats is you last name?")))

