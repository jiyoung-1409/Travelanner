import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import time as t
from datetime import datetime, timedelta
import tkinter.font
import os
import webbrowser as wb
import shutil
from tkinter import filedialog # 별도로 import
import PIL.Image
import fnmatch
from tkinter import *

start_win = Tk()
start_win.title("Travelanner")

# set position
start_win.geometry("480x600+500+100")
start_win.resizable(False, False)

# start frame -----------------------------------------------------------------------------------

# date label
time_font = tkinter.font.Font(family = "Times New Roman", size = 13)

date_lbl = Label(start_win, bg = "slate gray", font = time_font, fg = "White")
date_lbl.place(x = 5, y = 23)

def dclock():
    time_live = t.strftime("%Y:%m:%d:%H:%M")
    date_lbl.config(text = time_live)
    date_lbl.after(200, dclock)

# title label
isexist_file = t.strftime("%Y_%m_%d.txt")
def isexist():
    true_dir = []
    path = "./1_plans_folder/"
    for folder in os.listdir(path):
        if fnmatch.fnmatch(folder, 'Plan_folder*'):
            true_dir.append(folder)
    for folder in true_dir:
        global folder_path
        folder_path = str(path + folder)
        for file in os.listdir(folder_path):
            if file == isexist_file:
                return True

def config_bg_frame():
    def open_frame(frame):
        frame.tkraise()

    if isexist() == True:
        open_frame(bg_frame)
        global folder_path
        today_plan_file = folder_path + "/" + isexist_file
                                    
        f = open("{0}" .format(today_plan_file), "r")

        lines_infile = []

        for i in range(26):
            line = f.readline().strip()
            lines_infile.append(line)

        f.close()

        time_lst = []

        time_lst.extend("0" + str(i) + ":00" for i in range(0,10))
        time_lst.extend("1" + str(i) + ":00" for i in range(0,10))
        time_lst.extend(("2" + str(i) + ":00" for i in range(0,5)))

        # text_in_timelbl0 = ""
        # text_in_timelbl1 = ""
        # text_in_timelbl2 = ""
        # text_in_timelbl3 = ""
        # text_in_timelbl4 = ""
        # text_in_timelbl5 = ""
        # text_in_timelbl6 = ""
        # text_in_timelbl7 = ""
        # text_in_timelbl8 = ""
        # text_in_timelbl9 = ""
        # text_in_timelbl10 = ""
        # text_in_timelbl11 = ""
        # text_in_timelbl12 = ""
        # text_in_timelbl13 = ""
        # text_in_timelbl14 = ""
        # text_in_timelbl15 = ""
        # text_in_timelbl16 = ""
        # text_in_timelbl17 = ""
        # text_in_timelbl18 = ""
        # text_in_timelbl19 = ""
        # text_in_timelbl20 = ""
        # text_in_timelbl21 = ""
        # text_in_timelbl22 = ""
        # text_in_timelbl23 = ""
        # text_in_timelbl24 = ""

        if lines_infile[0] in time_lst:
            location = time_lst.index(lines_infile[0])
            lbl_num = 0
            for i in range(location, 25):
                globals()["text_in_timelbl{}" .format(lbl_num)] = time_lst[i]
                lbl_num += 1
            globals()["text_in_timelbl{}" .format(lbl_num)] = ""
            while not(lbl_num == 23):
                lbl_num += 1
                globals()['text_in_timelbl{}' .format(lbl_num)] = ""
                

        time_lbl0 = Label(bg_frame, text = globals()["text_in_timelbl0"], borderwidth=2, relief="ridge",  width = 5, height = 1)
        time_lbl1 = Label(bg_frame, text = globals()["text_in_timelbl1"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl2 = Label(bg_frame, text = globals()["text_in_timelbl2"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl3 = Label(bg_frame, text = globals()["text_in_timelbl3"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl4 = Label(bg_frame, text = globals()["text_in_timelbl4"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl5 = Label(bg_frame, text = globals()["text_in_timelbl5"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl6 = Label(bg_frame, text = globals()["text_in_timelbl6"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl7 = Label(bg_frame, text = globals()["text_in_timelbl7"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl8 = Label(bg_frame, text = globals()["text_in_timelbl8"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl9 = Label(bg_frame, text = globals()["text_in_timelbl9"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl10 = Label(bg_frame, text = globals()["text_in_timelbl10"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl11 = Label(bg_frame, text = globals()["text_in_timelbl11"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl12 = Label(bg_frame, text = globals()["text_in_timelbl12"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl13 = Label(bg_frame, text = globals()["text_in_timelbl13"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl14 = Label(bg_frame, text = globals()["text_in_timelbl14"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl15 = Label(bg_frame, text = globals()["text_in_timelbl15"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl16 = Label(bg_frame, text = globals()["text_in_timelbl16"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl17 = Label(bg_frame, text = globals()["text_in_timelbl17"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl18 = Label(bg_frame, text = globals()["text_in_timelbl18"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl19 = Label(bg_frame, text = globals()["text_in_timelbl19"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl20 = Label(bg_frame, text = globals()["text_in_timelbl20"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl21 = Label(bg_frame, text = globals()["text_in_timelbl21"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl22 = Label(bg_frame, text = globals()["text_in_timelbl22"], borderwidth=2, relief="ridge", width = 5, height = 1)
        time_lbl23 = Label(bg_frame, text = globals()["text_in_timelbl23"], borderwidth=2, relief="ridge", width = 5, height = 1)

        time_lbl0.grid(row = 0, column = 0, sticky = N+E+W+S)
        time_lbl1.grid(row = 1, column = 0, sticky=N+E+W+S)
        time_lbl2.grid(row = 2, column = 0, sticky=N+E+W+S)
        time_lbl3.grid(row = 3, column = 0, sticky=N+E+W+S)
        time_lbl4.grid(row = 4, column = 0, sticky=N+E+W+S)
        time_lbl5.grid(row = 5, column = 0, sticky=N+E+W+S)
        time_lbl6.grid(row = 6, column = 0, sticky=N+E+W+S)
        time_lbl7.grid(row = 7, column = 0, sticky=N+E+W+S)
        time_lbl8.grid(row = 8, column = 0, sticky=N+E+W+S)
        time_lbl9.grid(row = 9, column = 0, sticky=N+E+W+S)
        time_lbl10.grid(row = 10, column = 0, sticky=N+E+W+S)
        time_lbl11.grid(row = 11, column = 0, sticky=N+E+W+S)
        time_lbl12.grid(row = 12, column = 0, sticky=N+E+W+S)
        time_lbl13.grid(row = 13, column = 0, sticky=N+E+W+S)
        time_lbl14.grid(row = 14, column = 0, sticky=N+E+W+S)
        time_lbl15.grid(row = 15, column = 0, sticky=N+E+W+S)
        time_lbl16.grid(row = 16, column = 0, sticky=N+E+W+S)
        time_lbl17.grid(row = 17, column = 0, sticky=N+E+W+S)
        time_lbl18.grid(row = 18, column = 0, sticky=N+E+W+S)
        time_lbl19.grid(row = 19, column = 0, sticky=N+E+W+S)
        time_lbl20.grid(row = 20, column = 0, sticky=N+E+W+S)
        time_lbl21.grid(row = 21, column = 0, sticky=N+E+W+S)
        time_lbl22.grid(row = 22, column = 0, sticky=N+E+W+S)
        time_lbl23.grid(row = 23, column = 0, sticky=N+E+W+S)

        text_in_infolbl0 = lines_infile[1]
        text_in_infolbl1 = lines_infile[2]
        text_in_infolbl2 = lines_infile[3]
        text_in_infolbl3 = lines_infile[4]
        text_in_infolbl4 = lines_infile[5]
        text_in_infolbl5 = lines_infile[6]
        text_in_infolbl6 = lines_infile[7]
        text_in_infolbl7 = lines_infile[8]
        text_in_infolbl8 = lines_infile[9]
        text_in_infolbl9 = lines_infile[10]
        text_in_infolbl10 = lines_infile[11]
        text_in_infolbl11 = lines_infile[12]
        text_in_infolbl12 = lines_infile[13]
        text_in_infolbl13 = lines_infile[14]
        text_in_infolbl14 = lines_infile[15]
        text_in_infolbl15 = lines_infile[16]
        text_in_infolbl16 = lines_infile[17]
        text_in_infolbl17 = lines_infile[18]
        text_in_infolbl18 = lines_infile[19]
        text_in_infolbl19 = lines_infile[20]
        text_in_infolbl20 = lines_infile[21]
        text_in_infolbl21 = lines_infile[22]
        text_in_infolbl22 = lines_infile[23]
        text_in_infolbl23 = lines_infile[24]

        info_lbl0 = Label(bg_frame, text = text_in_infolbl0, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl1 = Label(bg_frame, text = text_in_infolbl1, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl2 = Label(bg_frame, text = text_in_infolbl2, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl3 = Label(bg_frame, text = text_in_infolbl3, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl4 = Label(bg_frame, text = text_in_infolbl4, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl5 = Label(bg_frame, text = text_in_infolbl5, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl6 = Label(bg_frame, text = text_in_infolbl6, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl7 = Label(bg_frame, text = text_in_infolbl7, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl8 = Label(bg_frame, text = text_in_infolbl8, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl9 = Label(bg_frame, text = text_in_infolbl9, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl10 = Label(bg_frame, text = text_in_infolbl10, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl11 = Label(bg_frame, text = text_in_infolbl11, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl12 = Label(bg_frame, text = text_in_infolbl12, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl13 = Label(bg_frame, text = text_in_infolbl13, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl14 = Label(bg_frame, text = text_in_infolbl14, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl15 = Label(bg_frame, text = text_in_infolbl15, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl16 = Label(bg_frame, text = text_in_infolbl16, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl17 = Label(bg_frame, text = text_in_infolbl17, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl18 = Label(bg_frame, text = text_in_infolbl18, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl19 = Label(bg_frame, text = text_in_infolbl19, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl20 = Label(bg_frame, text = text_in_infolbl20, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl21 = Label(bg_frame, text = text_in_infolbl21, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl22 = Label(bg_frame, text = text_in_infolbl22, borderwidth=2, relief="ridge", width = 60, height =1)
        info_lbl23 = Label(bg_frame, text = text_in_infolbl23, borderwidth=2, relief="ridge", width = 60, height =1)

        info_lbl0.grid(row = 0, column = 1, sticky=N+E+W+S)
        info_lbl1.grid(row = 1, column = 1, sticky=N+E+W+S)
        info_lbl2.grid(row = 2, column = 1, sticky=N+E+W+S)
        info_lbl3.grid(row = 3, column = 1, sticky=N+E+W+S)
        info_lbl4.grid(row = 4, column = 1, sticky=N+E+W+S)
        info_lbl5.grid(row = 5, column = 1, sticky=N+E+W+S)
        info_lbl6.grid(row = 6, column = 1, sticky=N+E+W+S)
        info_lbl7.grid(row = 7, column = 1, sticky=N+E+W+S)
        info_lbl8.grid(row = 8, column = 1, sticky=N+E+W+S)
        info_lbl9.grid(row = 9, column = 1, sticky=N+E+W+S)
        info_lbl10.grid(row = 10, column = 1, sticky=N+E+W+S)
        info_lbl11.grid(row = 11, column = 1, sticky=N+E+W+S)
        info_lbl12.grid(row = 12, column = 1, sticky=N+E+W+S)
        info_lbl13.grid(row = 13, column = 1, sticky=N+E+W+S)
        info_lbl14.grid(row = 14, column = 1, sticky=N+E+W+S)
        info_lbl15.grid(row = 15, column = 1, sticky=N+E+W+S)
        info_lbl16.grid(row = 16, column = 1, sticky=N+E+W+S)
        info_lbl17.grid(row = 17, column = 1, sticky=N+E+W+S)
        info_lbl18.grid(row = 18, column = 1, sticky=N+E+W+S)
        info_lbl19.grid(row = 19, column = 1, sticky=N+E+W+S)
        info_lbl20.grid(row = 20, column = 1, sticky=N+E+W+S)
        info_lbl21.grid(row = 21, column = 1, sticky=N+E+W+S)
        info_lbl22.grid(row = 22, column = 1, sticky=N+E+W+S)
        info_lbl23.grid(row = 23, column = 1, sticky=N+E+W+S)

    else:
        bg_frame2 = Frame(start_win, width = 470, height = 510, relief = "sunken", bd = 2)
        bg_frame2.place(x = 5, y = 45)
        open_frame(bg_frame2)
        thereisnoplan_lbl = Label(bg_frame2, text = "no plan for today!").place(x = 180, y = 5)

title_font = tkinter.font.Font(family = "Times New Roman", size = 18)

title_btn = Button(start_win, padx = 5, pady = 1, text = "TRAVELANNER", font = title_font, fg = "White", bg = "slate gray", command = config_bg_frame)
title_btn.place(x = 150, y = 2)


# new plan button ----------------------------------------------------------------------------------
def new_plan_cmd():
    new_plan_win_cho = Tk()
    new_plan_win_cho.title("New plan - choose")

    new_plan_win_cho.geometry("480x300+500+250")
    new_plan_win_cho.resizable(False, False) 

    states_dict = { "Alabama":"AL", "Alaska":"AK", "Arizona":"AZ", "Arkansas":"AR", "California":"CA", "Colorado":"CO", "Connecticut":"CT", \
              "Delaware":"DE", "Washington":"WA", "Florida":"FL", "Georgia":"GA", "Hawaii":"HI", "Idaho":"ID", "Illinois":"IL", "Indiana":"IN" ,\
            "Iowa":"IA", "Kansas":"KS", "Kentucky":"KY", "Louisiana":"LA", "Maine":"ME", "Maryland":"MD", "Massachusetts":"MA", "Michigan":"MI" ,\
            "Minnesota":"MN", "Mississippi":"MS", "Missouri":"MO", "Montana":"MT", "Nebraska":"NE", "Nevada":"NV", "New Hampshire":"NH" ,\
            "New Jersey":"NJ", "New Mexico":"NM", "New York":"NY", "North Carolina":"NC", "North Dakota":"ND", "Ohio":"OH", "Oklahoma":"OK" ,\
            "Oregon":"OR", "Pennsylvania":"PA", "Rhode Island":"RI", "South Carolina":"SC", "South Dakota":"SD", "Tennessee":"TN", "Texas":"TX" ,\
            "Utah":"UT", "Vermont":"VT", "Virginia":"VA", "Wyoming":"WY", "West Virginia":"WV", "Wisconsin":"WI"}
    
    states_lst = [key for key in states_dict]


    state_combox = ttk.Combobox(new_plan_win_cho, width = 30, height = 5, values = states_lst, state = "readonly")
    state_combox.place(x = 120, y = 40)
    state_combox.set("State")

    year = [(2020 + i) for i in range(3, 10)]
    month = [i for i in range(1, 13)]
    day = [i for i in range(1, 32)]

    starts = Label(new_plan_win_cho, text = "Starts..", bg = "slate gray", fg = "White")
    starts.place(x = 30, y = 80)

    starting_year = ttk.Combobox(new_plan_win_cho, height = 5, values = year, state = "readonly")
    starting_year.place(x = 30, y = 110)
    starting_year.set("year")

    starting_month = ttk.Combobox(new_plan_win_cho, height = 5, values = month, state = "readonly")
    starting_month.place(x = 30, y = 160)
    starting_month.set("month")

    starting_day = ttk.Combobox(new_plan_win_cho, height = 5, values = day, state = "readonly")
    starting_day.place(x = 30, y = 210)
    starting_day.set("day")

    ends = Label(new_plan_win_cho, text = "ends..", bg = "slate gray", fg = "White")
    ends.place(x = 270, y = 80)

    ending_year = ttk.Combobox(new_plan_win_cho, height = 5, values = year, state = "readonly")
    ending_year.place(x = 270, y = 110)
    ending_year.set("year")

    ending_month = ttk.Combobox(new_plan_win_cho, height = 5, values = month, state = "readonly")
    ending_month.place(x = 270, y = 160)
    ending_month.set("month")

    ending_day = ttk.Combobox(new_plan_win_cho, height = 5, values = day, state = "readonly")
    ending_day.place(x = 270, y = 210)
    ending_day.set("day")


    def open_new_plan_win():
        State = state_combox.get()
        st_y = starting_year.get()
        st_m = starting_month.get()
        st_d  = starting_day.get()
        en_y = ending_year.get()
        en_m = ending_month.get()
        en_d = ending_day.get()


        if State == "State" or st_y == "year" or st_m == "month" or st_d == "day" or en_y == "year" or en_m == "month" or en_d == "day": 
            msgbox.showwarning("warning", "please select all")
            new_plan_win_cho.lift()
        else:
            if st_y > en_y:
                msgbox.showwarning("warning", "starting date couldn't be later than ending date!")                    
                new_plan_win_cho.lift()
            else:
                if st_y == en_y and st_m > en_m:
                    msgbox.showwarning("warning", "starting date couldn't be later than ending date!")
                    new_plan_win_cho.lift()
                else:
                    if st_y == en_y and st_m == en_m and st_d > en_d:
                        msgbox.showwarning("warning", "starting date couldn't be later than ending date!")
                        new_plan_win_cho.lift()
                    else:
                        def date_range(start, end):
                            start = datetime.strptime(start, "%Y/%m/%d")
                            end = datetime.strptime(end, "%Y/%m/%d")
                            dates = [(start + timedelta(days=i)).strftime("%Y/%m/%d") for i in range((end-start).days+1)]
                            return dates
        
                        date_lst = date_range(st_y + "/" + st_m + "/" + st_d, en_y + "/" + en_m + "/" + en_d)

                        temp_date_st_en = date_lst[0][:4] + "_" + date_lst[0][5:7] + "_" + date_lst[0][8:] + "__" + date_lst[-1][:4] + "_" + date_lst[-1][5:7] + "_" + date_lst[-1][8:]
                        
                        path = "./1_plans_folder/"
                        
                        if os.path.exists(path + "Plan_folder_{0}_{1}" .format(State, temp_date_st_en)):
                            pass
                        else:
                            os.makedirs(path + "Plan_folder_{0}_{1}" .format(State, temp_date_st_en), exist_ok=True)
                        
                            make_dir_name = path + "Plan_folder_{0}_{1}/" .format(State, temp_date_st_en)
                            for date in date_lst:
                                temp_each_date = date[:4] + "_" + date[5:7] + "_" + date[8:]
                                f = open("{0}{1}.txt" .format(make_dir_name, temp_each_date), "w")
                                for i in range(25):
                                    f.write("\n")
                                f.close()

                        new_plan_win_cho.destroy()

                        global open_new_plan_win_win
                        def open_new_plan_win_win(State = State, st_y = st_y, st_m = st_m, st_d  = st_d, en_y = en_y, en_m = en_m, en_d = en_d):

                            new_plan_win = Tk()
                            new_plan_win.title("Create New Plan")

                            new_plan_win.geometry("480x600+500+100")
                            new_plan_win.resizable(False, False)  

                            global cur_location_in_lst
                            cur_location_in_lst = 0


                            def plan_done_cmd():
                                get_lst = []
                                cur_location_name = date_lst[cur_location_in_lst][:4] + "_" + date_lst[cur_location_in_lst][5:7] + "_" + date_lst[cur_location_in_lst][8:]
                                f = open("{0}{1}.txt" .format(make_dir_name, cur_location_name), "w")
                                f.write(time_Ent0.get())
                                get_lst.append(info_Ent0.get())
                                get_lst.append(info_Ent1.get())
                                get_lst.append(info_Ent2.get())
                                get_lst.append(info_Ent3.get())
                                get_lst.append(info_Ent4.get())
                                get_lst.append(info_Ent5.get())
                                get_lst.append(info_Ent6.get())
                                get_lst.append(info_Ent7.get())
                                get_lst.append(info_Ent8.get())
                                get_lst.append(info_Ent9.get())
                                get_lst.append(info_Ent10.get())
                                get_lst.append(info_Ent11.get())
                                get_lst.append(info_Ent12.get())
                                get_lst.append(info_Ent13.get())
                                get_lst.append(info_Ent14.get())
                                get_lst.append(info_Ent15.get())
                                get_lst.append(info_Ent16.get())
                                get_lst.append(info_Ent17.get())
                                get_lst.append(info_Ent18.get())
                                get_lst.append(info_Ent19.get())
                                get_lst.append(info_Ent20.get())
                                get_lst.append(info_Ent21.get())
                                get_lst.append(info_Ent22.get())
                                get_lst.append(info_Ent23.get())
                                get_lst.append(info_Ent24.get())
                                for i in range(0, 25):
                                    f.write("\n" + "{0}" .format(get_lst[i]))
                                f.close()


                                new_plan_win.destroy()


                            def L_arrow_cmd():
                                time_lbl1.configure(text = "")
                                time_lbl2.configure(text = "")
                                time_lbl3.configure(text = "")
                                time_lbl4.configure(text = "")
                                time_lbl6.configure(text = "")
                                time_lbl5.configure(text = "")
                                time_lbl7.configure(text = "")
                                time_lbl8.configure(text = "")
                                time_lbl9.configure(text = "")
                                time_lbl10.configure(text = "")
                                time_lbl11.configure(text = "")
                                time_lbl12.configure(text = "")
                                time_lbl13.configure(text = "")
                                time_lbl14.configure(text = "")
                                time_lbl15.configure(text = "")
                                time_lbl16.configure(text = "")
                                time_lbl17.configure(text = "")
                                time_lbl18.configure(text = "")
                                time_lbl19.configure(text = "")
                                time_lbl20.configure(text = "")
                                time_lbl21.configure(text = "")
                                time_lbl22.configure(text = "")
                                time_lbl23.configure(text = "")
                                time_lbl24.configure(text = "")


                                global cur_location_in_lst
                                cur_location_in_lst -= 1
                                if len(date_lst) == 1:
                                    L_arrow_btn.config(state = DISABLED)
                                else:
                                    if cur_location_in_lst == 0:
                                        L_arrow_btn.config(state = DISABLED)

                                    if cur_location_in_lst < len(date_lst):
                                        R_arrow_btn.config(state = NORMAL)
                                    travel_date_lbl.config(text = date_lst[cur_location_in_lst])

                                
                                get_lst = []
                                cur_location_name = date_lst[cur_location_in_lst+1][:4] + "_" + date_lst[cur_location_in_lst+1][5:7] + "_" + date_lst[cur_location_in_lst+1][8:]
                                f = open("{0}{1}.txt" .format(make_dir_name, cur_location_name), "w")
                                f.write(time_Ent0.get())
                                get_lst.append(info_Ent0.get())
                                get_lst.append(info_Ent1.get())
                                get_lst.append(info_Ent2.get())
                                get_lst.append(info_Ent3.get())
                                get_lst.append(info_Ent4.get())
                                get_lst.append(info_Ent5.get())
                                get_lst.append(info_Ent6.get())
                                get_lst.append(info_Ent7.get())
                                get_lst.append(info_Ent8.get())
                                get_lst.append(info_Ent9.get())
                                get_lst.append(info_Ent10.get())
                                get_lst.append(info_Ent11.get())
                                get_lst.append(info_Ent12.get())
                                get_lst.append(info_Ent13.get())
                                get_lst.append(info_Ent14.get())
                                get_lst.append(info_Ent15.get())
                                get_lst.append(info_Ent16.get())
                                get_lst.append(info_Ent17.get())
                                get_lst.append(info_Ent18.get())
                                get_lst.append(info_Ent19.get())
                                get_lst.append(info_Ent20.get())
                                get_lst.append(info_Ent21.get())
                                get_lst.append(info_Ent22.get())
                                get_lst.append(info_Ent23.get())
                                get_lst.append(info_Ent24.get())
                                for i in range(0, 25):
                                    f.write("\n"+ "{0}" .format(get_lst[i]))
                                f.close()


                                cur_date_file = "./1_plans_folder/" + "Plan_folder_{0}_{1}/" .format(State, temp_date_st_en) + date_lst[cur_location_in_lst][:4] + "_" + date_lst[cur_location_in_lst][5:7] + "_" + date_lst[cur_location_in_lst][8:]
                                
                                f = open("{0}.txt" .format(cur_date_file), "r")

                                fixed_lines = []

                                for i in range(26):
                                    line = f.readline().strip()
                                    fixed_lines.append(line)


                                time_Ent0.delete(0, END)
                                time_Ent0.insert(0, fixed_lines[0])
                                info_Ent0.delete(0, END)                                
                                info_Ent0.insert(0, fixed_lines[1])
                                info_Ent1.delete(0, END)                                
                                info_Ent1.insert(0, fixed_lines[2])
                                info_Ent2.delete(0, END)                                
                                info_Ent2.insert(0, fixed_lines[3])
                                info_Ent3.delete(0, END)                                
                                info_Ent3.insert(0, fixed_lines[4])
                                info_Ent4.delete(0, END)                              
                                info_Ent4.insert(0, fixed_lines[5])
                                info_Ent5.delete(0, END)                                
                                info_Ent5.insert(0, fixed_lines[6])
                                info_Ent6.delete(0, END)                                
                                info_Ent6.insert(0, fixed_lines[7])
                                info_Ent7.delete(0, END)                                
                                info_Ent7.insert(0, fixed_lines[8])
                                info_Ent8.delete(0, END)                                
                                info_Ent8.insert(0, fixed_lines[9])
                                info_Ent9.delete(0, END)                                
                                info_Ent9.insert(0, fixed_lines[10])
                                info_Ent10.delete(0, END)                                
                                info_Ent10.insert(0, fixed_lines[11])
                                info_Ent11.delete(0, END)                                
                                info_Ent11.insert(0, fixed_lines[12])
                                info_Ent12.delete(0, END)                                
                                info_Ent12.insert(0, fixed_lines[13])
                                info_Ent13.delete(0, END)                                
                                info_Ent13.insert(0, fixed_lines[14])
                                info_Ent14.delete(0, END)                                
                                info_Ent14.insert(0, fixed_lines[15])
                                info_Ent15.delete(0, END)                                
                                info_Ent15.insert(0, fixed_lines[16])
                                info_Ent16.delete(0, END)                                
                                info_Ent16.insert(0, fixed_lines[17])
                                info_Ent17.delete(0, END)                                
                                info_Ent17.insert(0, fixed_lines[18])
                                info_Ent18.delete(0, END)                                
                                info_Ent18.insert(0, fixed_lines[19])
                                info_Ent19.delete(0, END)                                
                                info_Ent19.insert(0, fixed_lines[20])
                                info_Ent20.delete(0, END)                                
                                info_Ent20.insert(0, fixed_lines[21])
                                info_Ent21.delete(0, END)                                
                                info_Ent21.insert(0, fixed_lines[22])
                                info_Ent22.delete(0, END)                                
                                info_Ent22.insert(0, fixed_lines[23])
                                info_Ent23.delete(0, END)                                
                                info_Ent23.insert(0, fixed_lines[24])
                                info_Ent24.delete(0, END)                                
                                info_Ent24.insert(0, fixed_lines[25])

                                f.close()

                            global make_dir_name
                            make_dir_name = path + "Plan_folder_{0}_{1}/" .format(State, temp_date_st_en)

                            L_arrow_font = tkinter.font.Font(family = "Times New Roman", size = 12)
                            L_arrow_btn = Button(new_plan_win, text = "<", font = L_arrow_font, command = L_arrow_cmd, state = DISABLED)
                            L_arrow_btn.place(x = 150, y = 5)

                            def R_arrow_cmd():
                                time_lbl1.configure(text = "")
                                time_lbl2.configure(text = "")
                                time_lbl3.configure(text = "")
                                time_lbl4.configure(text = "")
                                time_lbl6.configure(text = "")
                                time_lbl5.configure(text = "")
                                time_lbl7.configure(text = "")
                                time_lbl8.configure(text = "")
                                time_lbl9.configure(text = "")
                                time_lbl10.configure(text = "")
                                time_lbl11.configure(text = "")
                                time_lbl12.configure(text = "")
                                time_lbl13.configure(text = "")
                                time_lbl14.configure(text = "")
                                time_lbl15.configure(text = "")
                                time_lbl16.configure(text = "")
                                time_lbl17.configure(text = "")
                                time_lbl18.configure(text = "")
                                time_lbl19.configure(text = "")
                                time_lbl20.configure(text = "")
                                time_lbl21.configure(text = "")
                                time_lbl22.configure(text = "")
                                time_lbl23.configure(text = "")
                                time_lbl24.configure(text = "")

                                global cur_location_in_lst
                                cur_location_in_lst += 1    
                                if cur_location_in_lst == (len(date_lst)-1):
                                    R_arrow_btn.config(state = DISABLED)

                                if cur_location_in_lst > 0:
                                    L_arrow_btn.config(state = NORMAL)
                                travel_date_lbl.config(text = date_lst[cur_location_in_lst])
                                
                                get_lst = []
                                cur_location_name = date_lst[cur_location_in_lst-1][:4] + "_" + date_lst[cur_location_in_lst-1][5:7] + "_" + date_lst[cur_location_in_lst-1][8:]
                                global make_dir_name
                                f = open("{0}{1}.txt" .format(make_dir_name, cur_location_name), "w")
                                f.write(time_Ent0.get())
                                get_lst.append(info_Ent0.get())
                                get_lst.append(info_Ent1.get())
                                get_lst.append(info_Ent2.get())
                                get_lst.append(info_Ent3.get())
                                get_lst.append(info_Ent4.get())
                                get_lst.append(info_Ent5.get())
                                get_lst.append(info_Ent6.get())
                                get_lst.append(info_Ent7.get())
                                get_lst.append(info_Ent8.get())
                                get_lst.append(info_Ent9.get())
                                get_lst.append(info_Ent10.get())
                                get_lst.append(info_Ent11.get())
                                get_lst.append(info_Ent12.get())
                                get_lst.append(info_Ent13.get())
                                get_lst.append(info_Ent14.get())
                                get_lst.append(info_Ent15.get())
                                get_lst.append(info_Ent16.get())
                                get_lst.append(info_Ent17.get())
                                get_lst.append(info_Ent18.get())
                                get_lst.append(info_Ent19.get())
                                get_lst.append(info_Ent20.get())
                                get_lst.append(info_Ent21.get())
                                get_lst.append(info_Ent22.get())
                                get_lst.append(info_Ent23.get())
                                get_lst.append(info_Ent24.get())

                                for i in range(0, 25):
                                    f.write("\n" + "{0}" .format(get_lst[i]))
                                f.close()

                                cur_date_file = "./1_plans_folder/" + "Plan_folder_{0}_{1}/" .format(State, temp_date_st_en) + date_lst[cur_location_in_lst][:4] + "_" + date_lst[cur_location_in_lst][5:7] + "_" + date_lst[cur_location_in_lst][8:]
                                
                                f = open("{0}.txt" .format(cur_date_file), "r")

                                fixed_lines = []

                                for i in range(26):
                                    line = f.readline().strip()
                                    fixed_lines.append(line)


                                time_Ent0.delete(0, END)
                                time_Ent0.insert(0, fixed_lines[0])
                                info_Ent0.delete(0, END)                                
                                info_Ent0.insert(0, fixed_lines[1])
                                info_Ent1.delete(0, END)                                
                                info_Ent1.insert(0, fixed_lines[2])
                                info_Ent2.delete(0, END)                                
                                info_Ent2.insert(0, fixed_lines[3])
                                info_Ent3.delete(0, END)                                
                                info_Ent3.insert(0, fixed_lines[4])
                                info_Ent4.delete(0, END)                              
                                info_Ent4.insert(0, fixed_lines[5])
                                info_Ent5.delete(0, END)                                
                                info_Ent5.insert(0, fixed_lines[6])
                                info_Ent6.delete(0, END)                                
                                info_Ent6.insert(0, fixed_lines[7])
                                info_Ent7.delete(0, END)                                
                                info_Ent7.insert(0, fixed_lines[8])
                                info_Ent8.delete(0, END)                                
                                info_Ent8.insert(0, fixed_lines[9])
                                info_Ent9.delete(0, END)                                
                                info_Ent9.insert(0, fixed_lines[10])
                                info_Ent10.delete(0, END)                                
                                info_Ent10.insert(0, fixed_lines[11])
                                info_Ent11.delete(0, END)                                
                                info_Ent11.insert(0, fixed_lines[12])
                                info_Ent12.delete(0, END)                                
                                info_Ent12.insert(0, fixed_lines[13])
                                info_Ent13.delete(0, END)                                
                                info_Ent13.insert(0, fixed_lines[14])
                                info_Ent14.delete(0, END)                                
                                info_Ent14.insert(0, fixed_lines[15])
                                info_Ent15.delete(0, END)                                
                                info_Ent15.insert(0, fixed_lines[16])
                                info_Ent16.delete(0, END)                                
                                info_Ent16.insert(0, fixed_lines[17])
                                info_Ent17.delete(0, END)                                
                                info_Ent17.insert(0, fixed_lines[18])
                                info_Ent18.delete(0, END)                                
                                info_Ent18.insert(0, fixed_lines[19])
                                info_Ent19.delete(0, END)                                
                                info_Ent19.insert(0, fixed_lines[20])
                                info_Ent20.delete(0, END)                                
                                info_Ent20.insert(0, fixed_lines[21])
                                info_Ent21.delete(0, END)                                
                                info_Ent21.insert(0, fixed_lines[22])
                                info_Ent22.delete(0, END)                                
                                info_Ent22.insert(0, fixed_lines[23])
                                info_Ent23.delete(0, END)                                
                                info_Ent23.insert(0, fixed_lines[24])
                                info_Ent24.delete(0, END)                                
                                info_Ent24.insert(0, fixed_lines[25])

                                f.close()


                            R_arrow_font = tkinter.font.Font(family = "Times New Roman", size = 12)
                            R_arrow_btn = Button(new_plan_win, text = ">", font = R_arrow_font, command = R_arrow_cmd)
                            R_arrow_btn.place(x = 310, y = 5)

                            if len(date_lst) == 1:
                                R_arrow_btn.config(state = DISABLED)


                            travel_date_font = tkinter.font.Font(family = "Times New Roman", size = 18)
                            travel_date_lbl = Label(new_plan_win, text = date_lst[cur_location_in_lst], font = travel_date_font, bg = "slate gray", fg = "White")
                            travel_date_lbl.place(x = 190, y = 10)

                            plan_frame = Frame(new_plan_win, height = 540, width = 470, relief = "sunken", bd = 2)
                            plan_frame.place(x = 5, y = 40)

                            time_lst = []

                            time_lst.extend("0" + str(i) + ":00" for i in range(0,10))
                            time_lst.extend("1" + str(i) + ":00" for i in range(0,10))
                            time_lst.extend(("2" + str(i) + ":00" for i in range(0,5)))

                            text_in_timelbl1 = ""
                            text_in_timelbl2 = ""
                            text_in_timelbl3 = ""
                            text_in_timelbl4 = ""
                            text_in_timelbl5 = ""
                            text_in_timelbl6 = ""
                            text_in_timelbl7 = ""
                            text_in_timelbl8 = ""
                            text_in_timelbl9 = ""
                            text_in_timelbl10 = ""
                            text_in_timelbl11 = ""
                            text_in_timelbl12 = ""
                            text_in_timelbl13 = ""
                            text_in_timelbl14 = ""
                            text_in_timelbl15 = ""
                            text_in_timelbl16 = ""
                            text_in_timelbl17 = ""
                            text_in_timelbl18 = ""
                            text_in_timelbl19 = ""
                            text_in_timelbl20 = ""
                            text_in_timelbl21 = ""
                            text_in_timelbl22 = ""
                            text_in_timelbl23 = ""
                            text_in_timelbl24 = ""



                            def apply_time():
                                time_Ent0_entry = time_Ent0.get()
                                if time_Ent0_entry in time_lst:
                                    location = time_lst.index(time_Ent0_entry)
                                    lbl_num = 1
                                    for i in range(location+1, 25):
                                        globals()["text_in_timelbl{}" .format(lbl_num)] = time_lst[i]
                                        lbl_num += 1
                                    
                                time_lbl1.configure(text = globals()['text_in_timelbl1'])
                                time_lbl2.configure(text = globals()['text_in_timelbl2'])
                                time_lbl3.configure(text = globals()['text_in_timelbl3'])
                                time_lbl4.configure(text = globals()['text_in_timelbl4'])
                                time_lbl5.configure(text = globals()['text_in_timelbl5'])
                                time_lbl6.configure(text = globals()['text_in_timelbl6'])
                                time_lbl7.configure(text = globals()['text_in_timelbl7'])
                                time_lbl8.configure(text = globals()['text_in_timelbl8'])
                                time_lbl9.configure(text = globals()['text_in_timelbl9'])
                                time_lbl10.configure(text = globals()['text_in_timelbl10'])
                                time_lbl11.configure(text = globals()['text_in_timelbl11'])
                                time_lbl12.configure(text = globals()['text_in_timelbl12'])
                                time_lbl13.configure(text = globals()['text_in_timelbl13'])
                                time_lbl14.configure(text = globals()['text_in_timelbl14'])
                                time_lbl15.configure(text = globals()['text_in_timelbl15'])
                                time_lbl16.configure(text = globals()['text_in_timelbl16'])
                                time_lbl17.configure(text = globals()['text_in_timelbl17'])
                                time_lbl18.configure(text = globals()['text_in_timelbl18'])
                                time_lbl19.configure(text = globals()['text_in_timelbl19'])
                                time_lbl20.configure(text = globals()['text_in_timelbl20'])
                                time_lbl21.configure(text = globals()['text_in_timelbl21'])
                                time_lbl22.configure(text = globals()['text_in_timelbl22'])
                                time_lbl23.configure(text = globals()['text_in_timelbl23'])
                                time_lbl24.configure(text = globals()['text_in_timelbl24'])

                            

                            str_time_txt = Button(plan_frame, text = "TIME", width = 5, height = 1, command = apply_time).grid(row = 0, column = 0, sticky=N+E+W+S)
                            
                            time_Ent0 = Entry(plan_frame, width = 5)
                            time_Ent0.insert(0, "")
                            time_Ent0.grid(row = 1, column = 0, sticky=N+E+W+S)

                            time_lbl1 = Label(plan_frame, text = text_in_timelbl1, width = 5, height = 1)
                            time_lbl2 = Label(plan_frame, text = text_in_timelbl2, width = 5, height = 1)
                            time_lbl3 = Label(plan_frame, text = text_in_timelbl3, width = 5, height = 1)
                            time_lbl4 = Label(plan_frame, text = text_in_timelbl4, width = 5, height = 1)
                            time_lbl5 = Label(plan_frame, text = text_in_timelbl5, width = 5, height = 1)
                            time_lbl6 = Label(plan_frame, text = text_in_timelbl6, width = 5, height = 1)
                            time_lbl7 = Label(plan_frame, text = text_in_timelbl7, width = 5, height = 1)
                            time_lbl8 = Label(plan_frame, text = text_in_timelbl8, width = 5, height = 1)
                            time_lbl9 = Label(plan_frame, text = text_in_timelbl9, width = 5, height = 1)
                            time_lbl10 = Label(plan_frame, text = text_in_timelbl10, width = 5, height = 1)
                            time_lbl11 = Label(plan_frame, text = text_in_timelbl11, width = 5, height = 1)
                            time_lbl12 = Label(plan_frame, text = text_in_timelbl12, width = 5, height = 1)
                            time_lbl13 = Label(plan_frame, text = text_in_timelbl13, width = 5, height = 1)
                            time_lbl14 = Label(plan_frame, text = text_in_timelbl14, width = 5, height = 1)
                            time_lbl15 = Label(plan_frame, text = text_in_timelbl15, width = 5, height = 1)
                            time_lbl16 = Label(plan_frame, text = text_in_timelbl16, width = 5, height = 1)
                            time_lbl17 = Label(plan_frame, text = text_in_timelbl17, width = 5, height = 1)
                            time_lbl18 = Label(plan_frame, text = text_in_timelbl18, width = 5, height = 1)
                            time_lbl19 = Label(plan_frame, text = text_in_timelbl19, width = 5, height = 1)
                            time_lbl20 = Label(plan_frame, text = text_in_timelbl20, width = 5, height = 1)
                            time_lbl21 = Label(plan_frame, text = text_in_timelbl21, width = 5, height = 1)
                            time_lbl22 = Label(plan_frame, text = text_in_timelbl22, width = 5, height = 1)
                            time_lbl23 = Label(plan_frame, text = text_in_timelbl23, width = 5, height = 1)
                            time_lbl24 = Label(plan_frame, text = text_in_timelbl24, width = 5, height = 1)


                            time_lbl1.grid(row = 2, column = 0, sticky=N+E+W+S)
                            time_lbl2.grid(row = 3, column = 0, sticky=N+E+W+S)
                            time_lbl3.grid(row = 4, column = 0, sticky=N+E+W+S)
                            time_lbl4.grid(row = 5, column = 0, sticky=N+E+W+S)
                            time_lbl5.grid(row = 6, column = 0, sticky=N+E+W+S)
                            time_lbl6.grid(row = 7, column = 0, sticky=N+E+W+S)
                            time_lbl7.grid(row = 8, column = 0, sticky=N+E+W+S)
                            time_lbl8.grid(row = 9, column = 0, sticky=N+E+W+S)
                            time_lbl9.grid(row = 10, column = 0, sticky=N+E+W+S)
                            time_lbl10.grid(row = 11, column = 0, sticky=N+E+W+S)
                            time_lbl11.grid(row = 12, column = 0, sticky=N+E+W+S)
                            time_lbl12.grid(row = 13, column = 0, sticky=N+E+W+S)
                            time_lbl13.grid(row = 14, column = 0, sticky=N+E+W+S)
                            time_lbl14.grid(row = 15, column = 0, sticky=N+E+W+S)
                            time_lbl15.grid(row = 16, column = 0, sticky=N+E+W+S)
                            time_lbl16.grid(row = 17, column = 0, sticky=N+E+W+S)
                            time_lbl17.grid(row = 18, column = 0, sticky=N+E+W+S)
                            time_lbl18.grid(row = 19, column = 0, sticky=N+E+W+S)
                            time_lbl19.grid(row = 20, column = 0, sticky=N+E+W+S)
                            time_lbl20.grid(row = 21, column = 0, sticky=N+E+W+S)
                            time_lbl21.grid(row = 22, column = 0, sticky=N+E+W+S)
                            time_lbl22.grid(row = 23, column = 0, sticky=N+E+W+S)
                            time_lbl23.grid(row = 24, column = 0, sticky=N+E+W+S)
                            time_lbl24.grid(row = 25, column = 0, sticky=N+E+W+S)



                            info_lbl = Label(plan_frame, text = "INFO", width = 59, height = 1).grid(row = 0, column = 1, sticky=N+E+W+S)

                            info_Ent0 = Entry(plan_frame, width = 59)
                            info_Ent1 = Entry(plan_frame, width = 59)
                            info_Ent2 = Entry(plan_frame, width = 59)
                            info_Ent3 = Entry(plan_frame, width = 59)
                            info_Ent4 = Entry(plan_frame, width = 59)
                            info_Ent5 = Entry(plan_frame, width = 59)
                            info_Ent6 = Entry(plan_frame, width = 59)
                            info_Ent7 = Entry(plan_frame, width = 59)
                            info_Ent8 = Entry(plan_frame, width = 59)
                            info_Ent9 = Entry(plan_frame, width = 59)
                            info_Ent10 = Entry(plan_frame, width = 59)
                            info_Ent11 = Entry(plan_frame, width = 59)
                            info_Ent12 = Entry(plan_frame, width = 59)
                            info_Ent13 = Entry(plan_frame, width = 59)
                            info_Ent14 = Entry(plan_frame, width = 59)
                            info_Ent15 = Entry(plan_frame, width = 59)
                            info_Ent16 = Entry(plan_frame, width = 59)
                            info_Ent17 = Entry(plan_frame, width = 59)
                            info_Ent18 = Entry(plan_frame, width = 59)
                            info_Ent19 = Entry(plan_frame, width = 59)
                            info_Ent20 = Entry(plan_frame, width = 59)
                            info_Ent21 = Entry(plan_frame, width = 59)
                            info_Ent22 = Entry(plan_frame, width = 59)
                            info_Ent23 = Entry(plan_frame, width = 59)
                            info_Ent24 = Entry(plan_frame, width = 59)

                            info_Ent0.grid(row = 1, column = 1, sticky=N+E+W+S)
                            info_Ent1.grid(row = 2, column = 1, sticky=N+E+W+S)
                            info_Ent2.grid(row = 3, column = 1, sticky=N+E+W+S)
                            info_Ent3.grid(row = 4, column = 1, sticky=N+E+W+S)
                            info_Ent4.grid(row = 5, column = 1, sticky=N+E+W+S)
                            info_Ent5.grid(row = 6, column = 1, sticky=N+E+W+S)
                            info_Ent6.grid(row = 7, column = 1, sticky=N+E+W+S)
                            info_Ent7.grid(row = 8, column = 1, sticky=N+E+W+S)
                            info_Ent8.grid(row = 9, column = 1, sticky=N+E+W+S)
                            info_Ent9.grid(row = 10, column = 1, sticky=N+E+W+S)
                            info_Ent10.grid(row =11, column = 1, sticky=N+E+W+S)
                            info_Ent11.grid(row = 12, column = 1, sticky=N+E+W+S)
                            info_Ent12.grid(row = 13, column = 1, sticky=N+E+W+S)
                            info_Ent13.grid(row = 14, column = 1, sticky=N+E+W+S)
                            info_Ent14.grid(row = 15, column = 1, sticky=N+E+W+S)
                            info_Ent15.grid(row = 16, column = 1, sticky=N+E+W+S)
                            info_Ent16.grid(row = 17, column = 1, sticky=N+E+W+S)
                            info_Ent17.grid(row = 18, column = 1, sticky=N+E+W+S)
                            info_Ent18.grid(row = 19, column = 1, sticky=N+E+W+S)
                            info_Ent19.grid(row = 20, column = 1, sticky=N+E+W+S)
                            info_Ent20.grid(row = 21, column = 1, sticky=N+E+W+S)
                            info_Ent21.grid(row = 22, column = 1, sticky=N+E+W+S)
                            info_Ent22.grid(row = 23, column = 1, sticky=N+E+W+S)
                            info_Ent23.grid(row = 24, column = 1, sticky=N+E+W+S)
                            info_Ent24.grid(row = 25, column = 1, sticky=N+E+W+S)

                            cur_date_file = "./1_plans_folder/" + "Plan_folder_{0}_{1}/" .format(State, temp_date_st_en) + date_lst[cur_location_in_lst][:4] + "_" + date_lst[cur_location_in_lst][5:7] + "_" + date_lst[cur_location_in_lst][8:]
                                
                            f = open("{0}.txt" .format(cur_date_file), "r")

                            fixed_lines = []

                            for i in range(26):
                                line = f.readline().strip()
                                fixed_lines.append(line)


                            time_Ent0.delete(0, END)
                            time_Ent0.insert(0, fixed_lines[0])
                            info_Ent0.delete(0, END)                                
                            info_Ent0.insert(0, fixed_lines[1])
                            info_Ent1.delete(0, END)                                
                            info_Ent1.insert(0, fixed_lines[2])
                            info_Ent2.delete(0, END)                                
                            info_Ent2.insert(0, fixed_lines[3])
                            info_Ent3.delete(0, END)                                
                            info_Ent3.insert(0, fixed_lines[4])
                            info_Ent4.delete(0, END)                              
                            info_Ent4.insert(0, fixed_lines[5])
                            info_Ent5.delete(0, END)                                
                            info_Ent5.insert(0, fixed_lines[6])
                            info_Ent6.delete(0, END)                                
                            info_Ent6.insert(0, fixed_lines[7])
                            info_Ent7.delete(0, END)                                
                            info_Ent7.insert(0, fixed_lines[8])
                            info_Ent8.delete(0, END)                                
                            info_Ent8.insert(0, fixed_lines[9])
                            info_Ent9.delete(0, END)                                
                            info_Ent9.insert(0, fixed_lines[10])
                            info_Ent10.delete(0, END)                                
                            info_Ent10.insert(0, fixed_lines[11])
                            info_Ent11.delete(0, END)                                
                            info_Ent11.insert(0, fixed_lines[12])
                            info_Ent12.delete(0, END)                                
                            info_Ent12.insert(0, fixed_lines[13])
                            info_Ent13.delete(0, END)                                
                            info_Ent13.insert(0, fixed_lines[14])
                            info_Ent14.delete(0, END)                                
                            info_Ent14.insert(0, fixed_lines[15])
                            info_Ent15.delete(0, END)                                
                            info_Ent15.insert(0, fixed_lines[16])
                            info_Ent16.delete(0, END)                                
                            info_Ent16.insert(0, fixed_lines[17])
                            info_Ent17.delete(0, END)                                
                            info_Ent17.insert(0, fixed_lines[18])
                            info_Ent18.delete(0, END)                                
                            info_Ent18.insert(0, fixed_lines[19])
                            info_Ent19.delete(0, END)                                
                            info_Ent19.insert(0, fixed_lines[20])
                            info_Ent20.delete(0, END)                                
                            info_Ent20.insert(0, fixed_lines[21])
                            info_Ent21.delete(0, END)                                
                            info_Ent21.insert(0, fixed_lines[22])
                            info_Ent22.delete(0, END)                                
                            info_Ent22.insert(0, fixed_lines[23])
                            info_Ent23.delete(0, END)                                
                            info_Ent23.insert(0, fixed_lines[24])
                            info_Ent24.delete(0, END)                                
                            info_Ent24.insert(0, fixed_lines[25])

                            f.close()


                            plan_done_btn = Button(new_plan_win, text = "done", padx = 5, pady = 5, command = plan_done_cmd).place(x = 420, y = 5)

                            new_plan_win.config(bg = "slate gray")
                            new_plan_win.mainloop()
                        
                        open_new_plan_win_win()
        

    done_btn = Button(new_plan_win_cho, text = "done", padx = 7, pady = 5, command = open_new_plan_win)
    done_btn.place(x = 420, y = 260)

    new_plan_win_cho.config(bg = "slate gray")
    new_plan_win_cho.mainloop()  


new_plan_photo = PhotoImage(file = "./imgs/new_plan_photo.png") 
new_plan_btn = Button(start_win, image = new_plan_photo, command = new_plan_cmd)
new_plan_btn.place(x = 410, y = 3)

# frame -------------------------------------------------------------------------------------------
bg_frame = Frame(start_win, width = 470, height = 510, relief = "sunken", bd = 2)
bg_frame.place(x = 5, y = 45)


# view previous visited place -------------------------------------------------------------------
def view_preplace_cmd():
    view_preplace_win = Tk()
    view_preplace_win.title("Visited places")

    view_preplace_win.geometry("480x600+500+100")
    view_preplace_win.resizable(False, False) 

    view_preplace_title_font = tkinter.font.Font(family = "Times New Roman", size = 18, weight = "bold")
    view_preplace_title_lbl = Label(view_preplace_win, padx = 5, pady = 5, text = "VISITED PLACE", font = view_preplace_title_font, fg = "White", bg = "slate gray")
    view_preplace_title_lbl.place(x = 170, y = 8)

    view_preplace_bg_frame = Frame(view_preplace_win, width = 470, height = 510, relief = "sunken", bd = 2)
    view_preplace_bg_frame.place(x = 5, y = 45)
    
    def create_preplace_cmd():

        create_place_win = Tk()
        create_place_win.title("Create place Info")

        create_place_win.geometry("480x600+500+100")
        create_place_win.resizable(False, False)

        place_file = "./imgs/view_place_photo.png"

        global place_imagee
        place_imagee = PhotoImage(file = place_file, master = create_place_win)
        place_image_lbl = Label(create_place_win, image = place_imagee, height = 180, width = 180)
        place_image_lbl.place(x = 20, y = 20)

        state_lbl = Label(create_place_win, text = "State :", bg = "slate gray", fg = "white").place(x = 230, y = 20)
        state_entry = Entry(create_place_win)
        state_entry.place(x = 300, y = 20)

        city_lbl = Label(create_place_win, text = "City :", bg = "slate gray", fg = "white").place(x = 230, y = 50)
        city_entry = Entry(create_place_win)
        city_entry.place(x = 300, y = 50)

        name_lbl = Label(create_place_win, text = "Name :", bg = "slate gray", fg = "white").place(x = 230, y = 80)
        name_entry = Entry(create_place_win)
        name_entry.place(x = 300, y = 80)

        global rating_text
        rating_text = 0.0

        def rating_l_cmd():
            global rating_text
            if rating_text == 0.0:
                rating_text = 0.0
            else:
                rating_text -= 0.5
            star_rating_lbl.config(text = rating_text)

        def rating_r_cmd():
            global rating_text
            if rating_text == 5.0:
                rating_text = 5.0
            else:
                rating_text += 0.5
            star_rating_lbl.config(text = rating_text)
        

        def search_result_cmd():
            state_cpw = state_entry.get()
            city_cpw = city_entry.get()
            name_cpw = name_entry.get()
            name_cpw_lst = name_cpw.split()
            name_cpw_lst_final = ""
            for thing in name_cpw_lst:
                if name_cpw_lst.index(thing) == (len(name_cpw_lst)-1):
                    name_cpw_lst_final += thing
                else:
                    name_cpw_lst_final += (thing + "+")


            wb.open("https://www.google.com/search?q={0}+{1}+{2}" .format(state_cpw, city_cpw, name_cpw_lst_final))

        global initial_dir

        initial_dir = os.path.join(os.path.expanduser("~"), "OneDrive", "바탕 화면")

        def change_photo_cmd():

            files = filedialog.askopenfilename(
                title="Choose one image file",
                filetypes=(("PNG file", "*.png"), ("all files", "*.*")),
                initialdir=initial_dir
            )

            global place_file

            place_file = files[0]

            while len(files) != 1:
                image_choose = msgbox.showwarning("warning", "please choose one image")

                files = filedialog.askopenfilenames(title = "choose image file", 
                filetypes=(("PNG file", "*.png"), ("all file", "*.*")),\
                initialdir = initial_dir) # r = 내용을 탈출 문자 상관없이 그대로 사용한다는 뜻

                place_file = files[0]

            place_file_resized = PIL.Image.open(place_file)
            place_file_resized = place_file_resized.resize((180, 180))
            place_file_resized.close()

            create_place_win.lift()

            global place_imagee
            place_imagee = PhotoImage(file = place_file, master = create_place_win)
            place_image_lbl.config(image = place_imagee)

        star_lbl = Label(create_place_win, text = "Rating :", bg = "slate gray", fg = "white").place(x = 230, y = 120)
        star_l_btn = Button(create_place_win, text = "<", bg = "slate gray", fg = "white", command = rating_l_cmd).place(x = 300,y = 120)
        star_rating_lbl = Label(create_place_win, text = rating_text, padx = 3, pady = 3)
        star_rating_lbl.place(x = 330, y = 120)
        star_r_btn = Button(create_place_win, text = ">", bg = "slate gray", fg = "white", command = rating_r_cmd).place(x = 370, y = 120)
        change_photo_btn = Button(create_place_win, text = "change photo", padx = 15, pady = 2, bg = "slate gray", fg = "white", command = change_photo_cmd).place(x = 230, y = 170)
        search_result_btn = Button(create_place_win, text = "search result", padx = 20, pady = 2, bg = "slate gray", fg = "white", command = search_result_cmd).place(x = 350, y = 170)

        info_lbl = Label(create_place_win, text = "info", bg = "slate gray", fg = "white").place(x = 10, y = 220)
        info_text = Text(create_place_win, width = 65, height = 23)
        info_text.place(x = 10, y = 245)

        def place_done_cmd():
            global state
            state = state_entry.get()
            city = city_entry.get()
            name = name_entry.get()
            star_rating = rating_text
            info = info_text.get("1.0", END)

            if state == "" or city == "" or name == "":
                select_all = msgbox.showwarning("warning", "please write all")
                create_place_win.lift()
            else:
                state_lst = list(state)
                state_lst_0 = state_lst[0]
                state_lst_0 = state_lst_0.upper()
                state_lst[0] = state_lst_0
                statee = "".join(state_lst)

                states_dict = { "Alabama":"AL", "Alaska":"AK", "Arizona":"AZ", "Arkansas":"AR", "California":"CA", "Colorado":"CO", "Connecticut":"CT", \
              "Delaware":"DE", "Washington":"WA", "Florida":"FL", "Georgia":"GA", "Hawaii":"HI", "Idaho":"ID", "Illinois":"IL", "Indiana":"IN" ,\
            "Iowa":"IA", "Kansas":"KS", "Kentucky":"KY", "Louisiana":"LA", "Maine":"ME", "Maryland":"MD", "Massachusetts":"MA", "Michigan":"MI" ,\
            "Minnesota":"MN", "Mississippi":"MS", "Missouri":"MO", "Montana":"MT", "Nebraska":"NE", "Nevada":"NV", "New Hampshire":"NH" ,\
            "New Jersey":"NJ", "New Mexico":"NM", "New York":"NY", "North Carolina":"NC", "North Dakota":"ND", "Ohio":"OH", "Oklahoma":"OK" ,\
            "Oregon":"OR", "Pennsylvania":"PA", "Rhode Island":"RI", "South Carolina":"SC", "South Dakota":"SD", "Tennessee":"TN", "Texas":"TX" ,\
            "Utah":"UT", "Vermont":"VT", "Virginia":"VA", "Wyoming":"WY", "West Virginia":"WV", "Wisconsin":"WI"}

                if statee not in states_dict:
                    wrong_state_name = msgbox.showwarning("warning", "wrong state name")
                    create_place_win.lift()
                else:
                    path = "./1_places_folder"

                    name_lst = name.split()
                    temp_name_for_file = ""
                    for word in name_lst:
                        if name_lst.index(word) == len(name_lst)-1:
                            temp_name_for_file += word
                        else:
                            temp_name_for_file += word + "_"

                    global place_file

                    f = open("{}/{}_{}_{}.txt" .format(path, state, city, temp_name_for_file), "w", encoding = "utf8")
                    f.write(place_file +"\n")
                    f.write(state + "\n")
                    f.write(city + "\n")
                    f.write(name + "\n")
                    f.write(str(star_rating) + "\n")
                    f.write(info)
                    f.close()

                    place_lstt = list(place_listbox.get(0, END))

                    if ("{}_{}_{}" .format(state, city, temp_name_for_file)) in place_lstt:
                        pass
                    else:
                        place_listbox.insert(END, "{}_{}_{}" .format(state, city, temp_name_for_file))

                    create_place_win.destroy()
                    view_preplace_win.lift()


        place_done_btn = Button(create_place_win, text = "done", padx = 5, pady = 5, command = place_done_cmd).place(x = 225, y = 560)

        place_image_lbl.config(image = place_imagee)
        create_place_win.config(bg = "slate gray")
        create_place_win.mainloop()

    preplace_open_btn = Button(view_preplace_win, text = "create", padx = 5, pady = 5, command = create_preplace_cmd)
    preplace_open_btn.place(x = 425, y = 560)

    def delete_preplace_cmd():
        selected = place_listbox.curselection()
        sselected = place_listbox.get(selected)

        path = "./1_places_folder/"

        file = "{}{}.txt" .format(path, sselected)

        os.remove("{}{}.txt" .format(path, sselected))

        place_listbox.delete(selected)
        

    preplace_delete_btn = Button(view_preplace_win, text = "delete", padx = 5, pady = 5, command = delete_preplace_cmd)
    preplace_delete_btn.place(x = 8, y = 560)

    def open_preplace_cmd():
        if len(place_listbox.curselection()) == 1:
            
            create_place_win = Tk()
            create_place_win.title("Create place Info")

            create_place_win.geometry("480x600+500+100")
            create_place_win.resizable(False, False)

            place_imagee = PhotoImage(file = "./imgs/view_place_photo.png", master = create_place_win)
            place_image_lbl = Label(create_place_win, image = place_imagee, height = 180, width = 180)
            place_image_lbl.place(x = 20, y = 20)

            state_lbl = Label(create_place_win, text = "State :", bg = "slate gray", fg = "white").place(x = 230, y = 20)
            state_entry = Entry(create_place_win)
            state_entry.place(x = 300, y = 20)

            city_lbl = Label(create_place_win, text = "City :", bg = "slate gray", fg = "white").place(x = 230, y = 50)
            city_entry = Entry(create_place_win)
            city_entry.place(x = 300, y = 50)

            name_lbl = Label(create_place_win, text = "Name :", bg = "slate gray", fg = "white").place(x = 230, y = 80)
            name_entry = Entry(create_place_win)
            name_entry.place(x = 300, y = 80)

            global rating_text
            rating_text = 0.0

            def rating_l_cmd():
                global rating_text
                if rating_text == 0.0:
                    rating_text = 0.0
                else:
                    rating_text -= 0.5
                star_rating_lbl.config(text = rating_text)

            def rating_r_cmd():
                global rating_text
                if rating_text == 5.0:
                    rating_text = 5.0
                else:
                    rating_text += 0.5
                star_rating_lbl.config(text = rating_text)
            

            def search_result_cmd():
                state_cpw = state_entry.get()
                city_cpw = city_entry.get()
                name_cpw = name_entry.get()
                name_cpw_lst = name_cpw.split()
                name_cpw_lst_final = ""
                for thing in name_cpw_lst:
                    if name_cpw_lst.index(thing) == (len(name_cpw_lst)-1):
                        name_cpw_lst_final += thing
                    else:
                        name_cpw_lst_final += (thing + "+")


                wb.open("https://www.google.com/search?q={0}+{1}+{2}" .format(state_cpw, city_cpw, name_cpw_lst_final))

            def change_photo_cmd():
                files = filedialog.askopenfilenames(title = "choose image file", 
                filetypes=(("PNG file", "*.png"), ("all file", "*.*")),\
                initialdir= initial_dir) # r = 내용을 탈출 문자 상관없이 그대로 사용한다는 뜻

                global place_file

                place_file = files[0]

                while len(files) != 1:
                    image_choose = msgbox.showwarning("warning", "please choose one image")

                    files = filedialog.askopenfilenames(title = "choose image file", 
                    filetypes=(("PNG file", "*.png"), ("all file", "*.*")),\
                    initialdir= initial_dir) # r = 내용을 탈출 문자 상관없이 그대로 사용한다는 뜻

                    place_file = files[0]


                place_file_resized = PIL.Image.open(place_file)
                place_file_resized = place_file_resized.resize((180, 180))
                place_file_resized.close()

                create_place_win.lift()

                global place_imagee
                place_imagee = PhotoImage(file = place_file, master = create_place_win)
                place_image_lbl.config(image = place_imagee)

                create_place_win.lift()

            star_lbl = Label(create_place_win, text = "Rating :", bg = "slate gray", fg = "white")
            star_lbl.place(x = 230, y = 120)
            star_l_btn = Button(create_place_win, text = "<", bg = "slate gray", fg = "white", command = rating_l_cmd).place(x = 300,y = 120)
            star_rating_lbl = Label(create_place_win, text = rating_text, padx = 3, pady = 3)
            star_rating_lbl.place(x = 330, y = 120)
            star_r_btn = Button(create_place_win, text = ">", bg = "slate gray", fg = "white", command = rating_r_cmd).place(x = 370, y = 120)
            change_photo_btn = Button(create_place_win, text = "change photo", padx = 15, pady = 2, bg = "slate gray", fg = "white", command = change_photo_cmd).place(x = 230, y = 170)
            search_result_btn = Button(create_place_win, text = "search result", padx = 20, pady = 2, bg = "slate gray", fg = "white", command = search_result_cmd).place(x = 350, y = 170)

            info_lbl = Label(create_place_win, text = "info", bg = "slate gray", fg = "white").place(x = 10, y = 220)
            info_text = Text(create_place_win, width = 65, height = 23)
            info_text.place(x = 10, y = 245)

            selected = place_listbox.curselection()
            sselected = place_listbox.get(selected)

            path = "./1_places_folder/"

            f = open('{}{}.txt' .format(path, sselected), "r", encoding = "utf8")
            place_file = (f.readline()[:-1])
            place_imagee = PhotoImage(file = place_file, master = create_place_win)
            place_image_lbl.config(image = place_imagee)
            state_get = (f.readline()).split()
            state_entry.insert(0, state_get)
            city_get = (f.readline()).split()
            city_entry.insert(0, city_get)
            name_get = (f.readline()).split()
            name_entry.insert(0, name_get)
            rating_text = f.readline().split()
            rating_text = float(rating_text[0])
            star_rating_lbl.config(text = rating_text)
            info_lines = f.readlines()
            for line in info_lines:
                info_text.insert(END, line)
            f.close()

            def place_done_cmd():
                global state
                state = state_get[0]
                city = city_get[0]
                name = name_get
                name = " ".join(name)
                star_rating = rating_text
                info = info_text.get("1.0", END)

                if state == "" or city == "" or name == "":
                    select_all = msgbox.showwarning("warning", "please write all")
                    create_place_win.lift()
                else:
                    state_lst = list(state)
                    state_lst[0] = state_lst[0].upper()
                    statee = "".join(state_lst)

                    states_dict = { "Alabama":"AL", "Alaska":"AK", "Arizona":"AZ", "Arkansas":"AR", "California":"CA", "Colorado":"CO", "Connecticut":"CT", \
                "Delaware":"DE", "Washington":"WA", "Florida":"FL", "Georgia":"GA", "Hawaii":"HI", "Idaho":"ID", "Illinois":"IL", "Indiana":"IN" ,\
                "Iowa":"IA", "Kansas":"KS", "Kentucky":"KY", "Louisiana":"LA", "Maine":"ME", "Maryland":"MD", "Massachusetts":"MA", "Michigan":"MI" ,\
                "Minnesota":"MN", "Mississippi":"MS", "Missouri":"MO", "Montana":"MT", "Nebraska":"NE", "Nevada":"NV", "New Hampshire":"NH" ,\
                "New Jersey":"NJ", "New Mexico":"NM", "New York":"NY", "North Carolina":"NC", "North Dakota":"ND", "Ohio":"OH", "Oklahoma":"OK" ,\
                "Oregon":"OR", "Pennsylvania":"PA", "Rhode Island":"RI", "South Carolina":"SC", "South Dakota":"SD", "Tennessee":"TN", "Texas":"TX" ,\
                "Utah":"UT", "Vermont":"VT", "Virginia":"VA", "Wyoming":"WY", "West Virginia":"WV", "Wisconsin":"WI"}

                    if statee not in states_dict:
                        wrong_state_name = msgbox.showwarning("warning", "wrong state name")
                        create_place_win.lift()
                    else:
                        path = "./1_places_folder"

                        temp_name_for_file = ""
                        name_lst = name.split()
                        for word in name_lst:
                            if name_lst.index(word) == len(name_lst)-1:
                                temp_name_for_file += word
                            else:
                                temp_name_for_file += word + "_"

                        f = open("{}/{}_{}_{}.txt" .format(path, state, city, temp_name_for_file), "w", encoding = "utf8")
                        f.write(place_file +"\n")
                        f.write(state + "\n") 
                        f.write(city + "\n")
                        f.write(name + "\n")
                        f.write(str(star_rating) + "\n")
                        f.write(info)
                        f.close()

                        place_listbox.config()

                        create_place_win.destroy()
                        view_preplace_win.lift()

            place_done_btn = Button(create_place_win, text = "done", padx = 5, pady = 5, command = place_done_cmd).place(x = 225, y = 560)
            create_place_win.config(bg = "slate gray")
            create_place_win.mainloop()


    preplace_open_btn = Button(view_preplace_win, text = "open", padx = 5, pady = 5, command = open_preplace_cmd)
    preplace_open_btn.place(x = 430, y = 7)

    listbox_font = tkinter.font.Font(size = 20)

    place_listbox = Listbox(view_preplace_bg_frame, selectmode = "single", width = 42, height = 24, bd= 2, fg = "black", font = listbox_font)

    folder_path = "./1_places_folder"

    place_lst = os.listdir(folder_path)

    for i in range(len(place_lst)):
        place_listbox.insert(END, place_lst[i][:-4])

    place_listbox.pack()


    view_preplace_bg_frame.config()
    view_preplace_win.config(bg = "slate gray")
    view_preplace_win.mainloop()  

view_preplace_photo = PhotoImage(file = "./imgs/view_preplace_photo.png")
view_preplace_btn = Button(start_win, image = view_preplace_photo, padx = 5, pady = 5,  command = view_preplace_cmd)
view_preplace_btn.place(x = 420, y = 560)

# view previous plan btn -------------------------------------------------------------------------
def view_preplan_cmd():
    view_preplan_win = Tk()
    view_preplan_win.title("My plan book")

    view_preplan_win.geometry("480x600+500+100")
    view_preplan_win.resizable(False, False) 

    view_preplan_title_font = tkinter.font.Font(family = "Times New Roman", size = 18, weight = "bold")

    view_preplan_title_lbl = Label(view_preplan_win, padx = 5, pady = 10, text = "MY PLANS", font = view_preplan_title_font, fg = "White", bg = "slate gray")
    view_preplan_title_lbl.place(x = 190, y = 5)

    view_preplan_bg_frame = Frame(view_preplan_win, width = 470, height = 550, relief = "sunken", bd = 2)
    view_preplan_bg_frame.place(x = 5, y = 45)

    def open_preplan_cmd():
        selected = plan_listbox.curselection()
        selected = plan_listbox.get(selected)


        State = str(selected[9:-32])
        st_y = str(selected[-23:-19])
        st_m = str(selected[-18:-16])
        st_d = str(selected[-15:-13])
        en_y = str(selected[-10:-6])
        en_m = str(selected[-5:-3])
        en_d = str(selected[-2:])

        def date_range(start, end):
            start = datetime.strptime(start, "%Y/%m/%d")
            end = datetime.strptime(end, "%Y/%m/%d")
            dates = [(start + timedelta(days=i)).strftime("%Y/%m/%d") for i in range((end-start).days+1)]
            return dates
        
        date_lst = date_range(st_y + "/" + st_m + "/" + st_d, en_y + "/" + en_m + "/" + en_d)

        temp_date_st_en = date_lst[0][:4] + "_" + date_lst[0][5:7] + "_" + date_lst[0][8:] + "__" + date_lst[-1][:4] + "_" + date_lst[-1][5:7] + "_" + date_lst[-1][8:]

        new_plan_win = Tk()
        new_plan_win.title("Create New Plan")

        new_plan_win.geometry("480x600+500+100")
        new_plan_win.resizable(False, False)  

        global cur_location_in_lst
        cur_location_in_lst = 0


        def plan_done_cmd():
            get_lst = []
            cur_location_name = date_lst[cur_location_in_lst][:4] + "_" + date_lst[cur_location_in_lst][5:7] + "_" + date_lst[cur_location_in_lst][8:]
            f = open("{0}{1}.txt" .format(make_dir_name, cur_location_name), "w")
            f.write(time_Ent0.get())
            get_lst.append(info_Ent0.get())
            get_lst.append(info_Ent1.get())
            get_lst.append(info_Ent2.get())
            get_lst.append(info_Ent3.get())
            get_lst.append(info_Ent4.get())
            get_lst.append(info_Ent5.get())
            get_lst.append(info_Ent6.get())
            get_lst.append(info_Ent7.get())
            get_lst.append(info_Ent8.get())
            get_lst.append(info_Ent9.get())
            get_lst.append(info_Ent10.get())
            get_lst.append(info_Ent11.get())
            get_lst.append(info_Ent12.get())
            get_lst.append(info_Ent13.get())
            get_lst.append(info_Ent14.get())
            get_lst.append(info_Ent15.get())
            get_lst.append(info_Ent16.get())
            get_lst.append(info_Ent17.get())
            get_lst.append(info_Ent18.get())
            get_lst.append(info_Ent19.get())
            get_lst.append(info_Ent20.get())
            get_lst.append(info_Ent21.get())
            get_lst.append(info_Ent22.get())
            get_lst.append(info_Ent23.get())
            get_lst.append(info_Ent24.get())
            for i in range(0, 25):
                f.write("\n" + "{0}" .format(get_lst[i]))
            f.close()


            new_plan_win.destroy()

        def L_arrow_cmd():
            time_lbl1.configure(text = "")
            time_lbl2.configure(text = "")
            time_lbl3.configure(text = "")
            time_lbl4.configure(text = "")
            time_lbl6.configure(text = "")
            time_lbl5.configure(text = "")
            time_lbl7.configure(text = "")
            time_lbl8.configure(text = "")
            time_lbl9.configure(text = "")
            time_lbl10.configure(text = "")
            time_lbl11.configure(text = "")
            time_lbl12.configure(text = "")
            time_lbl13.configure(text = "")
            time_lbl14.configure(text = "")
            time_lbl15.configure(text = "")
            time_lbl16.configure(text = "")
            time_lbl17.configure(text = "")
            time_lbl18.configure(text = "")
            time_lbl19.configure(text = "")
            time_lbl20.configure(text = "")
            time_lbl21.configure(text = "")
            time_lbl22.configure(text = "")
            time_lbl23.configure(text = "")
            time_lbl24.configure(text = "")


            global cur_location_in_lst
            cur_location_in_lst -= 1
            if len(date_lst) == 1:
                L_arrow_btn.config(state = DISABLED)
            else:
                if cur_location_in_lst == 0:
                    L_arrow_btn.config(state = DISABLED)

                if cur_location_in_lst < len(date_lst):
                    R_arrow_btn.config(state = NORMAL)
                travel_date_lbl.config(text = date_lst[cur_location_in_lst])

            
            get_lst = []
            cur_location_name = date_lst[cur_location_in_lst+1][:4] + "_" + date_lst[cur_location_in_lst+1][5:7] + "_" + date_lst[cur_location_in_lst+1][8:]
            f = open("{0}{1}.txt" .format(make_dir_name, cur_location_name), "w")
            f.write(time_Ent0.get())
            get_lst.append(info_Ent0.get())
            get_lst.append(info_Ent1.get())
            get_lst.append(info_Ent2.get())
            get_lst.append(info_Ent3.get())
            get_lst.append(info_Ent4.get())
            get_lst.append(info_Ent5.get())
            get_lst.append(info_Ent6.get())
            get_lst.append(info_Ent7.get())
            get_lst.append(info_Ent8.get())
            get_lst.append(info_Ent9.get())
            get_lst.append(info_Ent10.get())
            get_lst.append(info_Ent11.get())
            get_lst.append(info_Ent12.get())
            get_lst.append(info_Ent13.get())
            get_lst.append(info_Ent14.get())
            get_lst.append(info_Ent15.get())
            get_lst.append(info_Ent16.get())
            get_lst.append(info_Ent17.get())
            get_lst.append(info_Ent18.get())
            get_lst.append(info_Ent19.get())
            get_lst.append(info_Ent20.get())
            get_lst.append(info_Ent21.get())
            get_lst.append(info_Ent22.get())
            get_lst.append(info_Ent23.get())
            get_lst.append(info_Ent24.get())
            for i in range(0, 25):
                f.write("\n"+ "{0}" .format(get_lst[i]))
            f.close()


            cur_date_file = "./1_plans_folder/" + "Plan_folder_{0}_{1}/" .format(State, temp_date_st_en) + date_lst[cur_location_in_lst][:4] + "_" + date_lst[cur_location_in_lst][5:7] + "_" + date_lst[cur_location_in_lst][8:]
            
            f = open("{0}.txt" .format(cur_date_file), "r")

            fixed_lines = []

            for i in range(26):
                line = f.readline().strip()
                fixed_lines.append(line)


            time_Ent0.delete(0, END)
            time_Ent0.insert(0, fixed_lines[0])
            info_Ent0.delete(0, END)            
            info_Ent0.insert(0, fixed_lines[1])
            info_Ent1.delete(0, END)            
            info_Ent1.insert(0, fixed_lines[2])
            info_Ent2.delete(0, END)            
            info_Ent2.insert(0, fixed_lines[3])
            info_Ent3.delete(0, END)            
            info_Ent3.insert(0, fixed_lines[4])
            info_Ent4.delete(0, END)          
            info_Ent4.insert(0, fixed_lines[5])
            info_Ent5.delete(0, END)            
            info_Ent5.insert(0, fixed_lines[6])
            info_Ent6.delete(0, END)            
            info_Ent6.insert(0, fixed_lines[7])
            info_Ent7.delete(0, END)            
            info_Ent7.insert(0, fixed_lines[8])
            info_Ent8.delete(0, END)            
            info_Ent8.insert(0, fixed_lines[9])
            info_Ent9.delete(0, END)            
            info_Ent9.insert(0, fixed_lines[10])
            info_Ent10.delete(0, END)            
            info_Ent10.insert(0, fixed_lines[11])
            info_Ent11.delete(0, END)            
            info_Ent11.insert(0, fixed_lines[12])
            info_Ent12.delete(0, END)            
            info_Ent12.insert(0, fixed_lines[13])
            info_Ent13.delete(0, END)            
            info_Ent13.insert(0, fixed_lines[14])
            info_Ent14.delete(0, END)            
            info_Ent14.insert(0, fixed_lines[15])
            info_Ent15.delete(0, END)            
            info_Ent15.insert(0, fixed_lines[16])
            info_Ent16.delete(0, END)            
            info_Ent16.insert(0, fixed_lines[17])
            info_Ent17.delete(0, END)            
            info_Ent17.insert(0, fixed_lines[18])
            info_Ent18.delete(0, END)            
            info_Ent18.insert(0, fixed_lines[19])
            info_Ent19.delete(0, END)            
            info_Ent19.insert(0, fixed_lines[20])
            info_Ent20.delete(0, END)            
            info_Ent20.insert(0, fixed_lines[21])
            info_Ent21.delete(0, END)            
            info_Ent21.insert(0, fixed_lines[22])
            info_Ent22.delete(0, END)            
            info_Ent22.insert(0, fixed_lines[23])
            info_Ent23.delete(0, END)            
            info_Ent23.insert(0, fixed_lines[24])
            info_Ent24.delete(0, END)            
            info_Ent24.insert(0, fixed_lines[25])

            f.close()

        path = "./1_plans_folder/"

        global make_dir_name
        make_dir_name = path + "Plan_folder_{0}_{1}/" .format(State, temp_date_st_en)

        L_arrow_font = tkinter.font.Font(family = "Times New Roman", size = 12)
        L_arrow_btn = Button(new_plan_win, text = "<", font = L_arrow_font, command = L_arrow_cmd, state = DISABLED)
        L_arrow_btn.place(x = 150, y = 5)

        def R_arrow_cmd():
            time_lbl1.configure(text = "")
            time_lbl2.configure(text = "")
            time_lbl3.configure(text = "")
            time_lbl4.configure(text = "")
            time_lbl6.configure(text = "")
            time_lbl5.configure(text = "")
            time_lbl7.configure(text = "")
            time_lbl8.configure(text = "")
            time_lbl9.configure(text = "")
            time_lbl10.configure(text = "")
            time_lbl11.configure(text = "")
            time_lbl12.configure(text = "")
            time_lbl13.configure(text = "")
            time_lbl14.configure(text = "")
            time_lbl15.configure(text = "")
            time_lbl16.configure(text = "")
            time_lbl17.configure(text = "")
            time_lbl18.configure(text = "")
            time_lbl19.configure(text = "")
            time_lbl20.configure(text = "")
            time_lbl21.configure(text = "")
            time_lbl22.configure(text = "")
            time_lbl23.configure(text = "")
            time_lbl24.configure(text = "")

            global cur_location_in_lst
            cur_location_in_lst += 1    
            if cur_location_in_lst == (len(date_lst)-1):
                R_arrow_btn.config(state = DISABLED)

            if cur_location_in_lst > 0:
                L_arrow_btn.config(state = NORMAL)
            travel_date_lbl.config(text = date_lst[cur_location_in_lst])
            
            get_lst = []
            cur_location_name = date_lst[cur_location_in_lst-1][:4] + "_" + date_lst[cur_location_in_lst-1][5:7] + "_" + date_lst[cur_location_in_lst-1][8:]
            global make_dir_name
            f = open("{0}{1}.txt" .format(make_dir_name, cur_location_name), "w")
            f.write(time_Ent0.get())
            get_lst.append(info_Ent0.get())
            get_lst.append(info_Ent1.get())
            get_lst.append(info_Ent2.get())
            get_lst.append(info_Ent3.get())
            get_lst.append(info_Ent4.get())
            get_lst.append(info_Ent5.get())
            get_lst.append(info_Ent6.get())
            get_lst.append(info_Ent7.get())
            get_lst.append(info_Ent8.get())
            get_lst.append(info_Ent9.get())
            get_lst.append(info_Ent10.get())
            get_lst.append(info_Ent11.get())
            get_lst.append(info_Ent12.get())
            get_lst.append(info_Ent13.get())
            get_lst.append(info_Ent14.get())
            get_lst.append(info_Ent15.get())
            get_lst.append(info_Ent16.get())
            get_lst.append(info_Ent17.get())
            get_lst.append(info_Ent18.get())
            get_lst.append(info_Ent19.get())
            get_lst.append(info_Ent20.get())
            get_lst.append(info_Ent21.get())
            get_lst.append(info_Ent22.get())
            get_lst.append(info_Ent23.get())
            get_lst.append(info_Ent24.get())

            for i in range(0, 25):
                f.write("\n" + "{0}" .format(get_lst[i]))
            f.close()

            cur_date_file = "./1_plans_folder/" + "Plan_folder_{0}_{1}/" .format(State, temp_date_st_en) + date_lst[cur_location_in_lst][:4] + "_" + date_lst[cur_location_in_lst][5:7] + "_" + date_lst[cur_location_in_lst][8:]
            
            f = open("{0}.txt" .format(cur_date_file), "r")

            fixed_lines = []

            for i in range(26):
                line = f.readline().strip()
                fixed_lines.append(line)


            time_Ent0.delete(0, END)
            time_Ent0.insert(0, fixed_lines[0])
            info_Ent0.delete(0, END)            
            info_Ent0.insert(0, fixed_lines[1])
            info_Ent1.delete(0, END)            
            info_Ent1.insert(0, fixed_lines[2])
            info_Ent2.delete(0, END)            
            info_Ent2.insert(0, fixed_lines[3])
            info_Ent3.delete(0, END)            
            info_Ent3.insert(0, fixed_lines[4])
            info_Ent4.delete(0, END)          
            info_Ent4.insert(0, fixed_lines[5])
            info_Ent5.delete(0, END)            
            info_Ent5.insert(0, fixed_lines[6])
            info_Ent6.delete(0, END)            
            info_Ent6.insert(0, fixed_lines[7])
            info_Ent7.delete(0, END)            
            info_Ent7.insert(0, fixed_lines[8])
            info_Ent8.delete(0, END)            
            info_Ent8.insert(0, fixed_lines[9])
            info_Ent9.delete(0, END)            
            info_Ent9.insert(0, fixed_lines[10])
            info_Ent10.delete(0, END)            
            info_Ent10.insert(0, fixed_lines[11])
            info_Ent11.delete(0, END)            
            info_Ent11.insert(0, fixed_lines[12])
            info_Ent12.delete(0, END)            
            info_Ent12.insert(0, fixed_lines[13])
            info_Ent13.delete(0, END)            
            info_Ent13.insert(0, fixed_lines[14])
            info_Ent14.delete(0, END)            
            info_Ent14.insert(0, fixed_lines[15])
            info_Ent15.delete(0, END)            
            info_Ent15.insert(0, fixed_lines[16])
            info_Ent16.delete(0, END)            
            info_Ent16.insert(0, fixed_lines[17])
            info_Ent17.delete(0, END)            
            info_Ent17.insert(0, fixed_lines[18])
            info_Ent18.delete(0, END)            
            info_Ent18.insert(0, fixed_lines[19])
            info_Ent19.delete(0, END)            
            info_Ent19.insert(0, fixed_lines[20])
            info_Ent20.delete(0, END)            
            info_Ent20.insert(0, fixed_lines[21])
            info_Ent21.delete(0, END)            
            info_Ent21.insert(0, fixed_lines[22])
            info_Ent22.delete(0, END)            
            info_Ent22.insert(0, fixed_lines[23])
            info_Ent23.delete(0, END)            
            info_Ent23.insert(0, fixed_lines[24])
            info_Ent24.delete(0, END)            
            info_Ent24.insert(0, fixed_lines[25])

            f.close()


        R_arrow_font = tkinter.font.Font(family = "Times New Roman", size = 12)
        R_arrow_btn = Button(new_plan_win, text = ">", font = R_arrow_font, command = R_arrow_cmd)
        R_arrow_btn.place(x = 310, y = 5)

        if len(date_lst) == 1:
            R_arrow_btn.config(state = DISABLED)


        travel_date_font = tkinter.font.Font(family = "Times New Roman", size = 18)
        travel_date_lbl = Label(new_plan_win, text = date_lst[cur_location_in_lst], font = travel_date_font, bg = "slate gray", fg = "White")
        travel_date_lbl.place(x = 190, y = 10)

        plan_frame = Frame(new_plan_win, height = 540, width = 470, relief = "sunken", bd = 2)
        plan_frame.place(x = 5, y = 40)

        time_lst = []

        time_lst.extend("0" + str(i) + ":00" for i in range(0,10))
        time_lst.extend("1" + str(i) + ":00" for i in range(0,10))
        time_lst.extend(("2" + str(i) + ":00" for i in range(0,5)))

        text_in_timelbl1 = ""
        text_in_timelbl2 = ""
        text_in_timelbl3 = ""
        text_in_timelbl4 = ""
        text_in_timelbl5 = ""
        text_in_timelbl6 = ""
        text_in_timelbl7 = ""
        text_in_timelbl8 = ""
        text_in_timelbl9 = ""
        text_in_timelbl10 = ""
        text_in_timelbl11 = ""
        text_in_timelbl12 = ""
        text_in_timelbl13 = ""
        text_in_timelbl14 = ""
        text_in_timelbl15 = ""
        text_in_timelbl16 = ""
        text_in_timelbl17 = ""
        text_in_timelbl18 = ""
        text_in_timelbl19 = ""
        text_in_timelbl20 = ""
        text_in_timelbl21 = ""
        text_in_timelbl22 = ""
        text_in_timelbl23 = ""
        text_in_timelbl24 = ""



        def apply_time():
            time_Ent0_entry = time_Ent0.get()
            if time_Ent0_entry in time_lst:
                location = time_lst.index(time_Ent0_entry)
                lbl_num = 1
                for i in range(location+1, 25):
                    globals()["text_in_timelbl{}" .format(lbl_num)] = time_lst[i]
                    lbl_num += 1
                
            time_lbl1.configure(text = globals()['text_in_timelbl1'])
            time_lbl2.configure(text = globals()['text_in_timelbl2'])
            time_lbl3.configure(text = globals()['text_in_timelbl3'])
            time_lbl4.configure(text = globals()['text_in_timelbl4'])
            time_lbl5.configure(text = globals()['text_in_timelbl5'])
            time_lbl6.configure(text = globals()['text_in_timelbl6'])
            time_lbl7.configure(text = globals()['text_in_timelbl7'])
            time_lbl8.configure(text = globals()['text_in_timelbl8'])
            time_lbl9.configure(text = globals()['text_in_timelbl9'])
            time_lbl10.configure(text = globals()['text_in_timelbl10'])
            time_lbl11.configure(text = globals()['text_in_timelbl11'])
            time_lbl12.configure(text = globals()['text_in_timelbl12'])
            time_lbl13.configure(text = globals()['text_in_timelbl13'])
            time_lbl14.configure(text = globals()['text_in_timelbl14'])
            time_lbl15.configure(text = globals()['text_in_timelbl15'])
            time_lbl16.configure(text = globals()['text_in_timelbl16'])
            time_lbl17.configure(text = globals()['text_in_timelbl17'])
            time_lbl18.configure(text = globals()['text_in_timelbl18'])
            time_lbl19.configure(text = globals()['text_in_timelbl19'])
            time_lbl20.configure(text = globals()['text_in_timelbl20'])
            time_lbl21.configure(text = globals()['text_in_timelbl21'])
            time_lbl22.configure(text = globals()['text_in_timelbl22'])
            time_lbl23.configure(text = globals()['text_in_timelbl23'])
            time_lbl24.configure(text = globals()['text_in_timelbl24'])

        

        str_time_txt = Button(plan_frame, text = "TIME", width = 5, height = 1, command = apply_time).grid(row = 0, column = 0, sticky=N+E+W+S)
        
        time_Ent0 = Entry(plan_frame, width = 5)
        time_Ent0.insert(0, "")
        time_Ent0.grid(row = 1, column = 0, sticky=N+E+W+S)

        time_lbl1 = Label(plan_frame, text = text_in_timelbl1, width = 5, height = 1)
        time_lbl2 = Label(plan_frame, text = text_in_timelbl2, width = 5, height = 1)
        time_lbl3 = Label(plan_frame, text = text_in_timelbl3, width = 5, height = 1)
        time_lbl4 = Label(plan_frame, text = text_in_timelbl4, width = 5, height = 1)
        time_lbl5 = Label(plan_frame, text = text_in_timelbl5, width = 5, height = 1)
        time_lbl6 = Label(plan_frame, text = text_in_timelbl6, width = 5, height = 1)
        time_lbl7 = Label(plan_frame, text = text_in_timelbl7, width = 5, height = 1)
        time_lbl8 = Label(plan_frame, text = text_in_timelbl8, width = 5, height = 1)
        time_lbl9 = Label(plan_frame, text = text_in_timelbl9, width = 5, height = 1)
        time_lbl10 = Label(plan_frame, text = text_in_timelbl10, width = 5, height = 1)
        time_lbl11 = Label(plan_frame, text = text_in_timelbl11, width = 5, height = 1)
        time_lbl12 = Label(plan_frame, text = text_in_timelbl12, width = 5, height = 1)
        time_lbl13 = Label(plan_frame, text = text_in_timelbl13, width = 5, height = 1)
        time_lbl14 = Label(plan_frame, text = text_in_timelbl14, width = 5, height = 1)
        time_lbl15 = Label(plan_frame, text = text_in_timelbl15, width = 5, height = 1)
        time_lbl16 = Label(plan_frame, text = text_in_timelbl16, width = 5, height = 1)
        time_lbl17 = Label(plan_frame, text = text_in_timelbl17, width = 5, height = 1)
        time_lbl18 = Label(plan_frame, text = text_in_timelbl18, width = 5, height = 1)
        time_lbl19 = Label(plan_frame, text = text_in_timelbl19, width = 5, height = 1)
        time_lbl20 = Label(plan_frame, text = text_in_timelbl20, width = 5, height = 1)
        time_lbl21 = Label(plan_frame, text = text_in_timelbl21, width = 5, height = 1)
        time_lbl22 = Label(plan_frame, text = text_in_timelbl22, width = 5, height = 1)
        time_lbl23 = Label(plan_frame, text = text_in_timelbl23, width = 5, height = 1)
        time_lbl24 = Label(plan_frame, text = text_in_timelbl24, width = 5, height = 1)


        time_lbl1.grid(row = 2, column = 0, sticky=N+E+W+S)
        time_lbl2.grid(row = 3, column = 0, sticky=N+E+W+S)
        time_lbl3.grid(row = 4, column = 0, sticky=N+E+W+S)
        time_lbl4.grid(row = 5, column = 0, sticky=N+E+W+S)
        time_lbl5.grid(row = 6, column = 0, sticky=N+E+W+S)
        time_lbl6.grid(row = 7, column = 0, sticky=N+E+W+S)
        time_lbl7.grid(row = 8, column = 0, sticky=N+E+W+S)
        time_lbl8.grid(row = 9, column = 0, sticky=N+E+W+S)
        time_lbl9.grid(row = 10, column = 0, sticky=N+E+W+S)
        time_lbl10.grid(row = 11, column = 0, sticky=N+E+W+S)
        time_lbl11.grid(row = 12, column = 0, sticky=N+E+W+S)
        time_lbl12.grid(row = 13, column = 0, sticky=N+E+W+S)
        time_lbl13.grid(row = 14, column = 0, sticky=N+E+W+S)
        time_lbl14.grid(row = 15, column = 0, sticky=N+E+W+S)
        time_lbl15.grid(row = 16, column = 0, sticky=N+E+W+S)
        time_lbl16.grid(row = 17, column = 0, sticky=N+E+W+S)
        time_lbl17.grid(row = 18, column = 0, sticky=N+E+W+S)
        time_lbl18.grid(row = 19, column = 0, sticky=N+E+W+S)
        time_lbl19.grid(row = 20, column = 0, sticky=N+E+W+S)
        time_lbl20.grid(row = 21, column = 0, sticky=N+E+W+S)
        time_lbl21.grid(row = 22, column = 0, sticky=N+E+W+S)
        time_lbl22.grid(row = 23, column = 0, sticky=N+E+W+S)
        time_lbl23.grid(row = 24, column = 0, sticky=N+E+W+S)
        time_lbl24.grid(row = 25, column = 0, sticky=N+E+W+S)



        info_lbl = Label(plan_frame, text = "INFO", width = 59, height = 1).grid(row = 0, column = 1, sticky=N+E+W+S)

        info_Ent0 = Entry(plan_frame, width = 59)
        info_Ent1 = Entry(plan_frame, width = 59)
        info_Ent2 = Entry(plan_frame, width = 59)
        info_Ent3 = Entry(plan_frame, width = 59)
        info_Ent4 = Entry(plan_frame, width = 59)
        info_Ent5 = Entry(plan_frame, width = 59)
        info_Ent6 = Entry(plan_frame, width = 59)
        info_Ent7 = Entry(plan_frame, width = 59)
        info_Ent8 = Entry(plan_frame, width = 59)
        info_Ent9 = Entry(plan_frame, width = 59)
        info_Ent10 = Entry(plan_frame, width = 59)
        info_Ent11 = Entry(plan_frame, width = 59)
        info_Ent12 = Entry(plan_frame, width = 59)
        info_Ent13 = Entry(plan_frame, width = 59)
        info_Ent14 = Entry(plan_frame, width = 59)
        info_Ent15 = Entry(plan_frame, width = 59)
        info_Ent16 = Entry(plan_frame, width = 59)
        info_Ent17 = Entry(plan_frame, width = 59)
        info_Ent18 = Entry(plan_frame, width = 59)
        info_Ent19 = Entry(plan_frame, width = 59)
        info_Ent20 = Entry(plan_frame, width = 59)
        info_Ent21 = Entry(plan_frame, width = 59)
        info_Ent22 = Entry(plan_frame, width = 59)
        info_Ent23 = Entry(plan_frame, width = 59)
        info_Ent24 = Entry(plan_frame, width = 59)

        info_Ent0.grid(row = 1, column = 1, sticky=N+E+W+S)
        info_Ent1.grid(row = 2, column = 1, sticky=N+E+W+S)
        info_Ent2.grid(row = 3, column = 1, sticky=N+E+W+S)
        info_Ent3.grid(row = 4, column = 1, sticky=N+E+W+S)
        info_Ent4.grid(row = 5, column = 1, sticky=N+E+W+S)
        info_Ent5.grid(row = 6, column = 1, sticky=N+E+W+S)
        info_Ent6.grid(row = 7, column = 1, sticky=N+E+W+S)
        info_Ent7.grid(row = 8, column = 1, sticky=N+E+W+S)
        info_Ent8.grid(row = 9, column = 1, sticky=N+E+W+S)
        info_Ent9.grid(row = 10, column = 1, sticky=N+E+W+S)
        info_Ent10.grid(row =11, column = 1, sticky=N+E+W+S)
        info_Ent11.grid(row = 12, column = 1, sticky=N+E+W+S)
        info_Ent12.grid(row = 13, column = 1, sticky=N+E+W+S)
        info_Ent13.grid(row = 14, column = 1, sticky=N+E+W+S)
        info_Ent14.grid(row = 15, column = 1, sticky=N+E+W+S)
        info_Ent15.grid(row = 16, column = 1, sticky=N+E+W+S)
        info_Ent16.grid(row = 17, column = 1, sticky=N+E+W+S)
        info_Ent17.grid(row = 18, column = 1, sticky=N+E+W+S)
        info_Ent18.grid(row = 19, column = 1, sticky=N+E+W+S)
        info_Ent19.grid(row = 20, column = 1, sticky=N+E+W+S)
        info_Ent20.grid(row = 21, column = 1, sticky=N+E+W+S)
        info_Ent21.grid(row = 22, column = 1, sticky=N+E+W+S)
        info_Ent22.grid(row = 23, column = 1, sticky=N+E+W+S)
        info_Ent23.grid(row = 24, column = 1, sticky=N+E+W+S)
        info_Ent24.grid(row = 25, column = 1, sticky=N+E+W+S)

        cur_date_file = "./1_plans_folder/" + "Plan_folder_{0}_{1}/" .format(State, temp_date_st_en) + date_lst[cur_location_in_lst][:4] + "_" + date_lst[cur_location_in_lst][5:7] + "_" + date_lst[cur_location_in_lst][8:]

        f = open("{0}.txt" .format(cur_date_file), "r")

        fixed_lines = []

        for i in range(26):
            line = f.readline().strip()
            fixed_lines.append(line)


        time_Ent0.delete(0, END)
        time_Ent0.insert(0, fixed_lines[0])
        info_Ent0.delete(0, END)            
        info_Ent0.insert(0, fixed_lines[1])
        info_Ent1.delete(0, END)            
        info_Ent1.insert(0, fixed_lines[2])
        info_Ent2.delete(0, END)            
        info_Ent2.insert(0, fixed_lines[3])
        info_Ent3.delete(0, END)            
        info_Ent3.insert(0, fixed_lines[4])
        info_Ent4.delete(0, END)          
        info_Ent4.insert(0, fixed_lines[5])
        info_Ent5.delete(0, END)            
        info_Ent5.insert(0, fixed_lines[6])
        info_Ent6.delete(0, END)            
        info_Ent6.insert(0, fixed_lines[7])
        info_Ent7.delete(0, END)            
        info_Ent7.insert(0, fixed_lines[8])
        info_Ent8.delete(0, END)            
        info_Ent8.insert(0, fixed_lines[9])
        info_Ent9.delete(0, END)            
        info_Ent9.insert(0, fixed_lines[10])
        info_Ent10.delete(0, END)            
        info_Ent10.insert(0, fixed_lines[11])
        info_Ent11.delete(0, END)            
        info_Ent11.insert(0, fixed_lines[12])
        info_Ent12.delete(0, END)            
        info_Ent12.insert(0, fixed_lines[13])
        info_Ent13.delete(0, END)            
        info_Ent13.insert(0, fixed_lines[14])
        info_Ent14.delete(0, END)            
        info_Ent14.insert(0, fixed_lines[15])
        info_Ent15.delete(0, END)            
        info_Ent15.insert(0, fixed_lines[16])
        info_Ent16.delete(0, END)            
        info_Ent16.insert(0, fixed_lines[17])
        info_Ent17.delete(0, END)            
        info_Ent17.insert(0, fixed_lines[18])
        info_Ent18.delete(0, END)            
        info_Ent18.insert(0, fixed_lines[19])
        info_Ent19.delete(0, END)            
        info_Ent19.insert(0, fixed_lines[20])
        info_Ent20.delete(0, END)            
        info_Ent20.insert(0, fixed_lines[21])
        info_Ent21.delete(0, END)            
        info_Ent21.insert(0, fixed_lines[22])
        info_Ent22.delete(0, END)            
        info_Ent22.insert(0, fixed_lines[23])
        info_Ent23.delete(0, END)            
        info_Ent23.insert(0, fixed_lines[24])
        info_Ent24.delete(0, END)            
        info_Ent24.insert(0, fixed_lines[25])

        f.close()


        plan_done_btn = Button(new_plan_win, text = "done", padx = 5, pady = 5, command = plan_done_cmd).place(x = 420, y = 5)

        new_plan_win.config(bg = "slate gray")
        new_plan_win.mainloop()

    open_preplan_btn = Button(view_preplan_win, text = "open", command = open_preplan_cmd, padx = 10, pady = 6)
    open_preplan_btn.place(x = 420, y = 7)

    def delete_preplan_cmd():
        selected = plan_listbox.curselection()
        sselected = plan_listbox.get(selected)


        State = str(sselected[9:-32])
        st_y = str(sselected[-23:-19])
        st_m = str(sselected[-18:-16])
        st_d = str(sselected[-15:-13])
        en_y = str(sselected[-10:-6])
        en_m = str(sselected[-5:-3])
        en_d = str(sselected[-2:])

        path = "./1_plans_folder/"

        shutil.rmtree("{}Plan_folder_{}_{}_{}_{}__{}_{}_{}" .format(path, State, st_y, st_m, st_d, en_y, en_m, en_d))

        plan_listbox.delete(selected)

    preplan_delete_btn = Button(view_preplan_win, text = "delete", padx = 5, pady = 5, command = delete_preplan_cmd)
    preplan_delete_btn.place(x = 427, y = 563)

    listbox_font = tkinter.font.Font(size = 2)

    plan_listbox = Listbox(view_preplan_bg_frame, selectmode = "single", width = 42, height = 24, bd= 2, fg = "black", font = listbox_font)

    folder_path = "./1_plans_folder"

    plan_lst = os.listdir(folder_path)

    for i in range(len(plan_lst)):
        plan_listbox_name = " State : " + plan_lst[i][12:-23] +"  Date : " + plan_lst[i][-22:-18] +"/" + plan_lst[i][-17:-15] + "/" + plan_lst[i][-14:-12] + " - " + plan_lst[i][-10:-6] + "/" + plan_lst[i][-5:-3] + "/" + plan_lst[i][-2:]
        plan_listbox.insert(END, plan_listbox_name)

    plan_listbox.pack()

    plan_listbox.config(font = listbox_font)

    view_preplan_win.config(bg = "slate gray")
    view_preplan_win.mainloop()  

view_preplan_photo = PhotoImage(file = "./imgs/view_preplan_photo.png")
view_preplan_btn = Button(start_win, image = view_preplan_photo, command = view_preplan_cmd)
view_preplan_btn.place(x = 360, y = 560)

start_win.config(bg = "slate gray")
dclock()
start_win.mainloop()
