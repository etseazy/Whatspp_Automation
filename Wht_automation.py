import pywhatkit as kit

# Parameters:
# 1. Phone number with country code
# 2. Message to send
# 3. Hour (24-hour format)
# 4. Minute

phone_number = input("Enter the recipient's phone number (with country code): ")
message = input("Enter the message to send: ")
hour = int(input("Enter the hour to send the message (24-hour format): "))
minute = int(input("Enter the minute to send the message: "))

try:
    kit.sendwhatmsg(phone_number, message, hour, minute)
    print("Message scheduled successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
