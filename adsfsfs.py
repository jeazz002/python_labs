def xor_encrypt(text, key):
    """
    Функция для шифрования текста с помощью XOR.
    Возвращает зашифрованные данные в hex-формате.
    """
    # Кодирование: преобразуем текст и ключ в байты
    text_bytes = text.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    # Криптография: применяем XOR к каждому байту
    encrypted_bytes = bytearray()
    for i in range(len(text_bytes)):
        encrypted_byte = text_bytes[i] ^ key_bytes[i % len(key_bytes)]
        encrypted_bytes.append(encrypted_byte)
    
    # Возвращаем в виде hex-строки
    return encrypted_bytes.hex()

def xor_decrypt(hex_string, key):
    """
    Функция для дешифрования текста из hex-формата с помощью XOR.
    """
    # Преобразуем hex-строку обратно в байты
    encrypted_bytes = bytes.fromhex(hex_string)
    key_bytes = key.encode('utf-8')
    
    # Применяем XOR для дешифрования
    decrypted_bytes = bytearray()
    for i in range(len(encrypted_bytes)):
        decrypted_byte = encrypted_bytes[i] ^ key_bytes[i % len(key_bytes)]
        decrypted_bytes.append(decrypted_byte)
    
    # Декодируем байты обратно в текст
    return decrypted_bytes.decode('utf-8')

# --- ИСПОЛЬЗОВАНИЕ ---
secret_message = "Привет123"
secret_key = "key"

print("1. Исходное сообщение:", secret_message)

# Шифруем
encrypted_hex = xor_encrypt(secret_message, secret_key)
print("2. Сообщение после кодирования и шифрования (в hex):", encrypted_hex)

# Дешифруем
decrypted_text = xor_decrypt(encrypted_hex, secret_key)
print("3. Сообщение после дешифрования и декодирования:", decrypted_text)

# Проверка
print("4. Совпадает ли исходное и дешифрованное сообщение?", secret_message == decrypted_text)