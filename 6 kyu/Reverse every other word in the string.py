def reverse_alternate(st):
    cleaned_string = ' '.join(st.strip().split())
    words = cleaned_string.split()

    for i in range(1, len(words), 2):
        words[i] = words[i][::-1]

    return ' '.join(words)
