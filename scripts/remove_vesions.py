with open( "../requirements.txt", 'r' ) as file:
      lines = file.readlines()

# Django==4.9.1 --> "Django", "4.9.1" --> we only take Django and add a "\n" newline character
lines = [ line.split( "==" )[0] + '\n' for line in lines ]

print(lines)

with open( "../requirements.txt", 'w' ) as file:
      file.writelines( lines )
