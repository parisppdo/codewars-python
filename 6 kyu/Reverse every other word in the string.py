def reverse_alternate(st):
    cleaned_string = ' '.join(st.strip().split())
    words_list = cleaned_string.split()

    for i in range(1, len(words_list), 2):
        words_list[i] = words_list[i][::-1]

    return ' '.join(words_list)