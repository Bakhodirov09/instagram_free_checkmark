def find_id_handler(message, users: dict, random_number: int, chat_id):
    if chat_id == 6606094329 and message.text == "1258":
        users["5769"]["score"] -= 1
        users["1258"]["score"] += 1
        return f""" 
Succesfully Gave 1 Score To
Name: {users['1258']['full_name']} 
ID: {users[message.text]["random_id"]}      
"""
    elif chat_id != 6606094329:
        if message.text in users.keys():
            users[random_number]["score"] -= 1
            users[message.text]["score"] += 1
            text1 = f"""
✅ Succefully Gaved
Name: {users[message.text]["full_name"]}
ID: {users[message.text]["random_id"]}
"""
            return text1
        else:
            text2 = "❌ Your ID Not Found!"
            return text2
    elif chat_id == 6606094329 and message.text != "1258":
        return "❌ Your ID Not Found!"

    elif chat_id == 5968397844 and message.text == "1258":
        users["5455"]["score"] -= 1
        users["1258"]["score"] += 1
        text3 = f"""
✅ Succefully Gaved
Name: {users[message.text]["full_name"]}
ID: {users[message.text]["random_id"]}
"""
        return text3