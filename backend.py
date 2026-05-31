rules = {
    "a":"َ",
    "u": "ُ",
    "i": "ِ",
    "A": "ا",
    "I": "إ",
    "2": "ء",
    "b": "ب",
    "t": "ت",
    "th": "ث",
    "j": "ج",
    "7": "ح",
    "kh": "خ",
    "d": "د",
    "dh": "ذ",
    "r": "ر",
    "z": "ز",
    "s": "س",
    "sh": "ش",
    "9": "ص",
    "ddh": "ض",
    "6": "ط",
    "zh": "ظ",
    "3": "ع",
    "gh": "غ",
    "f": "ف",
    "q": "ق",
    "k": "ك",
    "l": "ل",
    "m": "م",
    "n": "ن",
    "h": "ه",
    "w": "و",
    "U": "و",
    "e": "ي",
    "y": "ي"
}

words = [
    # greetings
    "السلام", "عليكم", "ورحمة", "الله", "وبركاته",

    # religious phrases
    "بسم", "الحمد", "إن", "شاء", "ما", "أستغفر", "لا", "إله", "إلا", "أكبر",

    # basic responses
    "نعم", "لا", "أعرف", "رجاء", "المعذرة", "عفوا",

    # polite expressions
    "شكرا", "جزيلا", "من", "فضلك", "تفضل", "بعد", "إذنك", "جميل",

    # conversation
    "كيف", "حالك", "الحال", "أنا", "بخير", "اسمك", "اسمي",
    "تشرفنا", "أين", "متى", "لماذا",

    # verbs
    "ذهب", "جاء", "أكل", "شرب", "نام", "مشى", "قاد",
    "طبخ", "غسل", "فتح", "كتب", "لعب", "درس", "قرأ", "جلس",

    # food
    "خبز", "ماء", "طعام", "تفاح", "موز", "برتقال",
    "خيار", "طماطم", "بطاطا", "بصل", "ثوم",

    # everyday objects
    "كتاب", "قلم", "حاسوب", "هاتف", "بيت", "مدرسة", "جامعة",

    # numbers
    "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة",
    "ستة", "سبعة", "ثمانية", "تسعة", "عشرة",

    # colours
    "أحمر", "أخضر", "أزرق", "أسود", "أبيض", "أصفر",

    # places/transport
    "سيارة", "طريق", "شارع", "جسر", "محطة",

    # nature
    "شمس", "قمر", "سماء", "مطر", "ريح",

    # animals
    "كلب", "قطة", "أسد", "نمر", "فيل",

    # body
    "رأس", "يد", "عين", "قلب",

    # connectors
    "في", "من", "إلى", "على", "مع", "عن", "هذا", "ذلك", "هناك"
]

frequency = {
    # greetings
    "الله": 1000, "السلام": 950, "عليكم": 900, "ورحمة": 850, "وبركاته": 800,

    # religious phrases
    "الحمد": 950, "بسم": 900, "إن": 850, "شاء": 800, "ما": 900, "لا": 950,
    "إله": 850, "إلا": 900, "أكبر": 900, "أستغفر": 750,

    # basic responses
    "نعم": 850, "أعرف": 700, "رجاء": 800, "المعذرة": 750, "عفوا": 850,

    # polite expressions
    "شكرا": 900, "جزيلا": 750, "من": 950, "فضلك": 700, "تفضل": 700,
    "بعد": 800, "إذنك": 750,

    # conversation
    "كيف": 800, "حالك": 750, "الحال": 700, "أنا": 850, "بخير": 800,
    "اسمك": 700, "اسمي": 700, "تشرفنا": 700,
    "أين": 750, "متى": 700, "لماذا": 650,

    # verbs
    "ذهب": 700, "جاء": 700, "أكل": 750, "شرب": 750,
    "نام": 650, "مشى": 650, "قاد": 650,
    "طبخ": 650, "غسل": 650, "فتح": 700,
    "كتب": 900, "لعب": 800, "درس": 900, "قرأ": 750, "جلس": 700,

    # food
    "ماء": 900, "طعام": 800, "خبز": 850,
    "تفاح": 700, "موز": 700, "برتقال": 700,
    "خيار": 650, "طماطم": 650, "بطاطا": 700,
    "بصل": 700, "ثوم": 650,

    # everyday objects
    "كتاب": 1000, "قلم": 850, "حاسوب": 700, "هاتف": 800,
    "بيت": 950, "مدرسة": 900, "جامعة": 850,

    # numbers
    "واحد": 800, "اثنان": 750, "ثلاثة": 750, "أربعة": 750,
    "خمسة": 750, "ستة": 700, "سبعة": 700,
    "ثمانية": 700, "تسعة": 700, "عشرة": 750,

    # colours
    "أحمر": 650, "أخضر": 650, "أزرق": 650,
    "أسود": 650, "أبيض": 650, "أصفر": 650,

    # places/transport
    "سيارة": 800, "طريق": 850, "شارع": 800,
    "جسر": 700, "محطة": 750,

    # nature
    "شمس": 800, "قمر": 750, "سماء": 750,
    "مطر": 800, "ريح": 750,

    # animals
    "كلب": 700, "قطة": 750, "أسد": 700,
    "نمر": 650, "فيل": 650,

    # body
    "رأس": 800, "يد": 800, "عين": 800, "قلب": 850,

    # connectors
    "في": 950, "إلى": 900, "على": 900,
    "مع": 850, "عن": 800, "هذا": 900,
    "ذلك": 800, "هناك": 750
}

bigrams = {
    # greetings
    "السلام": {"عليكم": 1000},
    "عليكم": {"ورحمة": 900},
    "ورحمة": {"الله": 1000},
    "الله": {"وبركاته": 950, "أكبر": 900},

    # religious phrases
    "بسم": {"الله": 1000},
    "الحمد": {"الله": 1000},
    "إن": {"شاء": 800},
    "ما": {"شاء": 700},
    "شاء": {"الله": 1000},
    "لا": {"إله": 1000},
    "إله": {"إلا": 1000},
    "إلا": {"الله": 1000},
    "أستغفر": {"الله": 1000},

    # polite expressions
    "شكرا": {"جزيلا": 900},
    "من": {"فضلك": 800},
    "بعد": {"إذنك": 800},

    # conversation
    "كيف": {"حالك": 900},
    "أنا": {"بخير": 850},

    # verbs
    "أكل": {"طعام": 800},
    "شرب": {"ماء": 900},
    "قرأ": {"كتاب": 900},
    "كتب": {"كتاب": 850},
    "درس": {"كتاب": 850},

    # places/transport
    "أين": {"الطريق": 700},
    "في": {"البيت": 900, "السيارة": 700, "المحطة": 750},
    "على": {"الطريق": 700},
    "إلى": {"البيت": 700, "مدرسة": 800},

    # connectors
    "هذا": {"البيت": 800, "كتاب": 900},
    "ذلك": {"الطريق": 700}
}

def transliterate(text, rules):

    result = ""
    i = 0

    while i < len(text): # while there is an input:

        if text[i:i+3] in rules: # 3 char match check
            result += rules[text[i:i+3]] # 3 character (Arabic) letter detected
            i += 3 # 3 char jump (greedy jump)

        elif text[i:i+2] in rules:
            result += rules[text[i:i+2]]
            i += 2 # 2 char jump

        elif text[i:i+1] in rules:
             result += rules[text[i:i+1]]
             i += 1 # 1 char jump (rule match)

        else:
            result += text[i]
            i += 1 # 1 char jump (no rule match: fallback)

    return result

def dictionary_search(prefix, words):
    suggestions = []

    for word in words: # iterates through every word in the words list
        if word.startswith(prefix): # if any words prefix matches the input
            suggestions.append(word) # add that word to the suggestions
    return suggestions

def frequency_ranking(suggestions):
    sorted_suggestions = sorted(suggestions, key=get_frequency, reverse=True) # sorts suggestions by frequency in descending order
    return sorted_suggestions

def get_frequency(word):
    return frequency[word]

def bigram_model(current_word):
    previous_word = current_word

    if previous_word in bigrams: # checks if the last word entered is in bigrams
        next_words = bigrams[previous_word] # makes a list of next word predictions
        prediction = max(next_words, key=next_words.get) # gets the most common prediction
    else:
        prediction = None

    return prediction
