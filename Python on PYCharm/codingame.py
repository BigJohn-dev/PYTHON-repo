s=input()
print(f"{len([*filter(str.isalpha,s)])/len([*filter(str.isdigit,s)]):.0%}")