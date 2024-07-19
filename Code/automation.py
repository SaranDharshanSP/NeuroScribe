import requests

#esp32_ip = "192.168.31.177"  # Replace with the IP address of your ESP32
esp32_ip  = "192.168.102.237"
alphabet = 0
while True:
    url = f"http://{esp32_ip}/send_message?play={alphabet}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Alpabet sent successfully")
        break
    else:
        print(f"Error: {response.text}")
        print("Sending again")
        

print("Message sending completed")
