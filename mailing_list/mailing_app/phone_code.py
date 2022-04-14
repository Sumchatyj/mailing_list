def get_phone_code(client):
    phone = list(str(client.phone))
    phone_code = phone[1] + phone[2] + phone[3]
    client.phone_code = int(phone_code)
