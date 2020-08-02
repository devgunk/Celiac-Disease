from tkinter import *
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
root = Tk()
ap=ctrl.Antecedent(np.arange(0,11,1),'ap')
an=ctrl.Antecedent(np.arange(0,11,1),'an')
da=ctrl.Antecedent(np.arange(0,11,1),'da')
vom=ctrl.Antecedent(np.arange(0,11,1),'vom')
wl=ctrl.Antecedent(np.arange(0,11,1),'wl')
bmi = ctrl.Antecedent(np.arange(0, 41, 1), 'bmi')
cd = ctrl.Consequent(np.arange(0, 101, 1), 'cd')
ap['Mild']=fuzz.trimf(ap.universe,[0,0,4])
ap['Mod']=fuzz.trimf(ap.universe,[1,5,9])
ap['Sev']=fuzz.trimf(ap.universe,[6,10,10])
an['Mild']=fuzz.trimf(an.universe,[0,0,4])
an['Mod']=fuzz.trimf(an.universe,[1,5,9])
an['Sev']=fuzz.trimf(an.universe,[6,10,10])
da['Mild']=fuzz.trimf(da.universe,[0,0,4])
da['Mod']=fuzz.trimf(da.universe,[1,5,9])
da['Sev']=fuzz.trimf(da.universe,[6,10,10])
vom['OnceWeek']=fuzz.trimf(vom.universe,[0,0,4])
vom['ThriceWeek']=fuzz.trimf(vom.universe,[1,5,9])
vom['Daily']=fuzz.trimf(vom.universe,[6,10,10])
wl['US']=fuzz.trimf(wl.universe,[0,0,4])
wl['UL']=fuzz.trimf(wl.universe,[2,10,10])
bmi['UW'] = fuzz.trimf(bmi.universe, [0,0,22])
bmi['Normal'] = fuzz.trimf(bmi.universe, [15,22,29])
bmi['OW'] = fuzz.trimf(bmi.universe, [22,40,40])
cd['NCD'] = fuzz.trimf(cd.universe, [0, 0, 1])
cd['EL'] = fuzz.trimf(cd.universe, [0, 10, 20])
cd['VVL'] = fuzz.trimf(cd.universe, [10,20,30])
cd['VL'] = fuzz.trimf(cd.universe, [20,30,40])
cd['L'] = fuzz.trimf(cd.universe, [30,40,50])
cd['ML'] = fuzz.trimf(cd.universe, [40,50,60])
cd['M'] = fuzz.trimf(cd.universe, [50,60,70])
cd['MH'] = fuzz.trimf(cd.universe, [60,70,80])
cd['H'] = fuzz.trimf(cd.universe, [70,80,90])
cd['VH'] = fuzz.trimf(cd.universe, [80,90,100])
cd['VVH'] = fuzz.trimf(cd.universe, [90,100,100])
def Check():
    flag_chk = 0
    global Abdominal_Pain_var, Abdominal_Pain_entry, Anemia_var, Anemia_entry, Diarihea_var, Diarihea_entry,  Vomiting_var, Vomiting_entry, Weight_Loss_var, Weight_Loss_entry
    Abdominal_Pain_value = str(Abdominal_Pain_var.get())
    Abdominal_Pain_value = Abdominal_Pain_value.strip()
    Abdominal_Pain_value = Abdominal_Pain_value.replace(" ", "")
    try:
        Flag_Abdominal_Pain = 0
        if Abdominal_Pain_value == '':
            Flag_Abdominal_Pain = 1
        else:
            Abdominal_Pain_error_label = Label(root, fg='red', text='                                                         ', font=("Helvetica", 10)).grid(rowspan=1, row=3, column=3)
            Abdominal_Pain_value = float(Abdominal_Pain_value)
            if Abdominal_Pain_value < 0:
                Abdominal_Pain_entry.delete(0, END)
                Abdominal_Pain_entry.insert(END, 0.000)
                Abdominal_Pain_Scale.set(0)
                Flag_Abdominal_Pain = 1
            elif Abdominal_Pain_value > 10:
                Abdominal_Pain_entry.delete(0, END)
                Abdominal_Pain_entry.insert(END, 10.000)
                Abdominal_Pain_Scale.set(10)
                Flag_Abdominal_Pain = 1
        if Flag_Abdominal_Pain == 1:
            Abdominal_Pain_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=3, column=3)
            flag_chk = 1
    except:
        Abdominal_Pain_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=3, column=3)
        flag_chk = 1
    Anemia_value = str(Anemia_var.get())
    Anemia_value = Anemia_value.strip()
    Anemia_value = Anemia_value.replace(" ", "")
    try:
        Flag_Anemia = 0
        if Anemia_value == '':
            Flag_Anemia = 1
        else:
            Anemia_error_label = Label(root, fg='red', text='                                                         ', font=("Helvetica", 10)).grid(rowspan=1, row=5, column=3)
            Anemia_value = float(Anemia_value)
            if  Anemia_value < 0:
                Anemia_entry.delete(0, END)
                Anemia_entry.insert(END, 0.000)
                Anemia_Scale.set(0)
                Flag_Anemia = 1
            elif Anemia_value > 10:
                Anemia_entry.delete(0, END)
                Anemia_entry.insert(END, 10.000)
                Anemia_Scale.set(10)
                Flag_Anemia = 1
        if Flag_Anemia == 1:
            Anemia_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=5, column=3)
            flag_chk = 1
    except:
        Anemia_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=5, column=3)
        flag_chk = 1
    Diarihea_value = str(Diarihea_var.get())
    Diarihea_value = Diarihea_value.strip()
    Diarihea_value = Diarihea_value.replace(" ", "")
    try:
        Flag_Diarihea = 0
        if Diarihea_value == '':
            Flag_Diarihea = 1
        else:
            Diarihea_error_label = Label(root, fg='red', text='                                                         ', font=("Helvetica", 10)).grid(rowspan=1, row=7, column=3)
            Diarihea_value = float(Diarihea_value)
            if  Diarihea_value < 0:
                Diarihea_entry.delete(0, END)
                Diarihea_entry.insert(END, 0.000)
                Diarihea_Scale.set(0)
                Flag_Diarihea = 1
            elif Diarihea_value > 10:
                Diarihea_entry.delete(0, END)
                Diarihea_entry.insert(END, 10.000)
                Diarihea_Scale.set(10)
                Flag_Diarihea = 1
        if Flag_Diarihea == 1:
            Diarihea_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=7, column=3)
            flag_chk = 1
    except:
        Diarihea_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=7, column=3)
        flag_chk = 1
    Vomiting_value = str(Vomiting_var.get())
    Vomiting_value = Vomiting_value.strip()
    Vomiting_value = Vomiting_value.replace(" ", "")
    try:
        Flag_Vomiting = 0
        if Vomiting_value == '':
            Flag_Vomiting = 1
        else:
            Vomiting_error_label = Label(root, fg='red', text='                                                         ', font=("Helvetica", 10)).grid(rowspan=1, row=9, column=3)
            Vomiting_value = float(Vomiting_value)
            if Vomiting_value < 0:
                Vomiting_entry.delete(0, END)
                Vomiting_entry.insert(END, 0.000)
                Vomiting_Scale.set(0)
                Flag_Vomiting = 1
            elif Vomiting_value > 10:
                Vomiting_entry.delete(0, END)
                Vomiting_entry.insert(END, 10.000)
                Vomiting_Scale.set(10)
                Flag_Vomiting = 1
        if Flag_Vomiting == 1:
            Vomiting_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=9, column=3)
            flag_chk = 1
    except:
        Vomiting_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=9, column=3)
        flag_chk = 1
    Weight_Loss_value = str(Weight_Loss_var.get())
    Weight_Loss_value = Weight_Loss_value.strip()
    Weight_Loss_value = Weight_Loss_value.replace(" ", "")
    try:
        Flag_Weight_Loss = 0
        if Weight_Loss_value == '':
            Flag_Weight_Loss = 1
        else:
            Weight_Loss_error_label = Label(root, fg='red', text='                                                         ', font=("Helvetica", 10)).grid(rowspan=1, row=11, column=3)
            Weight_Loss_value = float(Weight_Loss_value)
            if Weight_Loss_value < 0:
                Weight_Loss_entry.delete(0, END)
                Weight_Loss_entry.insert(END, 0.000)
                Weight_Loss_Scale.set(0)
                Flag_Weight_Loss = 1
            elif Weight_Loss_value > 10:
                Weight_Loss_entry.delete(0, END)
                Weight_Loss_entry.insert(END, 10.000)
                Weight_Loss_Scale.set(10)
                Flag_Weight_Loss = 1
        if Flag_Weight_Loss == 1:
            Weight_Loss_error_label = Label(root, fg='red', text='Please enter (some / valid) value.',  font=("Helvetica", 10)).grid(rowspan=1, row=11, column=3)
            flag_chk = 1
    except:
        Weight_Loss_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=11, column=3)
        flag_chk = 1
    BMI_value = str(BMI_var.get())
    BMI_value = BMI_value.strip()
    BMI_value = BMI_value.replace(" ", "")
    try:
        Flag_BMI = 0
        if BMI_value == '':
            Flag_BMI = 1
        else:
            BMI_error_label = Label(root, fg='red', text='                                                         ', font=("Helvetica", 10)).grid(rowspan=1, row=13, column=3)
            BMI_value = float(BMI_value)
            if BMI_value < 0:
                BMI_entry.delete(0, END)
                BMI_entry.insert(END, 0.000)
                BMI_Scale.set(0)
                Flag_BMI = 1
            elif BMI_value > 40:
                BMI_entry.delete(0, END)
                BMI_entry.insert(END, 40.000)
                BMI_Scale.set(40)
                Flag_BMI = 1
        if Flag_BMI == 1:
            BMI_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=13, column=3)
            flag_chk = 1
    except:
        BMI_error_label = Label(root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10)).grid(rowspan=1, row=13, column=3)
        flag_chk = 1
    return flag_chk
def Abdominal_Pain_func():
    Check()
    ap.view()
def Anemia_func():
    Check()
    an.view()
def Diarihea_func():
    Check()
    da.view()
def Vomiting_func():
    Check()
    vom.view()
def Weight_Loss_func():
    Check()
    wl.view()
def BIM_func():
    Check()
    bmi.view()
def Result(result):
    result_root = Tk()
    result_root.title("Celiac Disease Probabilistic System")
    Celiac_Disease_Probability_label = Label(result_root, text='Celiac Disease Probability is : ', font=("Helvetica", 15)).grid(
        rowspan=1, row=1, columnspan=2, column=0)
    Celiac_Disease_Probability_label = Label(result_root, text=str(result), font=("Helvetica", 15), width=18).grid(
        rowspan=1, row=1, column=3, columnspan=3)
    Celiac_Disease_Probability_val = float(result)
    space_label = Label(result_root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=2, column=1)
    Recommandation_label = Label(result_root, fg='blue', text='Recommands : ', font=("Helvetica", 15), width=18).grid(
        rowspan=1, row=3, column=0, columnspan=2)
    if Celiac_Disease_Probability_val >= 0 and Celiac_Disease_Probability_val <= 10:
        result_label = Label(result_root, fg='blue', text='Extremely low chance of Celiac Disease',
                             font=("Helvetica", 15)).grid(rowspan=1, row=3, column=2, columnspan=4)
    elif Celiac_Disease_Probability_val > 10 and Celiac_Disease_Probability_val <= 20:
        result_label = Label(result_root, fg='blue', text='Very Very low chance of Celiac Disease',
                             font=("Helvetica", 15)).grid(rowspan=1, row=3, column=2, columnspan=4)
    elif Celiac_Disease_Probability_val > 20 and Celiac_Disease_Probability_val <= 30:
        result_label = Label(result_root, fg='blue', text='Very low chance of Celiac Disease',
                             font=("Helvetica", 15)).grid(rowspan=1, row=3, column=2, columnspan=4)
    elif Celiac_Disease_Probability_val > 30 and Celiac_Disease_Probability_val <= 40:
        result_label = Label(result_root, fg='blue', text='Low chance of Celiac Disease', font=("Helvetica", 15)).grid(
            rowspan=1, row=3, column=2, columnspan=4)
    elif Celiac_Disease_Probability_val > 40 and Celiac_Disease_Probability_val <= 50:
        result_label = Label(result_root, fg='blue', text='Medium chance of Celiac Disease, Go for tTg-IgA test',
                             font=("Helvetica", 15)).grid(rowspan=1, row=3, column=2, columnspan=4)
    elif Celiac_Disease_Probability_val > 50 and Celiac_Disease_Probability_val <= 60:
        result_label = Label(result_root, fg='blue', text='Medium high chance of Celiac Disease, Go for tTg-IgA test',
                             font=("Helvetica", 15)).grid(rowspan=1, row=3, column=2, columnspan=4)
    elif Celiac_Disease_Probability_val > 60 and Celiac_Disease_Probability_val <= 70:
        result_label = Label(result_root, fg='blue', text='High chance of Celiac Disease, Go for tTg-IgA test',
                             font=("Helvetica", 15)).grid(rowspan=1, row=3, column=2, columnspan=4)
    elif Celiac_Disease_Probability_val > 70 and Celiac_Disease_Probability_val <= 80:
        result_label = Label(result_root, fg='blue',
                             text='Very high chance of Celiac Disease, Must go for tTg-IgA test, Biopsy Tests to confirm Celiac Disease',
                             font=("Helvetica", 15)).grid(rowspan=1, row=3, column=2, columnspan=4)
    elif Celiac_Disease_Probability_val > 80:
        result_label = Label(result_root, fg='blue',
                             text='Strong chance of Celiac Disease, Must go for tTg-IgA test, Biopsy Tests to confirm Celiac Disease',
                             font=("Helvetica", 15)).grid(rowspan=1, row=3, column=2, columnspan=4)
def Calculate():
    Check_Flag = Check()
    if Check_Flag == 0:
        global BMI_var, BMI_Scale, Weight_Loss_var, Weight_Loss_Scale, Vomiting_var, Vomiting_Scale, Diarihea_var, Diarihea_Scale, Anemia_var, Anemia_Scale, Abdominal_Pain_var, Abdominal_Pain_Scale
        BMI_value = str(BMI_var.get())
        BMI_value = BMI_value.strip()
        BMI_value = BMI_value.replace(" ", "")
        BMI_value = float(BMI_value)
        BMI_Scale.set(BMI_value)
        Weight_Loss_value = str(Weight_Loss_var.get())
        Weight_Loss_value = Weight_Loss_value.strip()
        Weight_Loss_value = Weight_Loss_value.replace(" ", "")
        Weight_Loss_value = float(Weight_Loss_value)
        Weight_Loss_Scale.set(Weight_Loss_value)
        Vomiting_value = str(Vomiting_var.get())
        Vomiting_value = Vomiting_value.strip()
        Vomiting_value = Vomiting_value.replace(" ", "")
        Vomiting_value = float(Vomiting_value)
        Vomiting_Scale.set(Vomiting_value)
        Diarihea_value = str(Diarihea_var.get())
        Diarihea_value = Diarihea_value.strip()
        Diarihea_value = Diarihea_value.replace(" ", "")
        Diarihea_value = float(Diarihea_value)
        Diarihea_Scale.set(Diarihea_value)
        Anemia_value = str(Anemia_var.get())
        Anemia_value = Anemia_value.strip()
        Anemia_value = Anemia_value.replace(" ", "")
        Anemia_value = float(Anemia_value)
        Anemia_Scale.set(Anemia_value)
        Abdominal_Pain_value = str(Abdominal_Pain_var.get())
        Abdominal_Pain_value = Abdominal_Pain_value.strip()
        Abdominal_Pain_value = Abdominal_Pain_value.replace(" ", "")
        Abdominal_Pain_value = float(Abdominal_Pain_value)
        Abdominal_Pain_Scale.set(Abdominal_Pain_value)
        rule1 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['NCD'])
        rule2 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['NCD'])
        rule3 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['NCD'])
        rule4 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['NCD'])
        rule5 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['NCD'])
        rule6 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['NCD'])
        rule7 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['EL'])
        rule8 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['NCD'])
        rule9 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['EL'])
        rule10 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['VVL'])
        rule11 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'],cd['EL'])
        rule12 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['VVL'])
        rule13 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VVL'])
        rule14 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['EL'])
        rule15 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VVL'])
        rule16 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VL'])
        rule17 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VVL'])
        rule18 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VL'])
        rule19 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['EL'])
        rule20 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['NCD'])
        rule21 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['EL'])
        rule22 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['VVL'])
        rule23 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['EL'])
        rule24 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['VVL'])
        rule25 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['VVL'])
        rule26 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['EL'])
        rule27 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['VVL'])
        rule28 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['VL'])
        rule29 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'],cd['VVL'])
        rule30 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['VL'])
        rule31 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VL'])
        rule32 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['VVL'])
        rule33 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VL'])
        rule34 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['L'])
        rule35 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VL'])
        rule36 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['L'])
        rule37 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['VVL'])
        rule38 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['EL'])
        rule39 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['VVL'])
        rule40 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['VL'])
        rule41 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['VVL'])
        rule42 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['VL'])
        rule43 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['VL'])
        rule44 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'],cd['VVL'])
        rule45 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['VL'])
        rule46 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['L'])
        rule47 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['VL'])
        rule48 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['L'])
        rule49 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['L'])
        rule50 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule51 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['L'])
        rule52 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule53 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule54 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule55 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['VVL'])
        rule56 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['EL'])
        rule57 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['VVL'])
        rule58 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['VL'])
        rule59 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['VVL'])
        rule60 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['VL'])
        rule61 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['VL'])
        rule62 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'],cd['VVL'])
        rule63 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['VL'])
        rule64 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['L'])
        rule65 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['VL'])
        rule66 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['L'])
        rule67 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['L'])
        rule68 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule69 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['L'])
        rule70 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule71 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule72 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule73 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['VL'])
        rule74 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['VVL'])
        rule75 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['VL'])
        rule76 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['L'])
        rule77 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['VL'])
        rule78 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['L'])
        rule79 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['L'])
        rule80 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule81 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['L'])
        rule82 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule83 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule84 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule85 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['ML'])
        rule86 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['L'])
        rule87 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['ML'])
        rule88 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['M'])
        rule89 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['ML'])
        rule90 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['M'])
        rule91 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['L'])
        rule92 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule93 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['L'])
        rule94 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule95 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule96 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule97 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['ML'])
        rule98 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['L'])
        rule99 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['ML'])
        rule100 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['M'])
        rule101 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['ML'])
        rule102 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['M'])
        rule103 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['M'])
        rule104 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule105 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['M'])
        rule106 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule107 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule108 = ctrl.Rule(ap['Mild'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule109 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['L'])
        rule110 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule111 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['L'])
        rule112 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule113 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule114 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule115 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['ML'])
        rule116 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['L'])
        rule117 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['ML'])
        rule118 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['M'])
        rule119 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'],cd['ML'])
        rule120 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['M'])
        rule121 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['M'])
        rule122 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule123 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['M'])
        rule124 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule125 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule126 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule127 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['ML'])
        rule128 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['L'])
        rule129 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['ML'])
        rule130 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['M'])
        rule131 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['ML'])
        rule132 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['M'])
        rule133 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['M'])
        rule134 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule135 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['M'])
        rule136 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule137 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule138 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule139 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['MH'])
        rule140 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['M'])
        rule141 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['MH'])
        rule142 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['H'])
        rule143 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule144 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['H'])
        rule145 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['M'])
        rule146 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule147 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['M'])
        rule148 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule149 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule150 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule151 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['MH'])
        rule152 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['M'])
        rule153 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['MH'])
        rule154 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['H'])
        rule155 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule156 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['H'])
        rule157 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VH'])
        rule158 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['H'])
        rule159 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VH'])
        rule160 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule161 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VH'])
        rule162 = ctrl.Rule(ap['Mild'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule163 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['VVL'])
        rule164 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['EL'])
        rule165 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['VVL'])
        rule166 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['VL'])
        rule167 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['VVL'])
        rule168 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['VL'])
        rule169 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['VL'])
        rule170 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'],cd['VVL'])
        rule171 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['VL'])
        rule172 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['L'])
        rule173 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'],cd['VL'])
        rule174 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['L'])
        rule175 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['L'])
        rule176 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule177 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['L'])
        rule178 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule179 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule180 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule181 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['VL'])
        rule182 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['VVL'])
        rule183 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['VL'])
        rule184 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['L'])
        rule185 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['VL'])
        rule186 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['L'])
        rule187 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['L'])
        rule188 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule189 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['L'])
        rule190 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule191 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule192 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule193 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['ML'])
        rule194 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['L'])
        rule195 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['ML'])
        rule196 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['M'])
        rule197 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['ML'])
        rule198 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['M'])
        rule199 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['L'])
        rule200 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule201 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['L'])
        rule202 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule203 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule204 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule205 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['ML'])
        rule206 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['L'])
        rule207 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['ML'])
        rule208 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['M'])
        rule209 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['ML'])
        rule210 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['M'])
        rule211 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['M'])
        rule212 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule213 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['M'])
        rule214 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule215 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule216 = ctrl.Rule(ap['Mod'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule217 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['L'])
        rule218 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule219 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['L'])
        rule220 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule221 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule222 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule223 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['ML'])
        rule224 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['L'])
        rule225 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['ML'])
        rule226 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['M'])
        rule227 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['ML'])
        rule228 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['M'])
        rule229 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['M'])
        rule230 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule231 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['M'])
        rule232 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule233 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule234 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule235 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['ML'])
        rule236 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['L'])
        rule237 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['ML'])
        rule238 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['M'])
        rule239 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['ML'])
        rule240 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['M'])
        rule241 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['M'])
        rule242 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule243 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['M'])
        rule244 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule245 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule246 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule247 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['MH'])
        rule248 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['M'])
        rule249 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['MH'])
        rule250 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['H'])
        rule251 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule252 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['H'])
        rule253 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['M'])
        rule254 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule255 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['M'])
        rule256 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule257 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule258 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule259 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['MH'])
        rule260 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['M'])
        rule261 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['MH'])
        rule262 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['H'])
        rule263 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule264 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['H'])
        rule265 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['H'])
        rule266 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['MH'])
        rule267 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['H'])
        rule268 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VH'])
        rule269 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['H'])
        rule270 = ctrl.Rule(ap['Mod'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VH'])
        rule271 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['M'])
        rule272 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule273 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['M'])
        rule274 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule275 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule276 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule277 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['MH'])
        rule278 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['M'])
        rule279 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['MH'])
        rule280 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['H'])
        rule281 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule282 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['H'])
        rule283 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['H'])
        rule284 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['MH'])
        rule285 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['H'])
        rule286 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VH'])
        rule287 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['H'])
        rule288 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VH'])
        rule289 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['MH'])
        rule290 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['M'])
        rule291 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['MH'])
        rule292 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['H'])
        rule293 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule294 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['H'])
        rule295 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['H'])
        rule296 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['MH'])
        rule297 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['H'])
        rule298 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['VH'])
        rule299 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['H'])
        rule300 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['VH'])
        rule301 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VH'])
        rule302 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['H'])
        rule303 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VH'])
        rule304 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule305 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VH'])
        rule306 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule307 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['H'])
        rule308 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['MH'])
        rule309 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['H'])
        rule310 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['VH'])
        rule311 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['H'])
        rule312 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['VH'])
        rule313 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['VH'])
        rule314 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['H'])
        rule315 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['VH'])
        rule316 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule317 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['VH'])
        rule318 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule319 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VVH'])
        rule320 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['VH'])
        rule321 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VVH'])
        rule322 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule323 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VVH'])
        rule324 = ctrl.Rule(ap['Mod'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule325 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['L'])
        rule326 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['VL'])
        rule327 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['L'])
        rule328 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['ML'])
        rule329 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['L'])
        rule330 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['ML'])
        rule331 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['ML'])
        rule332 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['L'])
        rule333 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['ML'])
        rule334 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['M'])
        rule335 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'],cd['ML'])
        rule336 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['M'])
        rule337 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['M'])
        rule338 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule339 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['M'])
        rule340 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule341 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule342 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule343 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['ML'])
        rule344 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['L'])
        rule345 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['ML'])
        rule346 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['M'])
        rule347 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['ML'])
        rule348 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['M'])
        rule349 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['M'])
        rule350 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule351 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['M'])
        rule352 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule353 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule354 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule355 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['MH'])
        rule356 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['M'])
        rule357 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['MH'])
        rule358 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['H'])
        rule359 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule360 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['H'])
        rule361 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['M'])
        rule362 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule363 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['M'])
        rule364 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule365 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule366 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule367 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['MH'])
        rule368 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['M'])
        rule369 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['MH'])
        rule370 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['H'])
        rule371 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule372 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['H'])
        rule373 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VH'])
        rule374 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['H'])
        rule375 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VH'])
        rule376 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule377 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VH'])
        rule378 = ctrl.Rule(ap['Sev'] & an['Mild'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule379 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['M'])
        rule380 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['ML'])
        rule381 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['M'])
        rule382 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['MH'])
        rule383 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['M'])
        rule384 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['MH'])
        rule385 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['MH'])
        rule386 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['M'])
        rule387 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['MH'])
        rule388 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['H'])
        rule389 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule390 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['H'])
        rule391 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['H'])
        rule392 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['MH'])
        rule393 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['H'])
        rule394 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VH'])
        rule395 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['H'])
        rule396 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VH'])
        rule397 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['MH'])
        rule398 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['M'])
        rule399 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['MH'])
        rule400 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['H'])
        rule401 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['MH'])
        rule402 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['H'])
        rule403 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['H'])
        rule404 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['MH'])
        rule405 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['H'])
        rule406 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['VH'])
        rule407 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['H'])
        rule408 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['VH'])
        rule409 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VH'])
        rule410 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['H'])
        rule411 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VH'])
        rule412 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule413 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VH'])
        rule414 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule415 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['H'])
        rule416 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['MH'])
        rule417 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['H'])
        rule418 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['VH'])
        rule419 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['H'])
        rule420 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['VH'])
        rule421 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['VH'])
        rule422 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['H'])
        rule423 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['VH'])
        rule424 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule425 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['VH'])
        rule426 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule427 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VVH'])
        rule428 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['VH'])
        rule429 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VVH'])
        rule430 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule431 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VVH'])
        rule432 = ctrl.Rule(ap['Sev'] & an['Mod'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule433 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['H'])
        rule434 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['MH'])
        rule435 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['H'])
        rule436 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['VH'])
        rule437 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['H'])
        rule438 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['VH'])
        rule439 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['VH'])
        rule440 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['H'])
        rule441 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['VH'])
        rule442 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule443 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['VH'])
        rule444 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule445 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VH'])
        rule446 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['H'])
        rule447 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VH'])
        rule448 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule449 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VH'])
        rule450 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mild'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule451 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['VH'])
        rule452 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['H'])
        rule453 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['VH'])
        rule454 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule455 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['VH'])
        rule456 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule457 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['VVH'])
        rule458 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['VH'])
        rule459 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['VVH'])
        rule460 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule461 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['VVH'])
        rule462 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule463 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VVH'])
        rule464 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['VVH'])
        rule465 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VVH'])
        rule466 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule467 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VVH'])
        rule468 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Mod'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule469 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['VVH'])
        rule470 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['VH'])
        rule471 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['VVH'])
        rule472 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule473 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['VVH'])
        rule474 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['OnceWeek'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule475 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['UW'], cd['VVH'])
        rule476 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['Normal'], cd['VVH'])
        rule477 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['US'] & bmi['OW'], cd['VVH'])
        rule478 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule479 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['Normal'], cd['VVH'])
        rule480 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['ThriceWeek'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule481 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['UW'], cd['VVH'])
        rule482 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['Normal'], cd['VVH'])
        rule483 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['US'] & bmi['OW'], cd['VVH'])
        rule484 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['UW'], cd['VVH'])
        rule485 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['Normal'], cd['VVH'])
        rule486 = ctrl.Rule(ap['Sev'] & an['Sev'] & da['Sev'] & vom['Daily'] & wl['UL'] & bmi['OW'], cd['VVH'])
        rule = []
        for i in range(1, 487):
            rule.append(eval("rule" + str(i)))
        cdlevel = ctrl.ControlSystemSimulation(fuzz.control.ControlSystem(rule))
        cdlevel.input['ap'] = Abdominal_Pain_value
        cdlevel.input['an'] = Anemia_value
        cdlevel.input['da'] = Diarihea_value
        cdlevel.input['vom'] = Vomiting_value
        cdlevel.input['wl'] = Weight_Loss_value
        cdlevel.input['bmi'] = BMI_value
        cdlevel.compute()
        cd.view(sim=cdlevel)
        Result(cdlevel.output['cd'])
def get_BMI_value(val):
    global BMI_value, BMI_entry
    BMI_entry.delete( 0, END)
    BMI_entry.insert(END, val)
    y = StringVar()
    BMI_text = '                                                           '
    y.set(BMI_text)
    BMI_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=13, column=3)
def get_Weight_Loss_value(val):
    global Weight_Loss_value, Weight_Loss_entry
    Weight_Loss_entry.delete(0, END)
    Weight_Loss_entry.insert(END, val)
    y = StringVar()
    Weight_Loss_text = '                                                          '
    y.set(Weight_Loss_text)
    Weight_Loss_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=11, column=3)
def get_Vomiting_value(val):
    global Vomiting_value, Vomiting_entry
    Vomiting_entry.delete(0, END)
    Vomiting_entry.insert(END, val)
    y = StringVar()
    Vomiting_text = '                                                          '
    y.set(Vomiting_text)
    Vomiting_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=9, column=3)
def get_Diarihea_value(val):
    global Diarihea_value, Diarihea_entry
    Diarihea_entry.delete(0, END)
    Diarihea_entry.insert(END, val)
    y = StringVar()
    Diarihea_text = '                                                          '
    y.set(Diarihea_text)
    Diarihea_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=7, column=3)
def get_Anemia_value(val):
    global Anemia_value, Anemia_entry
    Anemia_entry.delete(0, END)
    Anemia_entry.insert(END, val)
    y = StringVar()
    Anemia_text = '                                                          '
    y.set(Anemia_text)
    Anemia_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=5, column=3)
def get_Abdominal_Pain_value(val):
    global Abdominal_Pain_value, Abdominal_Pain_entry
    Abdominal_Pain_entry.delete(0, END)
    Abdominal_Pain_entry.insert(END, val)
    y = StringVar()
    Abdominal_Pain_text = '                                                          '
    y.set(Abdominal_Pain_text)
    Abdominal_Pain_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=3, column=3)
def Calculate_BMI_Calculate_func():
    global Enter_Age_entry, Enter_Height_Feet_entry, Enter_Height_Inch_entry, Enter_Weight_entry, Calculate_BMI_root, BMI_Scale
    flag = 0
    try:
        Age = float(Enter_Age_entry.get())
        correct_label = Label(Calculate_BMI_root, text='                                                          ', font=("Helvetica", 10), width=30).grid(rowspan=1, row=2, column=1)
    except:
        error_label = Label(Calculate_BMI_root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10), width=30).grid(rowspan=1, row=2, column=1)
        flag = 1
    try:
        Weight = float(Enter_Weight_entry.get())
        correct_label = Label(Calculate_BMI_root, text='                                                          ', font=("Helvetica", 10), width=30).grid(rowspan=1, row=9, column=1)
    except:
        error_label = Label(Calculate_BMI_root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10), width=30).grid(rowspan=1, row=9, column=1)
        flag = 1
    try:
        Height_Feet = float(Enter_Height_Feet_entry.get())
        correct_label = Label(Calculate_BMI_root, text='                                                          ', font=("Helvetica", 10), width=30).grid(rowspan=1, row=7, column=1)
        if Enter_Height_Inch_entry.get() == '':
            Height_Inch = 0
        else:
            Height_Inch = float(Enter_Height_Inch_entry.get())
        correct_label = Label(Calculate_BMI_root, text='                                                          ', font=("Helvetica", 10), width=30).grid(rowspan=1, row=7, column=1)
    except:
        error_label = Label(Calculate_BMI_root, fg='red', text='Please enter (some / valid) value.', font=("Helvetica", 10), width=30).grid(rowspan=1, row=7, column=1)
        flag = 1
    if flag == 0:
        Height = ((((Height_Feet * 12) + Height_Inch) * 2.54) / 100)
        BMI_val = round((Weight / (Height * Height)), 3)
        BMI_entry.delete(0, END)
        BMI_entry.insert(END, BMI_val)
        BMI_Scale.set(BMI_val)
        Calculate_BMI_root.destroy()
def Calculate_BMI_func():
    global Enter_Age_entry, Enter_Height_Feet_entry, Enter_Height_Inch_entry, Enter_Weight_entry, Calculate_BMI_root
    Calculate_BMI_root = Tk()
    v = IntVar()
    Calculate_BMI_Age_var, Calculate_BMI_Height_Feet_var, Calculate_BMI_Height_Inch_var, Calculate_BMI_Weight_var = StringVar(), StringVar(), StringVar(), StringVar()
    Calculate_BMI_root.title("CALCULATE DATA")
    Enter_Age_label = Label(Calculate_BMI_root, padx=10, pady=10, text='Enter Age : ', font=("Helvetica", 12), fg='black').grid(rowspan=1, row=1,columnspan=3)
    Enter_Age_entry = Entry(Calculate_BMI_root, textvariable=Calculate_BMI_Age_var, width=20)
    Enter_Age_entry.grid(rowspan=1, row=1, column=3, columnspan=2)
    space_label = Label(Calculate_BMI_root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=2, column=1)
    Enter_Gender_label = Label(Calculate_BMI_root, padx=10, pady=10, text='Select Gender', font=("Helvetica", 12), fg='black').grid(rowspan=1, row=3, columnspan=2)
    Radiobutton(Calculate_BMI_root, text="Male", variable=v, padx=20, value="Male").grid(rowspan=1, row=3, column=2)
    Radiobutton(Calculate_BMI_root, text="Female", variable=v, padx=20, value="Female").grid(rowspan=1, row=3, column=3)
    space_label = Label(Calculate_BMI_root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=4, column=1)
    Enter_Height_label = Label(Calculate_BMI_root, padx=10, pady=10, text='Enter Height', font=("Helvetica", 12), fg='black').grid(rowspan=2, row=5, column=0)
    Enter_Height_label = Label(Calculate_BMI_root, padx=10, pady=10, text='( in Feets ) : ', font=("Helvetica", 12), fg='black').grid(rowspan=1, row=5, column=1, columnspan=1)
    Enter_Height_label = Label(Calculate_BMI_root, padx=10, pady=10, text='( in Inches ): ', font=("Helvetica", 12), fg='black').grid(rowspan=1, row=6, column=1, columnspan=1)
    Enter_Height_Feet_entry = Entry(Calculate_BMI_root, textvariable=Calculate_BMI_Height_Feet_var, width=20)
    Enter_Height_Feet_entry.grid(rowspan=1, row=5, column=3, columnspan=1)
    Enter_Height_Inch_entry = Entry(Calculate_BMI_root, textvariable=Calculate_BMI_Height_Inch_var, width=20)
    Enter_Height_Inch_entry.grid(rowspan=1, row=6, column=3, columnspan=1)
    space_label = Label(Calculate_BMI_root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=7, column=1)
    Enter_Weight_label = Label(Calculate_BMI_root, padx=10, pady=10, text='Enter Weight     ( in  Kilograms ): ', font=("Helvetica", 12), fg='black').grid(rowspan=1, row=8,columnspan=3)
    Enter_Weight_entry = Entry(Calculate_BMI_root, textvariable=Calculate_BMI_Weight_var, width=20)
    Enter_Weight_entry.grid(rowspan=1, row=8, column=3, columnspan=2)
    space_label = Label(Calculate_BMI_root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=9, column=1)
    Calculate_BMI_Calculate_button = Button(Calculate_BMI_root, padx=39, pady=10, text='CALCULATE', fg='black', command=lambda: Calculate_BMI_Calculate_func()).grid(rowspan=1, row=10, columnspan=5)
    Calculate_BMI_root.mainloop()
def heading_label_func():
    heading_root = Tk()
    heading_root.title("Celiac Disease Probabilistic System")
    heading_label = Label(heading_root, text='Celiac Disease Probabilistic System', font=("Helvetica", 15)).pack()
    heading_label = Label(heading_root, text='Celiac disease is a kind of autoimmune disorder damaging small intestine after taking gluten in\n'
        'the diet by an individual.Gluten can be in the form of wheat, barley, rye etc. which appears as\n'
        'toxic agents to damage small intestine in the body. It has been confirmed that HLA DQ2/DQ8\n'
        'exists in all celiac patients.Celiac patients might provoke a severe effect on intestine by shaping\n'
        'differently in mucosa having a risk of death via gastro problem or any type of cancer.\n'
        'Symptoms of Celiac Disease\n'
        'Celiac disease symptoms deviate from patients with mild to severe effects. Celiac disease can\n'
        'occur at any age and gastrointestinal symptoms accompanying with multiple disorders. The\n'
        'numerous common symptoms are:\n'
        '• Abdominal Pain: Abdominal pain is a vital symptom present in celiac patients. The severe pain\n'
        ' often presents in the lower part of the abdomen as proclaimed by most individuals.\n\n'
        '• Iron Deficiency Anemia: Due to nutrient absorption, there is a possibility of the drop in red\n'
        'blood cells in the body.With GFD, iron level swiftly increases with existing celiac patients.\n'
        'There are unusual other reasons also for iron-deficiency with additional diseases.\n\n'
        '• Diarrhea: One of the basic symptoms of celiac disease as watery-stool (diarrhea). Frequently,\n'
        'all celiac patients own the difficulty of diarrhea after taking gluten in the menu.It takes several\n'
        'weeks to settle the problem after the consumption of GFD.\n\n'
        '• Vomiting: Another common symptom that is basically found in celiac patients is in the form of\n'
        'vomiting with varied symptom leads to daily vomiting after the consumption of gluten in the diet.\n\n'
        '• Weight Loss: A brisk reduction in the weight is the prime sign of celiac disease. Due to fewer\n'
        'nutrients consumption, weight loss consistently humiliates within a few weeks.\n\n'
        '• Body Mass Index: The symptom that is commonly present in celiac patients as Underweight or\n'
        'Overweight BMI. This is due to weight loss or weight gain which will effect either in the\n'
        'increase or decrease of BMI.', font=("Helvetica", 10)).pack()
def Abdominal_Pain_label_func():
    Abdominal_Pain_root = Tk()
    Abdominal_Pain_root.title("Abdominal Pain")
    Abdominal_Pain_label = Label(Abdominal_Pain_root, text='Abdominal Pain', font=("Helvetica", 15)).pack()
    Abdominal_Pain_label = Label(Abdominal_Pain_root, text='Abdominal Pain: Abdominal pain is a vital symptom present in celiac patients. The severe pain\n'
        ' often presents in the lower part of the abdomen as proclaimed by most individuals.', font=("Helvetica", 10)).pack()
def Anemia_label_func():
    Anemia_root = Tk()
    Anemia_root.title("Anemia")
    Anemia_label = Label(Anemia_root, text='Anemia', font=("Helvetica", 15)).pack()
    Anemia_label = Label(Anemia_root, text='Iron Deficiency Anemia: Due to nutrient absorption, there is a possibility of the drop in red\n'
        'blood cells in the body.With GFD, iron level swiftly increases with existing celiac patients.\n'
        'There are unusual other reasons also for iron-deficiency with additional diseases.', font=("Helvetica", 10)).pack()
def Diarihea_label_func():
    Diarihea_root = Tk()
    Diarihea_root.title("Diarihea")
    Diarihea_label = Label(Diarihea_root, text='Diarihea', font=("Helvetica", 15)).pack()
    Diarihea_label = Label(Diarihea_root, text='Diarrhea: One of the basic symptoms of celiac disease as watery-stool (diarrhea). Frequently,\n'
        'all celiac patients own the difficulty of diarrhea after taking gluten in the menu.It takes several\n'
        'weeks to settle the problem after the consumption of GFD.', font=("Helvetica", 10)).pack()
def Vomiting_label_func():
    Vomiting_root = Tk()
    Vomiting_root.title("Vomiting")
    Vomiting_label = Label(Vomiting_root, text='Vomiting', font=("Helvetica", 15)).pack()
    Vomiting_label = Label(Vomiting_root, text='Vomiting: Another common symptom that is basically found in celiac patients is in the form of\n'
        'vomiting with varied symptom leads to daily vomiting after the consumption of gluten in the diet.', font=("Helvetica", 10)).pack()
def Weight_Loss_label_func():
    Weight_Loss_root = Tk()
    Weight_Loss_root.title("Weight Loss")
    Weight_Loss_label = Label(Weight_Loss_root, text='Weight Loss', font=("Helvetica", 15)).pack()
    Weight_Loss_label = Label(Weight_Loss_root, text='Weight Loss: A brisk reduction in the weight is the prime sign of celiac disease. Due to fewer\n'
        'nutrients consumption, weight loss consistently humiliates within a few weeks.', font=("Helvetica", 10)).pack()
def BMI_label_func():
    BMI_root = Tk()
    BMI_root.title("BMI")
    BMI_label = Label(BMI_root, text='BMI', font=("Helvetica", 15)).pack()
    BMI_label = Label(BMI_root, text='Body Mass Index: The symptom that is commonly present in celiac patients as Underweight or\n'
        'Overweight BMI. This is due to weight loss or weight gain which will effect either in the\n'
        'increase or decrease of BMI.', font=("Helvetica", 10)).pack()
def Create_GUI():
    global Abdominal_Pain_Scale, Abdominal_Pain_var, Abdominal_Pain_entry, Anemia_Scale, Anemia_var, Anemia_entry, Diarihea_var, Diarihea_entry, Diarihea_Scale,Weight_Loss_Scale, Vomiting_Scale, Vomiting_var, Vomiting_entry, Weight_Loss_var, Weight_Loss_entry,BMI_var, BMI_entry, BMI_Scale
    Abdominal_Pain_var, Anemia_var, Diarihea_var, Vomiting_var, Weight_Loss_var, BMI_var = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
    root.title("Celiac Disease Probabilistic System")
    heading_label_button = Button(root, padx=30, pady=7, text='Celiac Disease Probabilistic System', font=("Helvetica", 20), fg='black', borderwidth=0, command=lambda: heading_label_func()).grid(rowspan=1, row=1, columnspan=6)
    # enter_details_label = Label(root, padx=70, pady=10, text='Enter Details -->', font=("Helvetica", 14)).grid(row=1)
    Abdominal_Pain_label_button = Button(root, pady=10, text='Abdominal Pain', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Abdominal_Pain_label_func()).grid(rowspan=1, row=2,columnspan=2)
    Abdominal_Pain_Scale = Scale(root, label = '', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command = get_Abdominal_Pain_value)
    Abdominal_Pain_Scale.grid(rowspan=1, row=2, column=2, columnspan=2)
    Abdominal_Pain_entry = Entry(root, textvariable=Abdominal_Pain_var, width=10)
    Abdominal_Pain_entry.grid(rowspan=1, row=2, column=4)
    Abdominal_Pain_button = Button(root, padx=12, pady=10, text='PLOT ABDOMINAL PAIN', fg='black', command=lambda: Abdominal_Pain_func()).grid(rowspan=1, row=2,column=5)
    space_label = Label(root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=3, column=1)
    Anemia_label_button = Button(root, pady=10, text='Anemia', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Anemia_label_func()).grid(rowspan=1, row=4, columnspan=2)
    Anemia_Scale = Scale(root, label='', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command=get_Anemia_value)
    Anemia_Scale.grid(rowspan=1, row=4, column=2,  columnspan=2)
    Anemia_entry = Entry(root, textvariable=Anemia_var, width=10)
    Anemia_entry.grid(rowspan=1, row=4, column=4)
    Anemia_button = Button(root, padx=39, pady=10, text='PLOT ANEMIA', fg='black', command=lambda: Anemia_func()).grid(rowspan=1, row=4,column=5)
    space_label = Label(root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=5, column=1)
    Diarihea_label_button = Button(root, pady=10, text='Diarihea', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Diarihea_label_func()).grid(rowspan=1, row=6, columnspan=2)
    Diarihea_Scale = Scale(root, label='', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command=get_Diarihea_value)
    Diarihea_Scale.grid(rowspan=1, row=6, column=2,  columnspan=2)
    Diarihea_entry = Entry(root, textvariable=Diarihea_var, width=10)
    Diarihea_entry.grid(rowspan=1, row=6, column=4)
    Diarihea_button = Button(root, padx=35, pady=10, text='PLOT DIARIHEA', fg='black', command=lambda: Diarihea_func()).grid(rowspan=1, row=6,column=5)
    space_label = Label(root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=7, column=1)
    Vomiting_label_button = Button(root, pady=10, text='Vomiting', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Vomiting_label_func()).grid(rowspan=1, row=8, columnspan=2)
    Vomiting_Scale = Scale(root, label='', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command=get_Vomiting_value)
    Vomiting_Scale.grid(rowspan=1, row=8, column=2, columnspan=2)
    Vomiting_entry = Entry(root, textvariable=Vomiting_var, width=10)
    Vomiting_entry.grid(rowspan=1, row=8, column=4)
    Vomiting_button = Button(root, padx=32, pady=10, text='PLOT VOMITING', fg='black', command=lambda: Vomiting_func()).grid(rowspan=1, row=8,column=5)
    space_label = Label(root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=9, column=1)
    Weight_Loss_label_button = Button(root, pady=10, text='Weight Loss', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Weight_Loss_label_func()).grid(rowspan=1, row=10, columnspan=2)
    Weight_Loss_Scale = Scale(root, label='', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command=get_Weight_Loss_value)
    Weight_Loss_Scale.grid(rowspan=1, row=10, column=2, columnspan=2)
    Weight_Loss_entry = Entry(root, textvariable=Weight_Loss_var, width=10)
    Weight_Loss_entry.grid(rowspan=1, row=10, column=4)
    Weight_Loss_button = Button(root, padx=24, pady=10, text='PLOT WEIGHT LOSS', fg='black', command=lambda: Weight_Loss_func()).grid(rowspan=1, row=10,column=5)
    space_label = Label(root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=11, column=1)
    BMI_label_button = Button(root, text='              BMI', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: BMI_label_func()).grid(rowspan=1, row=12, column=0)
    Calculate_BMI_button = Button(root, padx= 20, pady=10, text='CALCULATE BMI', fg='black', command=lambda: Calculate_BMI_func()).grid(rowspan=1, row=12,column=1)
    BMI_Scale = Scale(root, label='', from_=0, to=40, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=10, command=get_BMI_value)
    BMI_Scale.grid(rowspan=1, row=12, column=2, columnspan=2)
    BMI_entry = Entry(root, textvariable=BMI_var, width=10)
    BMI_entry.grid(rowspan=1, row=12, column=4)
    BMI_button = Button(root, padx=50, pady=10, text='PLOT BMI', fg='black', command=lambda: BIM_func()).grid(rowspan=1, row=12,column=5)
    space_label = Label(root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=13, column=1)
    Calculate_button = Button(root, padx=30, pady=10, text='CALCULATE', fg='black', command=lambda: Calculate()).grid(rowspan=1, row=14, column=3)
    space_label = Label(root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=15, column=1)
Create_GUI()
root.mainloop()
