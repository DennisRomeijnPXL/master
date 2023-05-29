file = open ('devices.txt', 'a')
while True:
  newITem = input ('Enter Device name: ')
  if newItem == exit:
    print('That's it')
    break
  file.write(newItem + '\n')
file.close
