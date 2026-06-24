while True:
    print("\n--- Student Quiz Average Calculator ---")
    
    # INPUT: Ask user to enter three quiz marks
    mark1 = float(input("Enter quiz mark 1: "))
    mark2 = float(input("Enter quiz mark 2: "))
    mark3 = float(input("Enter quiz mark 3: "))
    
    # PROCESS: Calculate the average mark
    average = (mark1 + mark2 + mark3) / 3
    
    # OUTPUT: Display the average
    print(f"\nAverage mark: {average:.2f}")
    
    # SELECTION: Determine whether the student passes or fails
    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")
    
    # ITERATION: Allow another student's marks to be entered
    another = input("\nEnter another student's marks? (yes/no): ").strip().lower()
    if another != "yes":
        print("Program ended. Goodbye!")
        break
