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
    for i in range(len(filtered_words) - memory - prediction_window + 1):
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
        word_tuple = tuple(word_sequences[i])
        pred_tuple = tuple(prediction_word_sequences[i])

        # Check if sequence currently exists in freq dict
        if word_tuple not in freq_dict:
            freq_dict[word_tuple] = {} # Initialize a dict for the predictions and their couns

        # Check if the prediction that follows the sequence is in the dict
        if pred_tuple not in freq_dict[word_tuple]:
            freq_dict[word_tuple][pred_tuple] = 0 # initalize the count to 0 if our first time seeing this prediction
        
        # Increment the freq of the prediction sequence following this word sequence
        freq_dict[word_tuple][pred_tuple] += 1
        
    # Make a dictionary for the probabiltiies instead of the counts
    probability_dict = {}
    # Keep track of the total # of pairs of words in the text
    for sequence in freq_dict:
        prediction_seq_count = sum(freq_dict[sequence].values())  # Total count for the sequence
        probability_dict[sequence] = {}
        for pred_seq in freq_dict[sequence]:
            # Calculate probability of the pred sequence for the word sequence
            probability_dict[sequence][pred_seq] = freq_dict[sequence][pred_seq] / prediction_seq_count

    # Write to output file model.txt
    with open('model.txt', 'w') as file:
        for sequence in probability_dict:
            # Write the new sequence
            file.write(f"+{' '.join(sequence)}\n")
            for pred in probability_dict[sequence]:
                if pred:
                    # Write each prediction sequence for this sequence and its probability
                    file.write(f"{' '.join(pred)} {probability_dict[sequence][pred]:.2f}\n")

    print("Model successfully built and written to model.txt")

build_model(3, 1)
