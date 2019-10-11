def cellCompete(states, days):
    # WRITE YOUR CODE HERE


    def update_per_day(states):
        left_end = 0
        right_end = 0
        new_state = []
        if left_end == states[1]:
            new_state.append(0)
        else:
            new_state.append(1)

        for i in range(1, 7):
            if states[i-1]==states[i+1]:
                new_state.append(0)
            else:
                new_state.append(1)
        if right_end == states[6]:
            new_state.append(0)
        else:
            new_state.append(1)

        return new_state

    for j in range(0, days):
        new_state = update_per_day(states)
        states = new_state

    return states

if __name__=="__main__":
    strs = [1, 0, 0, 0, 0, 1, 0, 0]
    print(cellCompete(strs, 1))

    strs = [1, 1, 1, 0, 1, 1, 1, 1]
    # print(cellCompete(strs, 1))
    print(cellCompete(strs, 2))