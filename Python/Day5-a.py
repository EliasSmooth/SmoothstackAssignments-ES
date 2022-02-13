input = [3, [80, 1.73], [55, 1.58], [49, 1.91]]

def math(input):
    a = []
    for x in input[1:]:
        BMI = (x[0] / x[1]**2)
        if BMI < 18.5:
            a.append('Underweight')
        if BMI >= 18.5 and BMI < 25.0:
            a.append('Normal Weight')
        if BMI >= 25.0 and BMI < 30.0:
            a.append('Overweight')
        if BMI >= 30.0:
            a.append('Obese') 
        
    print(a)
    
       
       
math(input)

        

    