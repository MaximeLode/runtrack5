def decaler_message(message, decalage):
  message_decale = ""
  for caractere in message:
    ascii_code = ord(caractere)
    if caractere.isalpha():
      if caractere.isupper():
        ascii_code = (ascii_code - 65 + decalage) % 26 + 65
      else:
        ascii_code = (ascii_code - 97 + decalage) % 26 + 97
    message_decale += chr(ascii_code)
  print(message_decale)
decaler_message("Bonjour",26)