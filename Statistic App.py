import tkinter
from tkinter import *
import statistics
from tkinter import messagebox
import os
os.system("pip install scipy")
os. system("pip install numpy")
import numpy 
import numpy as np
import scipy.stats
from scipy.stats import kurtosis
from scipy.stats import skew

window =Tk()
window.title("Petasco Statistics Calculator App")
window.geometry('1200x820+250+50')
window.configure(bg='gold')


# ------------------------------------- Labels -------------------------------------------------------------------
#lbl1 = Label(window, text="===== ==========> GROUP 5 200L <==============", font=('algeria',30, 'bold'),bg='gold', fg="blue", padx=10, pady=25)
#lbl1.place(y=1, x=100)

lbl2 = Label(window, text="============>[ PRESENTATION ]<===========", font=('blue',20, 'bold'),bg='gold' ,fg="red")
lbl2.place(y=70, x=300)
lbl3 = Label(window, text="=============>[ ON ]<===========", font=('blue',20, 'bold'),bg='gold' ,fg="red")
lbl3.place(y=100, x=400)
lbl4 = Label(window, text="=>[ Probability & Statictics ]<=", font=('blue',20, 'bold'), bg='gold',fg="red")
lbl4.place(y=130, x=450)
lbl5 = Label(window, text="[ Enter a Comma Separated Values ]", font=('blue',13, 'bold'), fg="blue")
lbl5.place(y=170, x=480)


#data = IntVar()
data = StringVar()

# --------------------------------- User Input/ Entry Field ---------------------------------------------
entry1 = Entry(window, width=70,textvariable=data ,highlightcolor='blue', font=('black', 13, 'bold'), bd=23 ,insertwidth=2 )
entry1.focus_set()
entry1.place(y=190, x=330)



def clearbtn():
    global operator
    operator = ""
    data.set('')

# --------------------------------- Clear Button -----------------------------------------------------------
clear_btn = Button(window, text='Clear', command=clearbtn, font=('times', 12, 'bold'), width=10)
clear_btn.place(y=260, x=600)

# -----------------------------------------------------output function ------------------------------------------------
def output():
    global empty_lbl
    empty_lbl.config(text='VALUES:  '+ entry1.get())
    entry = entry1.get().split(',')
    data_values = []
    for x in entry:
        data_values.append(int(x))
    #print(data_values)
    mean = statistics.mean(data_values).__round__(5)

    median = statistics.median(data_values)
    #mode = statistics.mode(data_values)
    stand_dev = statistics.stdev(data_values).__round__(5)
    variance = statistics.variance(data_values).__round__(5)

    #========================================= Quartiles ====================================
    '''quart_25 = np.quantile(data_values, 25)
    quart_50 = np.quantile(data_values, 50)
    quart_75 = np.quantile(data_values, 75)'''
    #quart_100 = np.quantile(data_values, 100)
    # ================================= Percentiles ===============================
    percen_25 = np.percentile(data_values,25)
    percen_50 = np.percentile(data_values, 50)
    percen_75 = np.percentile(data_values, 75)
    percen_100 = np.percentile(data_values, 100)



    # --------------------------------------  The Mean function ---------------------------------------------
    def meanfunction():
        global mean_lbl
        mean_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        mean_lbl.place(y=323, x=200)
        mean_lbl.config(text='THE MEAN IS: ' + str(mean))

    # ---------------------------------------MEAN BUTTON -----------------------------------------------------
    mean_btn = Button(window, text='Mean', command=meanfunction, font=('times', 12, 'bold'), width=12, pady=5,padx=10)
    mean_btn.place(y=320, x=50)

    '''def modef():
        global mode_lbl
        Mode = statistics.mode(data_values)
        myset = set(data_values)
        if len(data_values) != len(myset):
            lbl_m = Label(window,fg='green', font=('Arial', 15, 'bold'))
            lbl_m.place(y=368, x=200)
            lbl_m.config(text='MODE IS ' + str(Mode))
            
        else:
            lbl_nm = Label(window, fg='green', font=('Arial', 15, 'bold'))
            lbl_nm.place(y=368, x=200)
            lbl_nm.config(text='NO MODE!')'''
    #modef()

    def modef():
        global mode_lbl
        from statistics import multimode
        Mode = statistics.mode(data_values)
        Mode =statistics.multimode(data_values)
        myset = set(data_values)
        try:
            if len(data_values) != len(myset):
                lbl_m = Label(window, fg='green', font=('Arial', 15, 'bold'))
                lbl_m.place(y=368, x=200)
                lbl_m.config(text='MODE IS ' + str(Mode))

            else:
                lbl_nm = Label(window, fg='green', font=('Arial', 15, 'bold'))
                lbl_nm.place(y=368, x=200)
                lbl_nm.config(text='NO MODE!')
        except:
            from statistics import multimode
            mm = multimode(data_values)
            lbl_mm = Label(window, fg='green', font=('Arial', 15, 'bold'))
            lbl_mm.place(y=368, x=200)
            lbl_mm.config(text='MULTI MODE!' + str(mm))




    '''def modefunc():
        global mode_lbl
        #mode = scipy.stats.mode(data_values)

        mode_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        mode_lbl.place(y=368, x=200)
        mode_lbl.config(text='THE MODE IS: ' + str(mode))'''



    # --------------------------------------MODE BUTTON ------------------------------------------------------------
    mode_btn = Button(window, text='Mode',command=modef,font=('times', 12, 'bold'), width=12,pady=5,padx=10)
    mode_btn.place(y=365, x=50)

    def medianfunc():
        global median_lbl
        median_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        median_lbl.place(y=413, x=200)
        median_lbl.config(text='THE MEDIAN IS: ' + str(median))
    # ------------------------------------ MEDIAN BUTTON ------------------------------------------------------------
    median_btn = Button(window, text='Median',command=medianfunc ,font=('times', 12, 'bold'), width=12,pady=5,padx=10)
    median_btn.place(y=410, x=50)

    def mean_dev_func():
        global mean_dev_lbl
        #list = []
        mean_dev = mean
        list = [abs(loop - mean_dev) for loop in data_values]
        #print(list)
        mean_Dev = sum(list)/len(list)
        mean_dev_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        mean_dev_lbl.place(y=548, x=200)
        mean_dev_lbl.config(text='MEAN DEVIATION: ' + str(mean_Dev))
    # ------------------------------------ Mean Deviation BUTTON ------------------------------------------------------------
    mean_dev_btn = Button(window, text='Mean Deviation',command=mean_dev_func ,font=('times', 12, 'bold') ,width=12,pady=5,padx=10)
    mean_dev_btn.place(y=545, x=50)

    def st_func():
        global st_dev_lbl
        st_dev_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        st_dev_lbl.place(y=458, x=200)
        st_dev_lbl.config(text='STANDARD DEVIATION: ' + str(stand_dev))
    # ------------------------------------ Standard Deviation BUTTON ------------------------------------------------------------
    st_dev_btn = Button(window, text='Standard Deviation',command=st_func ,font=('times', 12, 'bold') ,width=12,pady=5,padx=10)
    st_dev_btn.place(y=455, x=50)

    def var_func():
        global var_lbl
        var_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        var_lbl.place(y=503, x=200)
        var_lbl.config(text='THE VARIANCE IS: ' + str(variance))
    # ------------------------------------ Variance BUTTON ------------------------------------------------------------
    var_btn = Button(window, text='Variance',command=var_func ,font=('times', 12, 'bold'), width=12,pady=5,padx=10)
    var_btn.place(y=500, x=50)

    # ---------------------------------------------------Kurtosis ----------------------------------------------------------------------
    def kurto_func():
        global kurto_lbl
        from scipy.stats import kurtosis
        kurtos = float(kurtosis(data_values)).__round__(5)
        kurto_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        kurto_lbl.place(y=593, x=200)
        kurto_lbl.config(text='THE KURTOSIS IS: ' + str(kurtos))
    # ------------------------------------ Kurtosis BUTTON ------------------------------------------------------------
    kurto_btn = Button(window, text='Kurtosis',command=kurto_func ,font=('times', 12, 'bold'), width=12,pady=5,padx=10)
    kurto_btn.place(y=590, x=50)

    # ------------------------------------------- Skewness -----------------------------------------------------
    def skew_func():
        global skewness_lbl
        from scipy.stats import skew
        skewness = float(skew(data_values, axis=0)).__round__(5)
        skewness_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        skewness_lbl.place(y=638, x=200)
        skewness_lbl.config(text='THE SKEWNESS IS: ' + str(skewness))
    # ------------------------------------ Skewness BUTTON ------------------------------------------------------------
    skewness_btn = Button(window, text='Skewness',command=skew_func ,font=('times', 12, 'bold'), width=12,pady=5,padx=10)
    skewness_btn.place(y=635, x=50)



# ------------------------------------ Quartiles BUTTON ------------------------------------------------------------
    def quart25_func():
        global quar_lbl
        quart_25 = np.quantile(data_values, 0.25)
        quar_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        quar_lbl.place(y=328, x=740)
        quar_lbl.config(text='THE QUARTILES IS: ' + str(quart_25))
    quar_btn = Button(window, text='25TH Quartiles',command=quart25_func ,font=('times', 12, 'bold'), width=12,pady=5,padx=10)
    quar_btn.place(y=325, x=600)



    def quart50_func():
        global quart_50_lbl
        quart_50 = np.quantile(data_values, 0.50)
        quart_50_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        quart_50_lbl.place(y=373, x=740)
        quart_50_lbl.config(text='THE QUARTILES IS: ' + str(quart_50))

    quart_50_btn = Button(window, text='50TH Quartiles', command=quart50_func, font=('times', 12, 'bold'), width=12, pady=5,padx=10)
    quart_50_btn.place(y=370, x=600)

    def quart75_func():
        global quart_75_lbl
        quart_75 = numpy.quantile(data_values, 0.75)
        quart_75_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        quart_75_lbl.place(y=418, x=740)
        quart_75_lbl.config(text='THE QUARTILES IS: ' + str(quart_75))

    quar75_btn = Button(window, text='75TH Quartiles', command=quart75_func, font=('times', 12, 'bold'), width=12, pady=5,padx=10)
    quar75_btn.place(y=415, x=600)

    def quart100_func():
        global quart_100_lbl
        quart_100 = numpy.quantile(data_values,1)
        quart_100_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        quart_100_lbl.place(y=463, x=740)
        quart_100_lbl.config(text='THE QUARTILES IS: ' + str(quart_100))

    quar100_btn = Button(window, text='100TH Quartiles', command=quart100_func, font=('times', 12, 'bold'), width=12, pady=5,padx=10)
    quar100_btn.place(y=460, x=600)

#----------------------------------- inter quartile ---------------------------------------------------
    def interq_func():
        global interquart_lbl
        from scipy.stats import skew
        Q3 = np.quantile(data_values, 0.75)
        Q1 = np.quantile(data_values, 0.25)
        interquartile = float(Q3-Q1 ).__round__(5)
        interquart_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        interquart_lbl.place(y=688, x=200)
        interquart_lbl.config(text='THE INTER QUARTILE IS: ' + str(interquartile))
    # ------------------------------------ inter quartile BUTTON ------------------------------------------------------------
    interquart_btn = Button(window, text='Inter Quartile',command=interq_func ,font=('times', 12, 'bold'), width=12,pady=5,padx=10)
    interquart_btn.place(y=685, x=50)


# ---------------------------------- Semi Quartile -----------------------------------------
    def semi_q_func():
        global semi_quart_lbl
        from scipy.stats import skew
        Q3 = np.quantile(data_values, 0.75)
        Q1 = np.quantile(data_values, 0.25)
        semi_quartile = float((Q3-Q1 )/2).__round__(5)
        semi_quart_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        semi_quart_lbl.place(y=688, x=740)
        semi_quart_lbl.config(text='THE SEMI QUARTILE IS: ' + str(semi_quartile))
    # ------------------------------------ Semi Quartile BUTTON ------------------------------------------------------------
    semi_quart_btn = Button(window, text='Semi-Quartile',command=semi_q_func ,font=('times', 12, 'bold'), width=12,pady=5,padx=10)
    semi_quart_btn.place(y=685, x=600)

    def percentiles():
        global percent_lbl
        percent_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        percent_lbl.place(y=508, x=740)
        percent_lbl.config(text='The 25th Percentile is ' + str(percen_25))

    percent_btn = Button(window, text='25th Percentile', command=percentiles, font=('times', 12, 'bold'), width=12, pady=5,padx=10)
    percent_btn.place(y=505, x=600)


    def percentiles_50():
        global percent_50_lbl
        percent_50_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        percent_50_lbl.place(y=553, x=740)
        percent_50_lbl.config(text='The 50th Percentile is ' + str(percen_50))

    percent_btn = Button(window, text='50th Percentile', command=percentiles_50, font=('times', 12, 'bold'), width=12, pady=5,padx=10)
    percent_btn.place(y=550, x=600)

    def percentiles_75():
        global percent_75_lbl
        percent_75_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        percent_75_lbl.place(y=598, x=740)
        percent_75_lbl.config(text='The 75th Percentile is ' + str(percen_75))

    percent_btn = Button(window, text='75th Percentile', command=percentiles_75, font=('times', 12, 'bold'), width=12, pady=5,padx=10)
    percent_btn.place(y=595, x=600)

    def percentiles_100():
        global percent_100_lbl
        percent_100_lbl = Label(window, fg='green', font=('Arial', 15, 'bold'))
        percent_100_lbl.place(y=643, x=740)
        percent_100_lbl.config(text='The 100th Percentile is ' + str(percen_100))

    percent_btn = Button(window, text='100th Percentile', command=percentiles_100, font=('times', 12, 'bold'), width=12, pady=5,padx=10)
    percent_btn.place(y=640, x=600)

    def reset():
        empty_lbl.destroy()
        mean_lbl.destroy()
        mode_lbl.destroy()
        median_lbl.destroy()
        st_dev_lbl.destroy()
        mean_dev_lbl.destroy()
        var_lbl.destroy()
        kurto_lbl.destroy()
        skewness_lbl.destroy()
        quar_lbl.destroy()
        quart_50_lbl.destroy()
        quart_75_lbl.destroy()
        quart_100_lbl.destroy()
        interquart_lbl.destroy()
        semi_quart_lbl.destroy()
        percent_lbl.destroy()
        percent_50_lbl.destroy()
        percent_75_lbl.destroy()
        percent_100_lbl.destroy()
    # ---------------------------------Reset Button ---------------------------------------------------------------

    reset_btn = Button(window, text='Reset', command=reset, font=('times', 12, 'bold'), width=10)
    reset_btn.place(y=260, x=800)

# ----------------------------- Submit Button --------------------------------------------------------------
submit_btn = Button(window, text='Submit',command=output ,font=('times', 12, 'bold'), width=10)
submit_btn.place(y=260, x=400)

def error():
    entry2 = entry1
    if not entry2:
        messagebox.showerror('Error!', 'OOPs')
    else:
        pass
error()
#entry1.bind('<Return>', output)

#------------------------------------- User Input Output -------------------------------------------------
empty_lbl = Label(window,fg='red', font=('Arial',15, 'bold'),bg='gold')
empty_lbl.place(y=300, x=400)


window.resizable(False, False)
window.mainloop()
