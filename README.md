# PYHangman
Simple hangman for Python 3.

## How to Play
- Run `hangman.py`.
- A random word will be chosen from the specified `WORDFILE` to 
be guessed.
- Guess by typing one lowercase letter when prompted.
- Win within the amount of unique letter guesses as specified by 
`MAXLIVES`.

## Settings
Can be found and customised on the top portion of the source code.
- `WORDFILE`: A list of words to be selected. One lowercase 
alphabetic word per line. Defaults to `words.txt`.
- `MAXLIVES`: Maximum amount of unique letter guesses (lives). 
Defaults to 10.
- `BARRIER`: Border character to be printed. Defaults to hashes.