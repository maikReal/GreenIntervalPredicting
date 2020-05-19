from tkinter import *
from tkinter import filedialog
import time
from animated_gif import Loading
import subprocess
import os
from PIL import ImageTk, Image


from green_interval_calculation import calculate_optimal_time


class LoadingScreen(Frame):
    def __init__(self, root):

        Frame.__init__(self)

        self._frame = LoadingScreen
        self.root = root

        root.title("Tkinter Application")
        root.resizable(width=False, height=False)

        root.geometry('1260x800')
    
        anim = Loading(self.root, 'Data/loader.gif')
        anim.pack()

        def switch_frame(frame_class):
            new_frame = frame_class(self)

            anim.pack_forget()
            setup_button.pack_forget()
            switch_button.pack_forget()
            try:
                label.pack_forget()

            except Exception:
                pass

            new_frame.pack()

        label = None
        def setup_deps():

            label_start = Label(self.root, text='Dependencies are installing')
            label_start.pack()
            os.system('./Scripts/setup.sh')
            label_start.pack_forget()

            global label
            label = Label(self.root, text='Dependencies was successfully installed')
            label.pack()

        def switch_to_main_screen():
            print('switched to main screen')
            anim.after_cancel(anim.cancel)
            switch_frame(Root)

        setup_button = Button(self.root, text='Setup Dependencies', command=setup_deps)
        setup_button.pack(pady=10)
        switch_button = Button(self.root, text='Test Application', command=switch_to_main_screen)
        switch_button.pack(pady=10)


class Root(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.filename = None
        self.master = master
        
        self.master.root.title("Tkinter Application")
        self.master.root.resizable(width=False, height=False)

        self.master.root.geometry('1260x800')

        self.article_name_label = Label(master.root, text='Optimap Green Interval Predicting')
        # self.article_name_label.place(x=480, y=0, anchor=NW)
        self.article_name_label.pack(pady=10)
        self.article_name_label["font"] = 'Montserrat 20 bold'

        self.app_desc = Label(master.root, text='The main aim of this application is to demonstrate how does algorithm of predicting optimal green interval for pedestrians work.\n Below, you can upload your short video or photo and get the following: video/photo with object detection predictions and optimal green interval (in seconds)')
        # self.app_desc.place(x=600, y=60, anchor=CENTER)
        self.app_desc.pack(pady=10)
        self.app_desc["font"] = 'Montserrat 14'

        self.upload_button_desc = Label(master.root, text='Upload your short video or photo below')
        # self.upload_button_desc.place(x=650, y=120, anchor=CENTER)
        self.upload_button_desc.pack(pady=10)
        self.upload_button_desc["font"] = 'Montserrat 14'

        self.button = Button(master.root, text='Browse A File', font='Montserrat 16', command=self.process_file)
        # self.button.place(x=510, y=150)
        self.button.pack(pady=10)
        self.button["font"] = 'Montserrat 14'

        self.label_1 = Label(master.root, text='Enter necessary information')
        self.button.pack(pady=10)
        self.button["font"] = 'Montserrat 14'

        self.road_width = Entry(master.root)
        self.road_width.insert(0, 'Road Width')
        self.road_width.configure(state=DISABLED)
        self.road_width.pack(pady=10)
        self.road_width["font"] = 'Montserrat 14'

        def on_click(event):
            self.road_width.configure(state=NORMAL)
            self.road_width.delete(0, END)

            # make the callback only work once
            self.road_width.unbind('<Button-1>', self.on_click_id)

        self.on_click_id = self.road_width.bind('<Button-1>', on_click)

        self.button_predict = Button(master.root, text='PredictInterval', command=self.calculate_interval)
        self.button_predict.pack(pady=10)
        self.button_predict["font"] = 'Montserrat 14'

        self.quit_buttons = Button(master.root, text='Quit', command=self.quit)
        self.quit_buttons.pack(pady=10)
        self.quit_buttons["font"] = 'Montserrat 14'

        self.panel = None
        self.predicted_bboxes = None

    def  process_file(self):
        self.filename = filedialog.askopenfilename()
        self.button['text'] = self.filename.split('/')[-1]

    def calculate_interval(self):

        print(self.filename)
        print(self.road_width.get())

        optimal_time = calculate_optimal_time(self.filename, self.road_width.get())
        
        try:
            self.predicted_bboxes.pack_forget()
            self.panel.pack_forget()
        except Exception:
            pass

        self.time_panel = Label(self.master.root, text=f'Optimal green interval for pedestrian on this photo is {round(optimal_time[0])} sec')
        self.time_panel.pack()
        self.time_panel["font"] = 'Montserrat 14'

        self.predicted_bboxes = Image.open("TmpDetectionResults/img_pedestrian.jpg")
        self.predicted_bboxes = self.predicted_bboxes.resize((850, 550), Image.ANTIALIAS)
        self.predicted_bboxes = ImageTk.PhotoImage(self.predicted_bboxes)

        self.panel = Label(self.master.root, image = self.predicted_bboxes)
        self.panel.image = self.predicted_bboxes
        self.panel.pack()


    def quit(self):
        self.master.root.destroy()




if __name__ == '__main__':

    root = Tk()

    LoadingScreen(root)
    
    root.mainloop()