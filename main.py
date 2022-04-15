from VividHues import Clr


input_email = input(f"{Clr.LIME}Please enter your email\n\t--> {Clr.RS}")
input_email = input_email.strip()

while len(input_email) <= 6:  # small email example _@_.__
  Clr.delPrevLine(2)
  input_email = input(f"{Clr.LIME}Please enter your email\n\t--> {Clr.RS}")
  input_email = input_email.strip()

at_location = input_email.index("@")
username    = input_email[:at_location]
domain      = input_email[at_location + 1:]

print(f"{Clr.RED}Email:\t\t{input_email}")
print(f"{Clr.PINK}Username:\t{username}")
print(f"{Clr.BLUE}Domain:\t\t{' ' * len(username) + ' '}{domain}")
print(Clr.RS, end="")
