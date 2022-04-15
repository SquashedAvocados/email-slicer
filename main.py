from VividHues import Clr


print(Clr.rainbow("""\
 _______  ___  ___       ___       __   __    
|   ____||   \/   |     /   \     |  | |  |   
|  |__   |  \  /  |    /  ^  \    |  | |  |   
|   __|  |  |\/|  |   /  /_\  \   |  | |  |   
|  |____ |  |  |  |  /  _____  \  |  | |  `--.
|_______||__|  |__| /__/     \__\ |__| |_____|
"""))
print(Clr.rainbow("""\
    ______  __     __    ____  _______  ______      
   /      ||  |   |  |  /    ||   ____||   _  \     
  |   (---`|  |   |  | |  ,--'|  |__   |  |_)  |    
   \   \   |  |   |  | |  |   |   __|  |      /     
.---)   |  |  `--.|  | |  `--.|  |____ |  |\  \--.
|______/   |_____||__|  \____||_______||__| `.___|
"""))

input_email = input(f"{Clr.LIME}Please enter your email\n\t--> {Clr.RS}")
input_email = input_email.strip()

while len(input_email) <= 6:  # small email example _@_.__
  Clr.delPrevLine(2)
  input_email = input(f"{Clr.LIME}Please enter your email\n\t--> {Clr.RS}")
  input_email = input_email.strip()

Clr.delPrevLine(2)

at_location = input_email.index("@")
username    = input_email[:at_location]
domain      = input_email[at_location + 1:]

box_line    = '•-' + '-' * 6 + 2 * ('-' * 4) + '-' * len(input_email) + '-•'
#          "| "    + "Email:"+ 2 * "\t"      + len(email)             + " |"
print(f"""
{box_line}
| {Clr.RED}Email:\t\t{input_email}{Clr.RS} |
| {Clr.PINK}Username:\t\t{username}{Clr.RS}{' ' + ' ' * len(domain)} |
| {Clr.BLUE}Domain:\t\t{' ' * len(username) + ' '}{domain}{Clr.RS} |
{box_line}{Clr.RS}\
""")
