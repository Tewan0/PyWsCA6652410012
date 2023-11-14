def get_sentence() :
    sentence = input("ป้อนข้อความ : ")
    return sentence
def show_sentence(sentence) :
    print(sentence)

def count_words(sentence) :
    words = sentence.split(" ")
    return len(words)


def check_duplicate(words) :
    words_set = set(words)
    return len(words) != len(words_set)

def show_duplicate(words) :
    duplicate_words = []
    for word in words :
        if word in duplicate_words :
            continue
        duplicate_words.append(word)
    print(f'มีคำที่ซํ้ารวมกัน {len(duplicate_words)} คำ')
    for word in duplicate_words :
        count = 0
        for w in words :
            if word == w :
                count += 1 
        print(f'คำว่า {word} ซํ้ากัน {count} ครั้ง')

sentence = get_sentence()
show_sentence(sentence)
print(f'มีคำรวมทั้งหมด {count_words(sentence)} คำ')
if check_duplicate(sentence.split(" ")) :
    show_duplicate(sentence.split(" "))

