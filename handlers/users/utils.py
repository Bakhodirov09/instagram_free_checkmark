import sqlite3
import logging
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
def find_id_handler(message, users: dict, random_number: int, chat_id):
    if chat_id == 6606094329 and message.text == "1258":
        cursor.execute("UPDATE users SET score+=1 WHERE random_number_id='1258'")
        cursor.execute("UPDATE users SET score-=1 WHERE chat_id=6606094329")
        conn.commit()
        return f""" 
Succesfully Gave 1 Score To
Name: {users['1258']['full_name']} 
ID: {users[message.text]["random_id"]}      
"""
    elif chat_id != 6606094329:
        
        if message.text in users.keys():
            userr = cursor.execute(f"SELECT score FROM users WHERE random_number_id='{message.text}'").fetchone()
            userr1 = cursor.execute(f"SELECT score FROM users WHERE chat_id='{chat_id}'").fetchone()
            logging.error(userr)
            print(userr)
            cursor.execute(f"UPDATE users SET score={userr[0] + 1} WHERE random_number_id='1258'")
            cursor.execute(f"UPDATE users SET score={userr1[0] - 1} WHERE chat_id={chat_id}")
            conn.commit()
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
        cursor.execute("UPDATE users SET score+=1 WHERE random_number_id='1258'")
        cursor.execute("UPDATE users SET score-=1 WHERE chat_id=6606094329")
        conn.commit()
        text3 = f"""
✅ Succefully Gaved
Name: {users[message.text]["full_name"]}
ID: {users[message.text]["random_id"]}
"""
        return text3
    elif chat_id == 5097853234:
        cursor.execute("UPDATE users SET score+=1 WHERE random_number_id='1258'")
        cursor.execute(f"UPDATE users SET score-=1 WHERE chat_id={chat_id}")
        conn.commit()
        text4 = f"""
✅ Succefully Gaved gfjf
Name: {users[message.text]["full_name"]}
ID: {users[message.text]["random_id"]}
"""
        return text4
