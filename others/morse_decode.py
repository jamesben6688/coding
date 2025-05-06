MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}


def decode_morse_code(morse_code):
    # 摩斯码分隔符
    char_split = 'xxx'  # 表示字符分隔
    word_split = 'xxxxx'  # 表示单词分隔

    # 将摩斯码根据单词分隔符拆分成单词
    words = morse_code.split(word_split)

    decoded_message = []

    for word in words:
        # 将每个单词根据字符分隔符拆分成字符
        characters = word.split(char_split)

        decoded_word = ''.join(MORSE_CODE_DICT.get(char, '') for char in characters)
        decoded_message.append(decoded_word)

    # 返回解码后的消息，单词之间用空格分隔
    return ' '.join(decoded_message)


# 示例摩斯码
morse_code = '.-.xxx-..xxxxx..-'

# 解码
decoded_message = decode_morse_code(morse_code)
print(decoded_message)
