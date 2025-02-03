from bookmodule import book1, book2

def main():
    print("Hello This program to download free Organic Chemistry free pdf")
    print("""
        Choose Book's Version \n 
        type 1 or 2\n
        1.เคมีอินทรีย์ เล่ม 1\n
        2.เคมีอินทรีย์ เล่ม 2\n
        3.Exit Program press any key\n 
    """)

    book_version = input("--> ")

    if book_version not in ["1", "2"]:
        print("Thank you for using this program")
        return 0
    else:
        print(f"You Choose เคมีอินทรีย์ เล่ม {book_version}!!")

        verify = input("Do you want to download this book? (y/n) ")

        if verify == "y":
            if book_version == "1":
                book1()
            elif book_version == "2":
                book2()
            else:
                print("Invalid input")
            
            print("\n\nthank you for using this program")
            print("Do you want to download another book? (y/n) ")
            verify = input("--> ")
            if verify == "y":
                main()
        elif verify == "n":
            print("thank you for using this program")
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()