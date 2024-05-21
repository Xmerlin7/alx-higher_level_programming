#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    hidden = dir(hidden_4)
    for hidden in names:
        if hidden[:2] != "__":
            print(hidden)
