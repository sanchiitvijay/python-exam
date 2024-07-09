passwd = {'rahul': 'genius', 'kumar': 'smart', 'ankita': 'intelligent'}

print("All items in the dictionary:")
for key, value in passwd.items():
    print(f"{key}: {value}")

print("\nAll keys in the dictionary:")
for key in passwd.keys():
    print(key)

print("\nAll values in the dictionary:")
for value in passwd.values():
    print(value)

user = 'rahul'
print(f"\nPassword of '{user}': {passwd[user]}")

user = 'ankita'
passwd[user] = 'brilliant'
print(f"\nChanged password of '{user}' to '{passwd[user]}'")
