def read_and_write_file():
    while True:
        try:
            # Ask the user for the input filename
            input_filename = input("Enter the name of the file to read: ").strip()
            if not input_filename:
                print("Error: Filename cannot be empty. Please try again.")
                continue

            # Attempt to open and read the file
            with open(input_filename, 'r') as infile:
                content = infile.readlines()
            print(f"Successfully read from '{input_filename}'.")
            break

        except FileNotFoundError:
            print("Error: The file does not exist. Please check the filename and try again.")
        except PermissionError:
            print("Error: You do not have permission to read the file. Please try a different file.")
        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")
            return

    while True:
        try:
            # Ask the user for the output filename
            output_filename = input("Enter the name of the file to write to: ").strip()
            if not output_filename:
                print("Error: Filename cannot be empty. Please try again.")
                continue

            # Modify the content (e.g., add line numbers)
            modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

            # Write the modified content to the new file
            with open(output_filename, 'w') as outfile:
                outfile.writelines(modified_content)
            print(f"Modified content has been written to '{output_filename}' successfully.")
            break

        except PermissionError:
            print("Error: You do not have permission to write to the file. Please try a different file.")
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")
            return

if __name__ == "__main__":
    read_and_write_file()