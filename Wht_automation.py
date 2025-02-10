import pyodbc
import pywhatkit
import datetime

# Database connection
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=AVT1;'
    'DATABASE=WhatsAppAutomation;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Step 1: Fetch pending messages
cursor.execute("SELECT MessageID, PhoneNumber, MessageText, ScheduledTime FROM Messages WHERE Status = 'Pending'")
messages = cursor.fetchall()

# Step 2: Process and send messages
current_time = datetime.datetime.now()

for msg in messages:
    message_id, phone, text, schedule_time = msg
    
    # Convert database time to datetime object
    if isinstance(schedule_time, str):
        schedule_time = datetime.datetime.strptime(schedule_time, "%Y-%m-%d %H:%M:%S")

    # Check if it's time to send the message
    if schedule_time <= current_time:
        try:
            print(f"Sending message to {phone}: {text}")
            pywhatkit.sendwhatmsg_instantly(phone, text, 15, True, 5)  # Send instantly, close tab after 5s

            # Step 3: Update message status to 'Sent'
            cursor.execute("UPDATE Messages SET Status = 'Sent' WHERE MessageID = ?", message_id)
            conn.commit()
            print(f"Message {message_id} sent successfully!")

        except Exception as e:
            print(f"Failed to send message {message_id}: {e}")

# Close database connection
conn.close()