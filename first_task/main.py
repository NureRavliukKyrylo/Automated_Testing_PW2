from formatter import ExcelFormatter


def main():
    file_path = "test.xlsx"

    formatter = ExcelFormatter(file_path)
    formatter.format()

    print("Excel formatted successfully!")


if __name__ == "__main__":
    main()