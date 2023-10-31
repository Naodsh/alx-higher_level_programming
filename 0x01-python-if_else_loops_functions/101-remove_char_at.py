def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        # Check if the index is out of range
        return input_str
    else:
        # Slice the string before and after the specified index
        return input_str[:n] + input_str[n+1:]
