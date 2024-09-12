def format_to_title_case(text):
    exceptions = {'de', 'del'}
    words = text.lower().split()
    return ' '.join([word.capitalize() if word not in exceptions else word for word in words])
