#!/usr/bin/env python3
import statistics
def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    total_scores = 0
    for score in scores:
        total_scores += score # total_scores = total_scores + score
    average = total_scores / len(scores)
    median_index = len(scores) // 2
    median = statistics.median(scores)
         
                
    # format and display the result
    print()
    print("Score total:       ", total_scores)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Low Score:         ", min(scores))
    print("High Score:        ", max(scores))
    print("Median Score:      ", median)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
