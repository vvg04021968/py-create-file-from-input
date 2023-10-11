def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as file:
        content = input("Enter new line of content: ")
        while content != "stop":
            file.write(f"{content}\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
