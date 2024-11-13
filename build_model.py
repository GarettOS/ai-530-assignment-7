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
        word_sequences.append(filtered_words[i:i + memory])
        # Find the word sequence of length prediction_window that follows it 
        prediction_word_sequences.append(filtered_words[i + memory: i + memory + prediction_window])

    # Make a freq dictionary to count how often sequences appear in the text
    # freq_dict = {
    #     sequence {
    #         prediction_sequence: count
    #          .
    #          .
    #     }
    #     sequence2 {
    #         prediction_sequence: count
    #          .
    #          .
    #     }
    # will have to convert sequence lists to tuples to store in dict

    freq_dict = {}
    for i in range(len(word_sequences)):
        # Check if sequence currently exists in freq dict
        if tuple(word_sequences[i]) not in freq_dict:
            freq_dict[tuple(word_sequences[i])] = {} # Initialize a dict for the predictions and their couns

        # Check if the prediction that follows the sequence is in the dict
        if tuple(prediction_word_sequences[i]) not in freq_dict[tuple(word_sequences[i])]:
            freq_dict[tuple(word_sequences[i])][tuple(prediction_word_sequences[i])] = 0 # initalize the count to 0 if our first time seeing this prediction
        
        # Increment the freq of the prediction sequence following this word sequence
        freq_dict[tuple(word_sequences[i])][tuple(prediction_word_sequences[i])] += 1
        
    

    return

build_model(1, 1)
