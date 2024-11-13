def build_model(memory, prediction_window):
    # Read english text from input.txt
    with open("input.txt", "r") as file:
        content = file.read()

    # Turn lowercase
    filtered_content = content.lower()

    # Keep alphanumeric chars, spaces, contractions and contiguous sets of characters
    filtered_content = ''.join(x for x in filtered_content if x.isalnum() or x in {" ", "-", "’", "'"})

    # Tokenize words
    words = filtered_content.split()

    # Ignore certain words
    ignore_list = ["the", "a", "an", "this", "that"]
    filtered_words = [x for x in words if x not in ignore_list]

    # Create sequences of length memory
    word_sequences = []
    prediction_word_sequences = []
    # Loop through each word to find the sequences of that word
    for i in range(len(filtered_words) - prediction_window):
        # Find the sequences of length memory
        word_sequences.append([filtered_words[i:i + memory]])
        # Find the word sequence of length prediction_window that follows it 
        prediction_word_sequences.append([filtered_words[i + memory: i + memory + prediction_window]])

    print(word_sequences)
    print(prediction_word_sequences)

    return

build_model(1, 1)
