from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States guessing")
image = "blank_states_img.gif"
screen.addshape(image)
t = Turtle()
t.shape(image)

list_of_gussing = []
list_of_missing = []

new_t = Turtle()
game_is_on = True

while len(list_of_gussing) < 50:

    answer = screen.textinput(title=f"{len(list_of_gussing)}/50 state", prompt="what is another state name? ").title()
    states_data = pandas.read_csv("./50_states.csv")
    list_of_data_states = states_data["state"].tolist()

    if answer == "Exit":
        for i in list_of_data_states:
            if i not in list_of_gussing:
                list_of_missing.append(i)

        new_missing_data_file = pandas.DataFrame(list_of_missing)
        new_missing_data_file.to_csv("missing_states.csv")
        break

    if answer in list_of_data_states:
        list_of_gussing.append(answer)
        row_with_specific_data = states_data[states_data["state"] == answer]

        x_value = int(row_with_specific_data.x)
        y_value = int(row_with_specific_data["y"])

        new_t.penup()
        new_t.hideturtle()
        new_t.goto(x_value, y_value)
        new_t.write(row_with_specific_data.state.item(), align="center", font=("Arial", 12, "normal"))




# df = pandas.DataFrame(data_dict)
# df.to_csv("missed_states.csv")


screen.exitonclick()
