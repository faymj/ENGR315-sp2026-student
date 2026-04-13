import sys
import time

"""
This code is altered with the explict objectives of maximizing its versatility
some of the most notable edits are to the file patcher, which were done in the
 interest of keeping operation costs down.
Please put location values as their FIPS code, more information can be found at 
https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt

It should be noted this system is only designed to handle 2 instances
A cooler system would allow for either up to any/all to be queried
Or for specific ones to be queried from the command line
But I don't have that much time at my disposal

Cool fun fact: entries show up in the data as relevant, so places no yet afflicted
do not have any entries until they have a case to report; I just like that this saves
on file size. This also means that case 1 is the first entry.

I have probably misused the ways which <triple"> are supposed to be used.

Reminders for me
Rockingham County (County Code: 51165)
Harrisonburg (County Code: 51660)

"""
#County codes of relevance
#replace these with anything from the offical list, seems to have mimimal impact on Q3
Location1 = 51660
Location2 = 51165

#Prepped variables for calculations
Location1_stow = ""
Location2_stow = ""

#putting some space between noisy terminal text and the much cooler data responses.

print("________________________________________________________________________________________________")
#Edits to the praser in order to make it more useful.
def parse_nyt_data_for_location(Location, file_path='',):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fdone = True
            continueips, cases, deaths) information
    """
    # data point list
    data=[]

    #set the file path
    file_path = "./././Exams\Assignment 1 - COVID Data/us-counties.csv"

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths 
        (date, county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)
        
        #only save data we are actually asking for.
        if fips == ( str(Location) ):
        #do nothing

            #print("FOUND ITEM =========================================V" + str(entry)) #Place visual flag
            data.append(entry)
            
        #This is probably the dumbest way I could say do !=, but that operator doesn't seem to want to work
        else:
            donothing = 0        
            #print(entry + "test")

    line = (data[0])
    (date, county, state, fips, cases, deaths) = line
    print("Finished creating a list for " + str(county) + ".")
    return data


"""
some arguements can be made as to whether or not reading the whole list every time it makes a stow is efficent
I mean, its not as efficent as having the program make every stow at once from the first read,
but at that point it would also be more effective to make the program deal with unlimited stows,
which its own can of worms and beyond the scope of this assignment.
"""

#custom def because I am tired of copying these over
def getdatelist(data):
    lines = data
    #setflag = 0
    count = 0
    #prep the list
    all_dates = list()
    #set a limit to counting (just in case something weird happens otherwise?)
    while count < len(lines):

        #unpack and proccess into a list of only dates
        line = (lines[count])
        (date, county, state, fips, cases, deaths) = line
        count = count + 1
        all_dates.append(date)
    #now to actually use these
    return all_dates

#this is basically just a matter of grabbing the first value that shows up, because the are no entries for 0 case senarios
def first_question(data):

    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Location?
    :return:
    """

    # your code here

    #pull from stow (we know the first entry will be the first confirmed case)
    line = (data[0])

    #tell the computer whats what
    (date, county, state, fips, cases, deaths) = line

    #make statement
    print("First COVID case for " + str(county) + " in " + str(state) + " occured on " + str(date) + ".")

    #wow ok so yeah turns out sorting out useful data makes this whole thing way way easier huh
    return

#this is just a matter of iterating over two values, grabbing the difference,
# and seeing where the difference is the biggest (careful to select the right day)
def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here

    #grab stow for local variables
    lines = data

    #setflag = 0
    count = 0

    #prep the list
    all_cases = list()

    #set a limit to counting (just in case something weird happens otherwise?)
    while count < len(lines):

        #unpack
        line = (lines[count])
        (date, county, state, fips, cases, deaths) = line
        count = count + 1
        all_cases.append(cases)
    
    #diagonistic for checking that our numbers are right
    #print(all_cases)

    #begin loop two = checking for our maximum increase where we assume that its probably not the beginning
    count = 0
    difference_of_cases = list()
    while count < len(all_cases) - 1:
        #finding the difference by item 2 - item 1 = diff. NOTE: this does not consider the change from nothing to inital.
        # so TECHNICALLY one can have the greatest increase on day one, and this program won't find it.
        #but then its not really definitionally pandemic... so...
        #fun fact: there ARE negative differences, which is weird. the cases values are cumulative, so theoretically it should be impossible
        # Current hypothesis: misreported values are retracted at a later date
        #The biggest negative is -5, so I'm going to assume someone thought there was a group that was sick, but they weren't in such situ.


        holdthis = all_cases[count + 1] - all_cases[count]
        difference_of_cases.append(holdthis)
        count = count + 1
        

    #these variable names are getting a bit excessive
    #take the biggest difference, and find its position, and use that to find the
    #  date
    biggest_difference_of_cases = max(difference_of_cases)
    #use the custom def to get all the dates for this county
    all_dates = getdatelist(data)
    #find the date by indexing the biggest -1 one, since the difference calculation will result in a forward shift of +1.
    biggest_difference_of_cases_date = all_dates[(difference_of_cases.index(biggest_difference_of_cases)) - 1]
        

    print("Biggest increase of COVID cases for " + str(county) + ", " + str(state) + " is " + str(biggest_difference_of_cases) + " on " + str(biggest_difference_of_cases_date) + ".")
    
    #actually return the value, for potential later use
    return biggest_difference_of_cases

#this is just a matter of iterating over *seven* values, grabbing the average, and seeing where the average is worst
#the time will be marked as the first day that leads the seven days of woe.
#probably could make a function that does the things that Q2 and Q3 do (unpacking and stuff) too for less code lines.
def third_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal. #good point to specify.
    :return:
    """
    # your code here

    #similar stuff to above (probably a sign I should be making a def for this too... wait...)
    lines = data
    count = 0
    all_cases = list()

    #set a limit to counting
    while count < len(lines):

        #unpack
        line = (lines[count])
        (date, county, state, fips, cases, deaths) = line
        count = count + 1
        all_cases.append(cases)

    #begin loop two = checking for our maximum increase where we assume that its probably not the beginning
    count = 0
    holdthis = list()
    difference_of_average_cases = list()

    #subtracting six since I can't have it go over bound, and it needs to cover the starter number plus six above it.
    while count < len(all_cases) - 6:
       #substracting the number above the base value. six jumps bring 0 to 6, which covers a range of 7, but it still feels wrong.
       #potentially am, might need a checkback here.
       #basically we're reading the day which is followed by another six days
        holdthis = all_cases[count + 6] - all_cases[count]
        difference_of_average_cases.append(holdthis)
        count = count + 1
    #print(difference_of_average_cases)
    biggest_average_of_cases = (max(difference_of_average_cases))
    #print(biggest_average_of_cases)

    all_dates = getdatelist(data)

    begin_the_week_of_woe = all_dates[(difference_of_average_cases.index(biggest_average_of_cases)) - 6]

    print("The worst week of COVID for humans starts at " + str(begin_the_week_of_woe) + " with a total increase of " + str(biggest_average_of_cases) + " cases over that week.")
    if begin_the_week_of_woe == "2022-01-01" or "2022-01-02" or "2022-01-03":
        print("(Lo and behold, the cost of new years celebrations...)")
    return 

#if in the future, more loops could improve versality of this section e.g for the stow reading
if __name__ == "__main__":
    #prepare stow locations
    Location1_stow = parse_nyt_data_for_location(Location1,'us-counties.csv')
    Location2_stow = parse_nyt_data_for_location(Location2,'us-counties.csv')

    print("")
    #This section is noisy and I don't think it helps with answering things (unless one can read really fast),
    # so I'm silencing it.
    """
    for (date,county, state, fips, cases, deaths) in data:
         #CO this line because I don't care for these statements, even if it looks cool in terminal.
         print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')
        count = count + 1
        print(str(count) + ": " + str(data))
    """

    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(Location1_stow)
    first_question(Location2_stow)
    print()

    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(Location1_stow)
    second_question(Location2_stow)
    print()

    # write code to address the following question: Use print() to display your responses.
    # What was the worst seven day period in Harrisonburg for new COVID cases (in terms of absolute number of cases)?
    # What was the worst seven day period in Rockingham County for new COVID cases (in terms of absolute number of cases)?
    third_question(Location1_stow)
    third_question(Location2_stow)

#I will admit I have not reread all the comments before submission: I am very tired at this point.
#This was a very interesting excercise, and the applicability is quite neat.
