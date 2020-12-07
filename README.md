# 2020CarProject
Published for Ms. Mikaelian

I know you are probably skeptical about me using a program to do the math for me, but I invite you to read this document while I explain my work in the program, and I believe you'll see that I have more than grasped conceptually the idea that this car project was trying to teach.

<h3> Optional: Open the Code Document </h3>
I Highly encourage you to view the code in your browser by clicking here: https://github.com/1Ghasthunter1/2020CarProject/blob/main/graphareafinder.py.
If you look carefully, you will see all of the math terms, equations, and variables needed to solve this problem. I manunally coded all of these in myself, there was no copied code anyhwere here. 

<h3> Car Project Code Theory </h3>
<h4> Math Theory </h4>
Although the original directions say to use squares, triangles, and quadrilaterals, I designed this program to operate exclusively with irregular quadrilaterals, so that any data input could be handled and processed. 
<h4> Code Theory </h4>
The idea behind this code was to have a program that could read data off of an excel sheet, process the data, use the necessary geometric and trigonometric functions to find the area of each irregular quadrilateral, add up all of the areas of these shapes, and spit out the output.

This result that the program spits out is the area underneath the curve of data that was gathered in the car, and the unit for this data is equal to the units of the x axis (time in minutes), and the y axis (miles per hour). When you multiply the x axis units by 60, you arrive at time in hours. 
`Miles / Hour * Hour` yields the unit Miles, which is what this program outputs.

<H3> Explaining the code </H3>
Please note, when you see a "#SomeText And Words" In the code document, that is a comment, and I have left those there to help clear up what the program is doing at a certain time.

In essence, the program starts off by creating a set of pre-defined functions that will be used later. These functions include `find_abcd`, which simply finds the abcd values of a quadrilateral. There are also functions like `find_s`, `find_area`, etc. Note that all of these functions have been programmed myself and all of the math you see in these functions are all programmed by myself.

At the bottom of the program document, all of these functions are now used. 
<h4> Events happen in this order: </h4>
<ol>
<li>Get all of the data from excel(same as on the graph on my submitted assignment), and creates a list of all of the quadrilaterals the program has found.</li>
<li>For each one of these quadrilaterals, the program first uses the "find_abcd" function, which simply takes the four vertices that we got from step 1 and uses distance formula to derive each of the side lengths, for a, b, c, and d, of each irregular quadrilateral.</li>
<li>Then, the program uses the "find_s" function, which simply takes all four side length values (a, b, c, d), adds them together, and divides the result by two. Note that these formulas are all listed on my submitted document</li>
<li>After, the program finds the theta value (also on submitted document). The function "find_theta" is relatively complex, and uses all of the points of the quadrilateral and all of the sides of the quadrilateral to find the theta. This function finds the cross-section across the irregular quadrilateral, and uses law of cosines to find each theta on the opposite sides of the quadrilateral.</li>
<li>At this point, the program has the s value, the theta value, the a, b, c, and d value. All of this data is enough to use in our main equation (on turned in document), and the program plugs these variables into the function "find_area_of_quadrilateral", which returns the output. </li>
<li> Finally, all of these areas are added together, and the program uses the "print" function to tell us that on the screen.</li>
</ol>
<H3> What the program shows me </H3>
<p>Once I hit the run button, this is what the program shows:</p>

    From 0.0 to 2.0, The area is 0.0 Miles
    From 2.0 to 4.0, The area is 0.5333 Miles  
    From 4.0 to 6.0, The area is 1.1333 Miles  
    From 6.0 to 8.0, The area is 0.85 Miles    
    From 8.0 to 10.0, The area is 1.55 Miles   
    From 10.0 to 12.0, The area is 2.6333 Miles
    From 12.0 to 14.0, The area is 2.6333 Miles
    From 14.0 to 16.0, The area is 2.6667 Miles
    From 16.0 to 18.0, The area is 2.45 Miles  
    From 18.0 to 20.0, The area is 2.2333 Miles
    From 20.0 to 22.0, The area is 1.6 Miles   
    From 22.0 to 24.0, The area is 0.9333 Miles
    From 24.0 to 26.0, The area is 0.4833 Miles
    The total area under the curve is 19.7 Miles

I hope this helps you understand that I really did succeed with learning what this activity was meant to teach me. Programming a computer is similar to teaching someone how to do an activity, except that this person needs to know exactly, pin-point how to do the problem, or else they completely fail. And, of course, teaching only solidifies what a person already knows, not what they don't know. 
