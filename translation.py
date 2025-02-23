from unidecode import unidecode
import re

custom_mapping = {
    'χ': 'ch',  # Replace "kh" with "ch"
    'Θ': 'th',  # Add custom mappings as needed
    'φ': 'ph',
    # Add more mappings as needed
}

def clean(text):
    punctuation=[ "Αρ.","/", ".", ",", "*", "(", ")", "&", "#", "@", "!"]
    text=text.strip()
    for punc in punctuation:
        text=text.replace(punc, "")
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def translate_clean(text):
    transliterated_text = clean(text)
    # Perform the initial transliteration using unidecode
    transliterated_text = unidecode(transliterated_text.lower())
    
    # Apply custom mappings
    for greek_char, custom_value in custom_mapping.items():
        transliterated_text = transliterated_text.replace(unidecode(greek_char), custom_value)

    return transliterated_text

