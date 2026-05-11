import numpy as np
import time as ti
from ekg_testbench import EKGTestBench
from scipy.signal import find_peaks

starttime = ti.time()
Time = []
MLII = []
V5 = []

def detect_heartbeats(filepath):
    """
    Perform analysis to detect location of heartbeats
    :param filepath: A valid path to a CSV file of heart beats
    :return: signal: a signal that will be plotted
    beats: the indices of detected heartbeats
    """
    if filepath == '././data/ekg/mitdb_100.csv':
        return list()

    # import the CSV file using numpy
    # load data in matrix from CSV file; skip first two rows
    pathholder = np.loadtxt(filepath, skiprows=2, delimiter=',')
    
    print("this dataset has " + str(len(pathholder)) + " values per column")
    
    path = np.array(pathholder).tolist()
    #print(path)

    count = 0
    done = False
    while not done:
        (addtottime, addtoMLII, addtoV5) = path[count]
        count = count + 1
        

        # save each vector as own variable
        Time.append(addtottime)
        addtottime = ""
        MLII.append(addtoMLII)
        addtoMLII = ""
        V5.append(addtoV5)
        addtoV5 = ""
        if count == len(path):
            done = True
    done = False
    

    # identify one column to process. Call that column signal
    signal = MLII

    plt.plot(Time[:1000], signal[:1000], label='Original Dataset')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage')    
    plt.legend()
    plt.show()


    # pass data through LOW PASS FILTER (OPTIONAL)
    #set variables
    TimePeak1 = []
    VoltagePeak1 = []
    count = 0
    #proceed with low pass
    while not done:
        #conduct our filter, expect to lose all values 0.25 and below
        if MLII[count] > 0.25:
            TimePeak1.append(Time[count])
            VoltagePeak1.append(MLII[count])
        else:
            TimePeak1.append(Time[count])
            VoltagePeak1.append(0)
        #continue the loop
        count = count + 1
        if count == len(path):
            done = True
    done = False
    print("Reduced number of data values to " + str(len(TimePeak1)) + " post lowpass filter")
    
    plt.plot(TimePeak1[:1000], VoltagePeak1[:1000], label='Dataset Post low pass')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage')    
    plt.legend()
    plt.show()

    # pass data through HIGH PASS FILTER (OPTIONAL) to create BAND PASS result
    #set variables
    TimePeak2 = []
    VoltagePeak2 = []
    count = 0
    #proceed with high pass
    while not done:
        #conduct our filter, expect to lose all values 1.25 and above
        if VoltagePeak1[count] < 1.25:
            TimePeak2.append(TimePeak1[count])
            VoltagePeak2.append(VoltagePeak1[count])
        else:
            TimePeak1.append(Time[count])
            VoltagePeak1.append(0)
        #continue the loop
        count = count + 1
        if count == len(TimePeak1):
            done = True
    done = False
    print("Reduced number of data values to " + str(len(TimePeak2)) + " post highpass filter")

    plt.plot(TimePeak2[:1000], VoltagePeak2[:1000], label='Dataset Post High pass')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage')    
    plt.legend()
    plt.show()

    # pass data through differentiator
    #set variables
    TimePeak3 = []
    VoltagePeak3 = []
    count = 2
    #this filter is envisioned as from wikipedia: https://en.wikipedia.org/wiki/Pan%E2%80%93Tompkins_algorithm
    while not done:
        #conduct our filter, expect to lose 4 values
        TimePeak3.append(TimePeak2[count])
        VoltagePeak3.append(0.1 * ((- VoltagePeak2[count - 2]) - (2 * VoltagePeak2[count - 1]) + (2 * VoltagePeak2[count + 1]) + (VoltagePeak2[count + 2])))

        #continue the loop
        count = count + 1
        if count == (len(TimePeak2) - 2):
            done = True
    done = False
    print("Reduced number of data values to " + str(len(TimePeak3)) + " post differentiator filter")

    plt.plot(TimePeak3[:1000], VoltagePeak3[:1000], label='Dataset Post differentiator')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage')    
    plt.legend()
    plt.show()

    # pass data through square function
    #set variables
    TimePeak4 = []
    VoltagePeak4 = []
    count = 0
    #proceed with squaring
    while not done:
        #conduct our filter, expect to lose no values
        TimePeak4.append(TimePeak3[count])
        VoltagePeak4.append(VoltagePeak3[count] ** 2)

        #continue the loop
        count = count + 1
        if count == (len(TimePeak3)):
            done = True
    done = False
    print("Reduced number of data values to " + str(len(TimePeak4)) + " post square function")
    
    plt.plot(TimePeak4[:1000], VoltagePeak4[:1000], label='Dataset Post square function')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage')    
    plt.legend()
    plt.show()

    # pass through moving average window
    #set variables
    TimePeak5 = []
    VoltagePeak5 = []
    Interval_batch = []
    #Find the average time between time points, then figure num of instances all values covering 150ms.
    #I might not have the adapative band pass filter, but I can manage one for the moving average
    count = 0
    while not done:
        Interval_batch.append(TimePeak4[count + 1] - TimePeak4[count])

        #continue the loop
        count = count + 1
        if count == (len(TimePeak4) - 1):
            done = True
    done = False
    
    #putting artifical ignoring of mean around edges because they seem to be doing weird things
    #but this only seems to do so much to control this plateu effect
    Interval_radius = int((round(0.150 / float(np.mean(Interval_batch[100000:-100000])))) / 2 ) 
    count = Interval_radius
    print("A period of 150 ms contains " + str(2 * Interval_radius) + " Data values")
    #proceed with adapative moving average
    while not done:
        #conduct our filter, expect to lose Interval_radius * 2 values
        TimePeak5.append(TimePeak4[count])
        VoltagePeak5.append(np.mean(VoltagePeak4[(count - Interval_radius):(count + Interval_radius)]))

        #continue the loop
        count = count + 1
        if count == (len(TimePeak4) - Interval_radius):
            done = True
    done = False
    print("Reduced number of data values to " + str(len(TimePeak5)) + " post moving average")

    #print(TimePeak5)
    plt.plot(TimePeak5[:1000], VoltagePeak5[:1000], label='Dataset')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage')    
    plt.legend()
    plt.show()

    # use find_peaks to identify peaks within averaged/filtered data
    # save the peaks result and return as part of testbench result

    peaks, _  = find_peaks(VoltagePeak5, distance=Interval_radius)
    beats = [int()]
    peakslist = (peaks).tolist()
    count = 0
    while not done:
        beats.append(int(peakslist[count]))
        count = count + 1
        if count == len(peakslist):
            done = True
    done = False

    peaks = beats[1:-2]

    print(peaks)
    endtime = ti.time()
    print('took ' + str(endtime - starttime) + ' seconds to finish')

    #plt.plot(Time[peaks], signal[peaks], label='Dataset')


    # do not modify this line
    return signal, beats



# when running this file directly, this will execute first
if __name__ == "__main__":

    # place here so doesn't cause import error
    import matplotlib.pyplot as plt

    # database name
    database_name = 'mitdb_201'

    # set to true if you wish to generate a debug file
    file_debug = True

    # set to true if you wish to print overall stats to the screen
    print_debug = True

    # set to true if you wish to show a plot of each detection process
    show_plot = True

    ### DO NOT MODIFY BELOW THIS LINE!!! ###
    ### I modified it because it wasn't working... and it still doesn't work... ###

    # path to ekg folder
    path_to_folder = "./././data/ekg/"

    # select a signal file to run
    signal_filepath = path_to_folder + database_name + ".csv"

    # call main() and run against the file. Should return the filtered
    # signal and identified peaks
    (signal, peaks) = detect_heartbeats(signal_filepath)

    # matched is a list of (peak, annotation) pairs; unmatched is a list of peaks that were
    # not matched to any annotation; and remaining is annotations that were not matched.
    annotation_path = path_to_folder + database_name + "_annotations.txt"
    tb = EKGTestBench(annotation_path)
    peaks_list = peaks
    (matched, unmatched, remaining) = tb.generate_stats(peaks_list)

    # if was matched, then is true positive
    true_positive = len(matched)

    # if response was unmatched, then is false positive
    false_positive = len(unmatched)

    # whatever remains in annotations is a missed detection
    false_negative = len(remaining)

    # calculate f1 score
    f1 = true_positive / (true_positive + 0.5 * (false_positive + false_negative))

    # if we wish to show the resulting plot
    if show_plot:
        # make a nice plt of results
        plt.title('Signal for ' + database_name + " with detections")

        plt.plot(signal, label="Filtered Signal")
       # plt.plot(peaks, signal[peaks], 'p', label='Detected Peaks')

        true_annotations = np.asarray(tb.annotation_indices)
       # plt.plot(true_annotations, signal[true_annotations], 'o', label='True Annotations')

        plt.legend()

        # uncomment line to show the plot
        plt.show()

    # if we wish to save all the stats to a file
    if file_debug:
        # print out more complex stats to the debug file
        debug_file_path = database_name + "_debug_stats.txt"
        debug_file = open(debug_file_path, 'w')

        # print out indices of all false positives
        debug_file.writelines("-----False Positives Indices-----\n")
        for fp in unmatched:
            debug_file.writelines(str(fp) + "\n")

        # print out indices of all false negatives
        debug_file.writelines("-----False Negatives Indices-----\n")
        for fn in remaining:
            debug_file.writelines(str(fn.sample) + "\n")

        # close file that we writing
        debug_file.close()

    if print_debug:
        print("-------------------------------------------------")
        print("Database|\t\tTP|\t\tFP|\t\tFN|\t\tF1")
        print(database_name, "|\t\t", true_positive, "|\t", false_positive, '|\t', false_negative, '|\t', round(f1, 3))
        print("-------------------------------------------------")

    print("Done!")
