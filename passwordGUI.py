import generator 



from tkinter import *

class PasswordGui():
    def __init__(self,master):
        #configuration
        master.configure(bg='ivory2')
        master.title('Password Generator')
        master.option_add('*Font','Georgia 12') #font for all widgets
        master.option_add('*Background','ivory2') #background of all
        master.option_add('*Label.Font','helvetica 14') #font for all
        master.geometry('800x500+100+100') #w,h,x,y (top left corner)
        #
        #frame1 - header area
        #
        frame1=Frame(master, bg='ivory2')
        frame1.pack(fill = 'both', expand = True)   #fills window
        #
        #frame2 - user input area
        #
        frame2= Frame(master)
        frame2.pack(fill='both', expand=True)
        #
        #frame 2a (subframe for frame 2)
        #
        frame2a= Frame(frame2, relief =GROOVE, borderwidth= 1,)
        frame2a.pack(side= LEFT, fill= Y) #fill Y makes frames same height
        #
        label_2a_heading= Label(frame2a)
        label_2a_heading.config(borderwidth=0, text='Password must contain:')
        label_2a_heading.pack(padx=10, pady=10)
        #
        self.caps_var=BooleanVar(master)
        cb_1=Checkbutton(frame2a, text='Capital Letter', variable=self.caps_var)
        cb_1.pack(anchor=W, padx=10, pady=10)
        #
        self.nums_var=BooleanVar(master)
        cb_2=Checkbutton(frame2a, text = 'Number', variable=self.nums_var)
        cb_2.pack(anchor=W, padx=10, pady=10)
        #
        self.chars_var = BooleanVar(master)
        cb_3=Checkbutton(frame2a, text= 'Special Character',variable= self.chars_var)
        cb_3.pack(anchor=W, padx=10, pady=10)
        #
        #frame 2b (number of words)
        #
        frame2b=Frame(frame2, relief=GROOVE, borderwidth=1,)
        frame2b.pack(side=LEFT, fill=Y)
        #
        label_2b_heading= Label(frame2b)
        label_2b_heading.config(borderwidth=0, text='Number of Words')
        label_2b_heading.pack(padx=10, pady=10)
        #
        self.radio_choice=IntVar(master) #variable to store radio button choice
        self.radio_choice.set(3) #sets to default value
        radio_1= Radiobutton(frame2b, text='Three', variable = self.radio_choice, value='3')
        radio_2 = Radiobutton(frame2b, text='Four', variable = self.radio_choice, value='4')
        radio_3 = Radiobutton(frame2b, text='Five', variable = self.radio_choice, value='5')
        radio_1.pack(anchor=W, padx=10, pady=10)
        radio_2.pack(anchor=W, padx=10, pady=10)
        radio_3.pack(anchor=W, padx=10, pady=10)
        #
        #frame 2c (password length)
        #
        frame2c = Frame(frame2, relief=GROOVE, borderwidth=1,)
        frame2c.pack(side=LEFT, fill= Y)
        #
        label_2c_heading = Label(frame2c)
        label_2c_heading.config(borderwidth=0, text='Length')
        label_2c_heading.pack(anchor=W, padx=10, pady=10, side=TOP)
        #
        self.length_spin_choice=IntVar(master)
        self.length_spin= Spinbox(frame2c, width=6, from_=8, to =20)
        self.length_spin.pack(anchor=W, padx=10, pady=10)
        #
        btn_generate= Button(frame2c)
        btn_generate.config(relief=RAISED, borderwidth= 5, text= 'Generate', command= self.generate_password)
        btn_generate.pack(padx=10, pady=10, side= BOTTOM)
        #
        icon = PhotoImage(file = 'pword2.gif')
        lbl_icon = Label(frame1)
        lbl_icon.config(image=icon)
        lbl_icon.image=icon # we need to have this line as well as previous one
        lbl_icon.pack(side=LEFT, padx= 10, pady=10)
        #
        label_heading=Label(frame1)
        label_heading.config(text='Password Generator', font=('helvetica 16 bold'))# override default font
        label_heading.pack(side=LEFT, padx=10,pady=10)
        #
        #frame3-output area
        #
        frame3=Frame(master)
        frame3.pack(fill='both', expand= True)
        #
        label_3a=Label(frame3)
        label_3a.config(borderwidth=0, text='Your password is......')
        label_3a.pack(side=LEFT)
        #
        self.password_var=StringVar(master)
        self.password_var.set('') #default to empty string
        label_password=Label(frame3)
        label_password.config(borderwidth=0, textvariable = self.password_var)
        label_password.pack(side=LEFT)


    def generate_password(self):
        #get values from interface
        min_length=self.length_spin.get()
        num_words=self.radio_choice.get()
        caps=self.caps_var.get()
        nums=self.nums_var.get()
        chars=self.chars_var.get()
        generator.generate_password(min_length, num_words, caps, nums, chars)
        #
        output=generator.generate_password(min_length, num_words, caps, nums, chars)
        self.password_var.set(output)
        
        

















    

def main():
    root=Tk()   #creates a tkinter root window
    app=PasswordGui(root)   #puts GUI onto the root
    root.mainloop()     #runs the event handler
    
if __name__=="__main__":
    main()

