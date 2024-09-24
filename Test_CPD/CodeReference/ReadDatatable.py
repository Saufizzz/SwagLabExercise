expected_program = "dsafa"
# This line finds all elements that represent program names in the table.
# It uses XPath to locate <td> elements that are in the 5th column (td[5]) of each row (//tr).
program_names = driver.find_elements(By.XPATH, "//tr/td[5]")
# This loop iterates through each program name found in the table.
# enumerate() is used to get both the index i and the program name program. start=1 ensures that the index starts from 1 instead of 0.
for i, program in enumerate(program_names, start=1):
    print(program.text)
    if program.text == expected_program:
        xpath_text = f"//tr[{i}]/td[8]//i[1]"
        button = driver.find_element(By.XPATH, xpath_text)
        button.click()
        break  # Exit loop after clicking the button