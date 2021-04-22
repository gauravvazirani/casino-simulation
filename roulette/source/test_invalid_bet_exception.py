import invalid_bet_exception

if __name__ == '__main__':
    try:
        raise invalid_bet_exception.InvalidBetException
    except invalid_bet_exception.InvalidBetException:
        print("Caught InvalidBetException")
