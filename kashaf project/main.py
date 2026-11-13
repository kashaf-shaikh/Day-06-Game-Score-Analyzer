print("============ Game Score Analyzer ===========")

user_name = input("Enter your name:\n")
# TODO 3: Create a function called calculate_total that accepts a list of scores.
def calculate_total(list_of_scores: list):
    total = 0
    for number in list_of_scores:
        total += number
    return total

# TODO 5: Create a function called calculate_average that accepts a list of scores.
def calculate_average(scores: list,total_score:int):
    len_of_number = len(scores)
    average = round(total_score/len_of_number,2)
    return average

# TODO 7: Create a function called find_highest_score that accepts a list of scores.
def find_highest_score(scores:list):
    highest_score = 0
    for score in scores:
        if score > highest_score:
            highest_score = score
    return highest_score
# TODO 9: Create a function called get_performance that accepts the average score.
def get_performance(average_score:float):
    if average_score >= 90:
        return"Excellent!😁"
    elif average_score >= 70:
        return "good😊"
    elif average_score >= 50:
        return "Average😣"
    else:
        return "Needs improvement❌"
# TODO 11: Create a list containing 5 game scores.
scores = []
number_of_subjects = int(input("How many subject you have.?"))
for _ in range(number_of_subjects):
    user_score = int(input("Enter your score in each subject :"))
    scores.append(user_score)

total_score = calculate_total(list_of_scores=scores)
average_score = calculate_average(scores=scores,total_score=total_score)
highest_score = find_highest_score(scores=scores)
user_performance = get_performance(average_score = average_score)
# TODO 16: Print a final report showing the player's name, scores, total, average,
# highest score and performance.
# Example:
print(f"Player: {user_name}")
print(f"Score : {scores}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Highest Score: {highest_score}")
print(f"Performance: {user_performance}")