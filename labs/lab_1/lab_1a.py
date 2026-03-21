"""
lab_1a.py

The first lab in the BWSI CSS course. To complete this lab, fill out the variable on line 10
with your name. Then, save the code, add it to the staging area, and commit it to the Git tree.
"""
def update():
    global counter

    counter += rc.get_delta_time()

def main():
    print("Hello World!")
    

    name = "Alex Lu" # TODO: Insert your name between the double quotes

    
    print(f"{523+910}")
    print(f"Hello {name}, welcome to RACECAR!")
    print(f"{round(counter, 1)} seconds have passed since the program started!")

if __name__ == "__main__":
    main()
