import tkinter as tk
import arabic_reshaper
from backend import transliterate, rules, dictionary_search, frequency_ranking, words, bigram_model

# window creation
window = tk.Tk()
window.title("Arabic Transliteration Tool")
window.geometry("500x400")


# input section
input_label = tk.Label(window, text="Enter Arabic word transliterated in Latin:") # outputs prompt for user to enter word
input_label.pack() # displays the widget/prompt

input_box = tk.Entry(window, width=50) # takes input
input_box.pack() # displays the input entry window

# validation/error message section
error_label = tk.Label(window, text="", fg="red")
error_label.pack()

# output section
output_label = tk.Label(window, text="Output (Arabic):")
output_label.pack()

output_box = tk.Label(window, text="", bg="white", width=40, height=2)
output_box.pack()

# suggestions section
suggestions_label = tk.Label(window, text="Suggestions:")
suggestions_label.pack()

suggestions_box = tk.Label(window, text="", bg="white", width=40, height=2)
suggestions_box.pack()

# prediction section
prediction_label = tk.Label(window, text="Predicted next word:")
prediction_label.pack()

prediction_box = tk.Label(window, text="", bg="white", width=40, height=2)
prediction_box.pack()

# function to validate input before transliteration
def validate_input(user_input):
    # empty input
    if user_input.strip() == "":
        return "Please enter a transliterated word."

    # normalise capitals
    user_input = user_input.lower()

    # valid characters (Latin + Arabizi numerals + spaces)
    allowed = set("abcdefghijklmnopqrstuvwxyz23679 ")

    for char in user_input:
        if char not in allowed:
            return "Invalid character detected."

    # at least one transliteration rule exists in input
    valid_mapping_found = False

    for i in range(len(user_input)):
        if (user_input[i:i+3] in rules or
            user_input[i:i+2] in rules or
            user_input[i:i+1] in rules):
            valid_mapping_found = True
            break

    if not valid_mapping_found:
        return "Input not recognised."

    return None

# function to reverse text and fix incorrect Arabic script
def format_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    reshaped_text = reshaped_text[::-1]
    return reshaped_text

def update_transliteration(event): # runs when an event occurs
    user_input = input_box.get() # safely gets the user input (in lower case to match rules)

    # run validation first
    error_message = validate_input(user_input)

    if error_message:
        error_label.config(text=error_message)

        # clear outputs if invalid
        output_box.config(text="")
        suggestions_box.config(text="")
        prediction_box.config(text="")
        return

    # clear old errors if valid
    error_label.config(text="")

    arabic_text = transliterate(user_input, rules) # transliterates the input using longest match rules
    output_box.config(text=format_arabic(arabic_text)) # changes the text of the output_box to the transliterated Arabic text

    top_suggestions = get_top_suggestions(arabic_text) # retrieves top suggestions

    # iterates and displays top suggestions (with comma between each one)
    formatted_suggestions = [format_arabic(word) for word in top_suggestions]
    suggestions_box.config(text=", ".join(formatted_suggestions))

    # retrieves and displays top prediction
    prediction_text = get_prediction(arabic_text)
    prediction_box.config(text=prediction_text)

def get_top_suggestions(arabic_text):
    suggestions = dictionary_search(arabic_text, words) # retrieves suggestions
    ranked = frequency_ranking(suggestions) # ranks suggestions by frequency
    return ranked[:3] # returns top 3 ranked suggestions (highest frequency)

def get_prediction(arabic_text):
    prediction = bigram_model(arabic_text)
    return format_arabic(prediction)

# real-time behaviour (when user types, output transliteration updates)
input_box.bind("<KeyRelease>", update_transliteration)

window.mainloop() # run GUI
