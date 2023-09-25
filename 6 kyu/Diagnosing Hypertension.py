# return the number of patients with hypertension in the array

def hypertensive(input):
    import re
    import statistics as st
    # I set the counter that will hold the final number of patients 
    result = 0
    # I use a for loop, to work with each patient
    for patient in input:
        # I set one list for the measurements of the systolic and one for the diastolic pressure
        s = []
        d = []
        # I extract every measurement and correspond it to the 's' list or the 'd' list
        for measurment in patient:
            temp = re.findall(r'\d+', measurment)
            res = list(map(int, temp))
            s.append(res[0])
            d.append(res[1])
        # I check the criteria
        if (st.mean(s) >= 140 and len(s) >= 2) or (st.mean(d) >= 90 and len(d) >= 2):
            result += 1
        else:
            for i in range(0, len(patient)):
                if s[i] >= 180 and d[i] >= 110:
                    result += 1
                    # In case this if statement is met, I break out of the loop cause a patient may have 2 measurements that meet this criterion
                    break
    return result