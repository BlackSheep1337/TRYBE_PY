def vertical_inverted_ladder(word):
    for removed_letters in range(len(word)):
        for idx in range(len(word) - removed_letters):
            print(word[idx], end="")
        print()

if __name__ == "__main__":
    name = input('Digite um nome: ')
    vertical_inverted_ladder(name)