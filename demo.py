from support_agent import support_agent


print("===================================")
print("      AmazonHelp AI Support Agent")
print("===================================")

print("\nType a customer message.")
print("Type 'exit' to close the agent.\n")


while True:
    message = input("Customer: ")

    if message.lower() == "exit":
        print("\nThank you for contacting AmazonHelp.")
        break

    if not message.strip():
        print("Please enter a customer message.")
        continue

    intent, confidence, response = support_agent(message)

    print("\nDetected Intent:", intent)
    print("Confidence:", round(confidence, 2))
    print("Support Response:", response)
    print()