from main import letter

message = letter("Xandrix", "Jill")
message.addLine("I am sorry for eating your triple cheese burger.")
message.addLine("I hope you can forgive me.")
print(message.getText())