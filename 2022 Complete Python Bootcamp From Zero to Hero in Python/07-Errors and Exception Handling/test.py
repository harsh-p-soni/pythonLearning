def askint():
    try:
        val = int(input("Please enter an integer: "))
    except Exception as e:
        print(e)
        print("Looks like you did not enter an integer!")
    finally:
        print("Finally, I executed!")

askint()

