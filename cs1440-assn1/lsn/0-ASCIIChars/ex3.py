# Justin Herzog A02306067
def scoreWord(word):
    score = 0
    # HINT: Try out "a".isalpha() and "!".isalpha() in the REPL! `help(str.isalpha)` may also come in handy :)
    # Thanks for the hint =D
    # We should be able to loop through word and use the .isalpha() method to see whether or not to add to the score.
    for i in word:
        if i.isalpha():
            # ord(A) = 65, ord(B) = 66, ord(C) = 67, etc...
            # If we uppercase all letters and subtract 65 we'll assign the correct score for each letter.
            score += (ord(i.upper()) - 65)
        elif not i.isalpha():
            pass

    return score

if __name__ == '__main__':
    provided = [
        "One",
        "oNE",
        "supercalifragilisticexpialidocious",
        "t",
        "aAaA",
        "Zap!",
        "Tr!ck3d y4!",
        "G0t it!"
    ]

    # For each word in the provided list, give the word to the function score word and print some fancy formatted output
    for word in provided:
        print(f"The score of {word} is: {scoreWord(word)}")

    # Should Output:
        # The score of One is: 31
        # The score of oNE is: 31
        # The score of supercalifragilisticexpialidocious is: 345
        # The score of t is: 19
        # The score of aAaA is: 0
        # The score of Zap! is: 40
        # The score of Tr!ck3d y4! is: 75
        # The score of G0t it! is: 52
