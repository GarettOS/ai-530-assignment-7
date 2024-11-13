# I used memory = 1 and prediction_window = 1 to create model.txt from input.txt
import random

def run_model(memory, prediction_window, prompt):
    print("Running Model....")
    print(f"Generating prediction of length 50 from \"{prompt}\"....\n")
    # Filter the prompt like in build_model.py
    filtered_prompt = prompt.lower()
    filtered_prompt = ''.join(x for x in filtered_prompt if x.isalnum() or x in {" ", "-", "’", "'"})
    prompt_tokens = filtered_prompt.split()

    # Check if the prompt is valid length
    if (len(prompt_tokens) != memory):
        print("Error: Prompt must be the same length as memory")
        return

    # Create freq dict like in build_model to store the model
    freq = {}
    with open('model.txt', 'r') as file:
        current_sequence = []
        for line in file:
            # If we are on a line that is a memory
            if line[0] == '+':
                # Split into tokens and take the word sequence
                line = line.replace('+', '')
                word_sequence = line.split()
                current_sequence = word_sequence

                # Add to our dict
                if tuple(current_sequence) not in freq:
                    freq[tuple(current_sequence)] = {}

            else: # it is not a memory line, so it should have prediction sequence + the probability
                pred_tokens = line.split()
                # Probability will always be at the last token
                pred_sequence = pred_tokens[:-1]
                probability = pred_tokens[-1]

                # Add this to our current mem sequence as its own dict
                freq[tuple(current_sequence)][tuple(pred_sequence)] = float(probability)

    # Start generating the sentence 
    GENERATION_LENGTH = 50
    generated_words = prompt_tokens
    current_sequence = tuple(prompt_tokens)
    for i in range(GENERATION_LENGTH-1):
        # Check if the current word is not in the model
        if current_sequence not in freq:
            #print(f"Sequence {current_sequence} not found in model, picking random seq to continue....\n")
            current_sequence = random.choice(list(freq.keys()))

        # Get the possible predictions
        preds = freq[current_sequence]

        # Find the highest probability for the next word
        highest_val = float('-inf')
        highest_prob_predictions = []
        for sequence in preds:
            if preds[sequence] > highest_val:
                highest_val = preds[sequence]
                highest_prob_predictions = [sequence]
            elif preds[sequence] == highest_val:
                highest_prob_predictions.append(sequence)
        
        # Check if there is multiple with same highest probability
        num_predictions = len(highest_prob_predictions)
        # If there is only one highest probability
        if num_predictions == 1:
            the_holy_choice = highest_prob_predictions[0]
        # If there is 2 with the same probability, perform coinflip
        elif num_predictions == 2:
            coin_flip = random.random()
            if coin_flip < 0.5:
                the_holy_choice = highest_prob_predictions[0]
            else:
                the_holy_choice = highest_prob_predictions[1]
        else:
            the_holy_choice = random.choice(highest_prob_predictions)

        # Add this prediction to our generated words
        generated_words.extend(the_holy_choice)
        
        # Make the generated word the new sequence to look for 
        current_sequence = the_holy_choice
    
    print("Generated Words: ")
    print(' '.join(generated_words))
    print('\n')
        