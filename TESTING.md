# TESTING

## COMPATIBILITY

To ensure the website works on many different browsers, the website was tested on Chrome, Firefox Developer Edition, Edge and Brave.

### CHROME:

[Precious Password on Chrome](https://github.com/RebellionWebdesign/precious-password/blob/0623a95fb289bf8750cc2372e747573fdfc9de3a/docs/testing-images/pp3-chrome-compat.png)

### FIREFOX:

[Precious Password on Firefox Developer Edition](https://github.com/RebellionWebdesign/precious-password/blob/0623a95fb289bf8750cc2372e747573fdfc9de3a/docs/testing-images/pp3-firefox-dev-compat.png)

### EDGE:

[Precious Password on Edge](https://github.com/RebellionWebdesign/precious-password/blob/0623a95fb289bf8750cc2372e747573fdfc9de3a/docs/testing-images/pp3-edge-compat.png)

### BRAVE:

[Precious Password on Brave](https://github.com/RebellionWebdesign/precious-password/blob/0623a95fb289bf8750cc2372e747573fdfc9de3a/docs/testing-images/pp3-brave-compat.png)

***NOTE: Testing on Apples Safari Browser was omitted due to the lack of access to Apple devices***

## RESPONSIVE BEHAVIOR:

Responsive behaviour was not testet due to being out of scope for this project.

## MANUAL TESTING

Manual tests were made by myself, friends and family and CI community members. The following section describes the testing of the underlying functions and screen outputs in alphabetical order. For an overview of the complete program, please refer to the [Overview Flowchart](docs/readme-images/flowcharts/pp3-flowchart-general-program-overview.png).

- **advanced_mode()** - [Flowchart](docs/readme-images/flowcharts/precious-password-advanced-mode.png)

  | FEATURE                                                      | ACTION                               | EXPECTED RESULT                                              | TESTED | PASSED | COMMENT |
  | ------------------------------------------------------------ | ------------------------------------ | ------------------------------------------------------------ | ------ | ------ | ------- |
  | Notifies the user about the selection made                   | Select advanced mode from the menu   | Starts advanced mode                                         | yes    | yes    |         |
  | Calls get_password, hash_password and check_password_frequency | Start advanced mode                  | Functions get called and their results get printed           | yes    | yes    |         |
  | Displays the password, SHA-1, prefix and suffix to the user  | Start advanced mode, give a password | Shows the password, SHA-1, prefix and suffix                 | yes    | yes    |         |
  | Validates password complexity positively by calling check_password_complexity | Start advanced mode                  | If the password meets the requirements notify the user with green text | yes    | yes    |         |
  | Validates password complexity by calling check_password_complexity, warns user | Start advanced mode                  | If the password does not meet the requirements notify the user with red text | yes    | yes    |         |
  | Calls check_password_database                                | Start advanced mode                  | Calls the function to check the pwned passwords api          | yes    | yes    |         |
  | Calls new_test_question                                      | Start advanced mode                  | Calls the function to ask if the user wishes to test a new password | yes    | yes    |         |

- **back_to_main()** - [Flowchart](docs/readme-images/flowcharts/precious-password-back-to-main.png)

  | FEATURE                 | ACTION                                                       | EXPECTED RESULT                                              | TESTED | PASSED | COMMENT                                             |
  | ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ | ------ | --------------------------------------------------- |
  | Return to the main menu | In the manual page press enter when prompted                 | When pressed the user gets back to the main menu             | yes    | yes    |                                                     |
  | Input validation        | The function should only accept an empty string confirmed with the Enter button | If something else is enterd to the prompt the user gets asked to only press Enter | yes    | yes    | [Output](docs/testing-images/back-to-main-test.png) |

- **check_password_complexity**() - [Flowchart](docs/readme-images/flowcharts/precious-password-check-password-complexity.png)

  | FEATURE                                                      | ACTION                               | EXPECTED RESULT                                              | TESTED | PASSED | COMMENT |
  | ------------------------------------------------------------ | ------------------------------------ | ------------------------------------------------------------ | ------ | ------ | ------- |
  | Checks if the password has at least 8 characters using len() | Function runs automatic, gets called | returns True when criteria is met, returns False when criteria is not met | yes    | yes    |         |
  | Checks if the password has at least one uppercase letter using regex | Function runs automatic, gets called | returns True when criteria is met, returns False when criteria is not met | yes    | yes    |         |
  | Checks if the password has at least one lowercase letter using regex | Function runs automatic, gets called | returns True when criteria is met, returns False when criteria is not met | yes    | yes    |         |
  | Checks if the password has at least one lowercase letter using regex | Function runs automatic, gets called | returns True when criteria is met, returns False when criteria is not met | yes    | yes    |         |
  | Checks if the password has at least one digit using regex    | Function runs automatic, gets called | returns True when criteria is met, returns False when criteria is not met | yes    | yes    |         |
  | Checks if the password has at least one special character using regex | Function runs automatic, gets called | returns True when criteria is met, returns False when criteria is not met | yes    | yes    |         |
  | Password validation                                          | Function runs automatic, gets called | Returns True when all critera are met, otherwise False       | yes    | yes    |         |

- **check_password_database()** - [Flowchart](docs/readme-images/flowcharts/precious-password-check-password-database.png)

  | FEATURE                                                      | ACTION                               | EXPECTED RESULT                                              | TESTED | PASSED | COMMENT |
  | ------------------------------------------------------------ | ------------------------------------ | ------------------------------------------------------------ | ------ | ------ | ------- |
  | Notifies user about checking the database                    | Function runs automatic, gets called | Prints text to console when starting, adds 2 sec delay       | yes    | yes    |         |
  | Sends GET request to pwned passwords API with specified prefix using requests | Function runs automatic, gets called | Uses the prefix from pw_prefix and appends it to the API address | yes    | yes    |         |
  | Strips API answer from colons and numbers following the colon using regex | Function runs automatic, gets called | Changes APi answers from this form: 0018A45C4D1DEF81644B54AB7F969B88D65:1 to this form: 0018A45C4D1DEF81644B54AB7F969B88D65 | yes    | yes    |         |
  | Compares if generated suffix is found in the API answer      | Function runs automatic, gets called | If suffix is found, prints red warning text and sets pw_in_db to "YES"; if suffix is not found prints green positive text | yes    | yes    |         |

- **check_password_frequency()** - [Flowchart](docs/readme-images/flowcharts/precious-password-check-password-frequencyl.png)

  | FEATURE                                                      | ACTION                               | EXPECTED RESULT                                              | TESTED | PASSED | COMMENT |
  | ------------------------------------------------------------ | ------------------------------------ | ------------------------------------------------------------ | ------ | ------ | ------- |
  | Takes the generated passwords list (in memory) and searches for the password the user has given | Function runs automatic, gets called | If password is found, notify the user with red text, sets pw_in_list to "YES" | yes    | yes    |         |
  |                                                              |                                      | If password is not found, notify the user with green text, sets pw_in_list to "NO" | yes    | yes    |         |

- **clear_screen()** - [Flowchart](docs/readme-images/flowcharts/precious-password-clear-screen.png)

  | FEATURE                                                 | ACTION                               | EXPECTED RESULT                                              | TESTED | PASSED | COMMENT |
  | ------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------ | ------ | ------ | ------- |
  | Checks if underlying OS is windows                      | When function gets called, automatic | Uses "cls" to clear the screen when windows is detected, uses "clear" when MacOS or Linux is detected | yes    | yes    |         |
  | Gets called everytime the user changes the program mode | User chooses a different mode        | Clears the screen                                            | yes    | yes    |         |

- **exit_program()** - [Flowchart](docs/readme-images/flowcharts/precious-password-exit-program.png)

  | FEATURE                                      | ACTION                                                       | EXPECTED RESULT                          | TESTED | PASSED | COMMENT |
  | -------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------- | ------ | ------ | ------- |
  | Asks user if he really wants to quit         | Select quit on the start screen or from the question displayed at mode change | Displays question                        | yes    | yes    |         |
  | Prints goodbye message when user quits       | Select "y" when asked                                        | Displays text                            | yes    | yes    |         |
  | Prints restart message when user doesnt quit | Select "n" when asked                                        | Displays text                            |        |        |         |
  | Calls clear_screen (on y and n)              | Automatic                                                    | Screen gets cleared before printing text | yes    | yes    |         |
  | Adds 3 sec delay (on y and n)                | Automatic                                                    | Waits 3 sec befor continuing             | yes    | yes    |         |
  | Calls main()                                 | Automatic                                                    | Restarts program                         | yes    | yes    |         |
  | Input validation                             | Validates if input is "y" or "n"                             | See above                                | yes    | yes    |         |
  |                                              | validates if the answer is something else, notifies user that the answer is not correct | Displays text                            | yes    | yes    |         |
  | Calls exit_program()                         | Restarts function when neither "y" or "n" is pressed         | Resets the function                      | yes    | yes    |         |

- **get_password()** - [Flowchart](docs/readme-images/flowcharts/precious-password-get-password.png)

  | FEATURE                            | ACTION                                            | EXPECTED RESULT                          | TESTED | PASSED | COMMENT |
  | ---------------------------------- | ------------------------------------------------- | ---------------------------------------- | ------ | ------ | ------- |
  | Takes a user password from input() | Select one of the modes in the main menu          | Displays invitation to enter password    | yes    | yes    |         |
  | Strips spaces from start and end   | type a password with preceding and trailing space | Strips the spaces using strip()          | yes    | yes    |         |
  | Input validation                   | Loops until a valid password is given             | Restarts itself if the password is empty | yes    | yes    |         |

- **hash_password()** - [Flowchart](docs/readme-images/flowcharts/precious-password-hash-password.png)

  | FEATURE                                                  | ACTION                                 | EXPECTED RESULT                                              | TESTED | PASSED | COMMENT |
  | -------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------ | ------ | ------ | ------- |
  | Checks if the pwc_instance class has a value in pw_clean | Automatic after get_password()         | Displays an error and restarts itself if there is no value   | yes    | yes    |         |
  | Generates SHA-1 hash using hashlib                       | Automatic if password value is present | generates SHA-1 hash                                         | yes    | yes    |         |
  | Separates prefix from SHA-1                              | Automatic                              | Separates the first five characters and writes them to pw_prefix | yes    | yes    |         |
  | Separates suffix from SHA-1                              | Automatic                              | Separates the remaining characters and writes them to pw_suffix | yes    | yes    |         |

- **main()** - [Flowchart](docs/readme-images/flowcharts/precious-password-main().png)

  | FEATURE                                                      | ACTION                   | EXPECTED RESULT    | TESTED | PASSED | COMMENT |
  | ------------------------------------------------------------ | ------------------------ | ------------------ | ------ | ------ | ------- |
  | Starts the main_menu() function which handles the other functions | Press RUN PROGRAM button | displays main menu | yes    | yes    |         |

- **mode_question()** - [Flowchart](docs/readme-images/flowcharts/precious-password-mode-question.png)

  | FEATURE                                                      | ACTION                                                       | EXPECTED RESULT                         | TESTED | PASSED | COMMENT |
  | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------- | ------ | ------ | ------- |
  | Asks the user if the program mode should be changed or if the user wants to quit | Confirm that a new password should be tested                 | Displays question                       | yes    | yes    |         |
  | Starts simple mode                                           | Select "s" from prompt                                       | Starts simple mode                      | yes    | yes    |         |
  | Starts advanced mode                                         | Select "a" from prompt                                       | Starts advanced mode                    | yes    | yes    |         |
  | Calls exit_program()                                         | Select "q" from prompt                                       | Starts exit_program()                   | yes    | yes    |         |
  | Input validation                                             | If input is different from "s", "a" or "q" the function restarts itself | Displays question until answer is given | yes    | yes    |         |

- **new_test_question()** - [Flowchart](docs/readme-images/flowcharts/precious-password-new-test-question.png)

  | FEATURE                                          | ACTION                                                     | EXPECTED RESULT                                              | TESTED | PASSED | COMMENT |
  | ------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------ | ------ | ------ | ------- |
  | Asks the user if a new password should be tested | Automatic call after password was tested                   | Displays question                                            | yes    | yes    |         |
  | Calls exit_program                               | Press "n" when prompted                                    | Calls exit_program                                           | yes    | yes    |         |
  | Calls mode_question                              | Press "y" when prompted                                    | Calls mode_question                                          | yes    | yes    |         |
  | Input validation                                 | Press only Enter or other text than expected when prompted | Diplays sorry message and restarts itself when neither "y" or "n" is pressed | yes    | yes    |         |

- **show_manual()** - [Flowchart](docs/readme-images/flowcharts/precious-password-show-manual.png)

  | FEATURE                           | ACTION                    | EXPECTED RESULT                  | TESTED | PASSED | COMMENT |
  | --------------------------------- | ------------------------- | -------------------------------- | ------ | ------ | ------- |
  | Opens manual.txt from root folder | Choose RTFM from menu     | Opens the file in memory         | yes    | yes    |         |
  | Reads maual.txt when opened       | Choose RTFM from menu     | Reads the file                   | yes    | yes    |         |
  | Closes manual.txt when read       | Choose RTFM from menu     | Closes the file                  | yes    | yes    |         |
  | Displays manual.txt on screen     | Choose RTFM from menu     | Shows the manual on screen       | yes    | yes    |         |
  | Calls back_to_main                | Press Enter when prompted | Sends user back to the main menu | yes    | yes    |         |

- **simple_mode()** - [Flowchart](docs/readme-images/flowcharts/precious-password-simple-mode.png)

  | FEATURE                                                      | ACTION                             | EXPECTED RESULT                                              | TESTED | PASSED | COMMENT |
  | ------------------------------------------------------------ | ---------------------------------- | ------------------------------------------------------------ | ------ | ------ | ------- |
  | Notifies the user about the selection made                   | Select advanced mode from the menu | Starts advanced mode                                         | yes    | yes    |         |
  | Calls get_password, hash_password and check_password_frequency | Start advanced mode                | Functions get called and their results get printed           | yes    | yes    |         |
  | Validates password complexity positively by calling check_password_complexity | Start advanced mode                | If the password meets the requirements notify the user with green text | yes    | yes    |         |
  | Validates password complexity by calling check_password_complexity, warns user | Start advanced mode                | If the password does not meet the requirements notify the user with red text | yes    | yes    |         |
  | Calls check_password_database                                | Start advanced mode                | Calls the function to check the pwned passwords api          | yes    | yes    |         |
  | Calls new_test_question                                      | Start advanced mode                | Calls the function to ask if the user wishes to test a new password | yes    | yes    |         |

***All other functionality outside of functions are tested and work as expected due to their simple nature (e.g. opening and closing files). Due to time constraints they aren´t handled in this file.***

## CODE VALIDATION

The underlying code was validated with Code Institutes PEP8 validator

![PEP8 results](docs/testing-images/pp3-ci-pep8-validator-results.png)

## LIGHTHOUSE REPORTS

### LANDING PAGE
![lighthouse result](docs/testing-images/pp3-lighthouse-result.png)

## BUGS

- *Program reloads without message when the user exits the program from the main menu.* This bug was due to the fact that the default Exit option in console-menu is made for when the program runs inside of a shell process on a computer. It would simply close the window but this is not possible on Heroku. The solution was to write a custom function which displays a good bye text before restarting the program.
- *Colorama adds color to empty lines.* Apparently colorama also interprets newline characters and thus colors completely blank lines. This was solved by printing newlines with an empty print function instead of newline characters where we need colored text.
- *The check_password_database function was unable to validate if a password is in the database or not based on the prefix search.* In a previous version the function checked the GET status for [200 OK] to validate if there is any match in the database. This is wrong. A prefix can be multiple times matched, therefore the API responds almost every time with [200 OK]. To fix this the function must check for [404] because the API responds with [404] when the prefix is not found.
- *The check_password_database was unable to compare a given suffix to its counterpart from the API answer.* This happened because the answer is already a list. After stripping and converting to a list (again) the API answer was unreadable for the function. Investigating the used variables and their values exposed that there are too many steps in converting to a list. This was changed and it works now.
- *When opening the manual the user has to scroll up a bit to see the complete text.* This happens because the terminal scrolls to the last line printed. This could be solved by adding a line-by-line print feature where the user has to press a button on the keyboard if he is done reading the line. This feature is to be added in the future due to time constraints.
