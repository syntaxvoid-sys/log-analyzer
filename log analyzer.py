with open("logs.txt", "r") as logs:
 count = 0
 wanted_action = input("Enter wanted action(LOGIN , LOGOUT , FALIED LOGIN , PASSWORD_CHANGE) :").upper().strip()
 wanted_user = input("Enter wanted user(if no user wanted enter: no_user): ").lower()
 for log in logs:
  part = log.split(" | ")
  if part[1] != wanted_action:
   continue
  if wanted_user == "no_user":
   count += 1
   print("Date:" , part[0])
   print("Action:" , part[1])
   print("User:" , part[2])
   continue
  elif part[2] != wanted_user:
   continue
  count += 1
  print("Date:" , part[0])
  print("Action:" , part[1])
  print("User:" , part[2])
 if count == 0:
  print("Nothing matched with the action: " , wanted_action)
print("total" , wanted_action , "analyzed:" , count)