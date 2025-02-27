from tkinter import * 
from PIL import Image, ImageTk
import time 

class Loading(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)        


# root = Tk()
# anim = Loading(root, 'Data/loader.gif')

# anim.pack()

# def stop_it():
# 	print('start')
# 	time.sleep(5)
# 	print('end')
# 	anim.after_cancel(anim.cancel)

# Button(root, text='stop', command=stop_it).pack()

# def setup_deps():
# 	print('setup')
# Button(root, text='setup', command=setup_deps).pack()

# root.mainloop()