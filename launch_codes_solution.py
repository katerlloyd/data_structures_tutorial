import random

launch_codes = ["45923", "12281", "70024", "34975", "20912", "54557", "71233", "62841"]

# Finds the most recent even launch code.
def determine_correct_launch_code(launch_codes):
  for code in reversed(launch_codes):
    if int(code) % 2 == 0:
      return code

print("Find the right code using the commands below.")
print("1. Push   - select and add random code")
print("2. Pop    - select and remove code")
print("3. Launch - use selected code")
print("4. Give up for now")

code = "11111"
command = input("> ")

while command != "4":
  correct_code = determine_correct_launch_code(launch_codes)
  # Adds a random launch code to the stack.
  if command == "1":
    code = str(random.randint(10000, 99999))
    launch_codes.append(code)
    print("Random launch code added")
    print(f"Selected launch code: {code}")
    correct_code = determine_correct_launch_code(launch_codes)
    command = input("> ")
  # Removes and selects the last launch code from the stack.
  elif command == "2":
    code = launch_codes.pop()
    print(f"Selected launch code: {code}")
    command = input("> ")
  # Checks if the launch codes match.
  elif command == "3":
    if code == correct_code:
      print("Launch successful!")
    else:
      print("Aaaaand now we're dead!")
    break