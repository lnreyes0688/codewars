def create_phone_number():
  num = []
  for i in range(10):
    n = int(input('Enter a one-digit number:'))
    num.append(n)
  return num

number = create_phone_number()

print(number[:3])








