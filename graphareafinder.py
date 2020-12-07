import math #gives the program math ability
import xlrd #gives the program the ability to read the data from an excel file
import trianglesolver #only utilizes the SSS function, law of cosines

excel_sheet_location = ("data.xlsx")

def get_data_from_excel(): #This program simply extracts the graph you see in problem 5 from an excel sheet. The data is listed in rows and columns for each data point
    '''
    Retrieves data from the excel sheet
    '''
    first_iteration_graph_point = False
    exceldata = []
    workbook = xlrd.open_workbook(excel_sheet_location) 
    sheet = workbook.sheet_by_index(0) 
    for column in range(0, 14):      
        time = sheet.cell_value(0, column)
        speed = sheet.cell_value(1, column)
        exceldata.append((time, speed))
    temp_list = []
    for current_point in exceldata:
        if not first_iteration_graph_point:
            previous_point = current_point
            first_iteration_graph_point = True
            continue
        Cx, Cy = current_point
        Dx, Dy = Cx, 0
        Bx, By = previous_point
        Ax, Ay = Bx, 0
        temp_list.append(((Ax, Ay),
                          (Bx, By),
                          (Cx, Cy),
                          (Dx, Dy)))
        previous_point = current_point
    return temp_list

def find_abcd(four_point_tuple): #Calculates all of the side lengths based on the four vertices given to this function
    def distance_formula(point_a, point_b):
        return math.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)
    Apoint, Bpoint, Cpoint, Dpoint = four_point_tuple
    a = distance_formula(Apoint, Bpoint)
    b = distance_formula(Bpoint, Cpoint)
    c = distance_formula(Cpoint, Dpoint)
    d = distance_formula(Dpoint, Apoint)
    return (a, b, c, d)

def find_s(side_length_tuple): #Finds the S value from all of the side lengths
    '''
    Formula: S = (a+b+c+d)/2

    Takes a 4-value tuple as input with each side length, returns the S value

    '''
    a, b, c, d = side_length_tuple
    s = (a+b+c+d)/2
    return s

def find_theta(four_point_tuple, side_length_tuple): #Calculates the theta as seen in the diagram on problem 7. Takes all four vertices coordinates and all four side lengths
    '''
    Takes the abcd side lengths, and returns the theta angle as defined on the worksheet
    theta = (theta1+theta2)

    Do note that with this given problem, one of the thetas will always be 90 degrees. As a result, this function interprets theta1 as 90, solves for theta2
    '''
    def distance_formula(point_a, point_b):
        return math.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)

    Apoint, Bpoint, Cpoint, Dpoint = four_point_tuple
    a, b, c, d = side_length_tuple
    e = distance_formula(Bpoint, Dpoint)
    temp_list = [a, b, c, d]
    nonecounter = 0
    for side in temp_list:
        if side == 0.0:
            nonecounter += 1
    
    if nonecounter <= 1: #finds theta2 when all of the sides are greater than 0 (if there is an area under the line)
        if c == 0.0: #in the case where the graph touches 0 with a negative derivative, the triangle calc must be handled differently to find theta as there is no theta in the "upper-right" of the graph section
            e = distance_formula(Apoint, Cpoint)
            a, b, c, AngleA, AngleB, AngleC = trianglesolver.sss(a, b, e) #Solves SSS for the given side lenghts, a, d, e
        else:
            a, b, c, AngleA, AngleB, AngleC = trianglesolver.sss(b, c, e) #Solves SSS for the given side lenghts, a, d, e
        theta1 = 90
        theta2 = math.degrees(AngleC) #convert to degrees, SSS function outputs radians
        #Angle C is the opposite from side C (side e) inputted into the SSS function, or in this diagram, the top right of each irregular quadrilateral
        theta = (theta1+theta2)
        theta = math.radians(theta)
        return theta
    else:
        return None

def find_area_of_quadrilaterial(quadrilateral_tuple): #Takes all of the 6 values calculated previously, the theta value, the S value, and all four side lengths
    '''
    Formula: sqrt((s - a)(s - b)(s - c)(s - d) - abcd * cos^2(theta/2))

    Takes a quadrilateral tuple: (s, theta, a, b, c, d)
    Returns area of the quadrilateral
    '''
    s, theta, a, b, c, d = quadrilateral_tuple #unpacks all of the data into individual variables
    if theta is not None:
        area = math.sqrt((s - a) * (s - b) * (s - c) * (s - d) - (a * b * c * d * (math.cos(theta / 2) ** 2)))
        area = round(area, 6)
        return area

#======== From this point below, all of the functions defined above are used. See all comments below: ========#
abcddata = get_data_from_excel() #This function, get_data_from_excel(), Reads all of the data from an excel sheet (same data as problem 5), and combines the data into a list of four vertices reprisenting each quadrilateral
total_area = 0 #Just sets the total area to 0 beforehand, will be used later
for points_quadrilateral in abcddata: #For every quadrilateral that we found from two lines above, do the following:
    sides_quadrilateral = find_abcd(points_quadrilateral) #Use the find_abcd function to find all the side lengths, we give it the data points_quadrilateral, which contains all of the vertices for each quadrilateral
    s = find_s(sides_quadrilateral) #we can use your find_s function we made previously to take all of the side lengths and find the S value
    theta = find_theta(points_quadrilateral, sides_quadrilateral) #Given the four vertices and side lengths of the quadrilateral, find the theta value (diagram on problem 7 of worksheet)
    quadrilateral_dataset = (s, theta, sides_quadrilateral[0], sides_quadrilateral[1], sides_quadrilateral[2], sides_quadrilateral[3]) #Just combine all of the information from above into one giant variable called quadrilateral_dataset
    area = find_area_of_quadrilaterial(quadrilateral_dataset) #Use the find_area_of_quadrilateral function we made previously. We give this function the theta, s, and all side length values
    if area == None:
        area = 0.0 #If there is no area reported, this means the current quadrilateral does not exist, so we can set this to 0.
    print(f"From {points_quadrilateral[0][0]} to {points_quadrilateral[0][0]+2}, The area is {area} MPH * T") #Just puts a message on the screen that says "From this x value to this x value, the area under the curve is X MPH * T"
    total_area += area #add up all of the areas from each quadrilateral into one large variable
print(f"The total area under the curve is {total_area} MPH * T ") #Puts a message out with the total area under the entire curve
