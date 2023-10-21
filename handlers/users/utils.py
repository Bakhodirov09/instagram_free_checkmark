import sqlite3
import logging
 
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
 
 
def get_user(chat_id: int = None, random_number_id: str = None):
    if chat_id:
        return cursor.execute(f"SELECT * FROM users WHERE chat_id='{chat_id}'").fetchone()
    if random_number_id:
        return cursor.execute(f"SELECT score FROM users WHERE random_number_id='{random_number_id}'").fetchone()
    return False
 
 
def find_id_handler(message, users: dict, random_number: int, chat_id):
    if chat_id in [6606094329, 5968397844, 5097853234]:
        if message.text == "1258":
            userr = get_user(random_number_id=message.text)
            userr1 = get_user(chat_id=chat_id)
            cursor.execute(f"UPDATE users SET score={userr[-1] + 1} WHERE random_number_id='1258'")
            cursor.execute(f"UPDATE users SET score={userr1[-1] - 1} WHERE chat_id={chat_id}")
            conn.commit()
            return f"""
                    Succesfully Gave 1 Score To
                    Name: {users['1258']['full_name']}
                    ID: {users[message.text]["random_id"]}
                    """
        return "❌ Your ID Not Found!"
    
    
    else:
        if message.text in users.keys():
            userr = get_user(random_number_id=message.text)
            userr1 = get_user(chat_id=chat_id)
            logging.error(userr)
            logging.error(userr1)
            cursor.execute(f"UPDATE users SET score={userr[-1] + 1} WHERE random_number_id='1258'")
            cursor.execute(f"UPDATE users SET score={userr1[-1] - 1} WHERE chat_id={chat_id}")
            conn.commit()
            text1 = f"""
                    ✅ Succefully Gaved
                    Name: {users[message.text]["full_name"]}
                    ID: {users[message.text]["random_id"]}
                    """
            return text1
        text2 = "❌ Your ID Not Found!"
        return text2