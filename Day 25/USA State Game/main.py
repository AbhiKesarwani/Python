import turtle
import pandas

screen = turtle.Screen()
screen.title(f"U.S. States Game Score")

#image = "blank_states_img.gif"
#screen.addshape(image)
#turtle.shape(image)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

guessed_state = []
score = 0
while score<51:
    answer_state = screen.textinput(f"{score}/50 State Correct Guess", "What's state name?")
    answer_state = answer_state.title()
    guessed_state.append(answer_state)
    for data_state in data["state"]:
        if answer_state == data_state:
            score += 1
            tom = turtle.Turtle()
            tom.hideturtle()
            tom.penup()
            state_list = data[data["state"] == answer_state]
            x_cor = state_list["x"]
            y_cor = state_list["y"]
            tom.goto(int(x_cor),int(y_cor))
            tom.write(answer_state)   #state_list.state.item()
        elif answer_state == "Exit":
            score = 51
            missing_states = [states for states in data["state"] if states not in guessed_state]

            missing_states_dataframe = pandas.DataFrame(missing_states)
            missing_states_dataframe.to_csv("missing_states.csv")







