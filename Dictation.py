from tkinter import *
import random
import tkinter.messagebox
import pickle
import os

root = Tk()

# list with foreign words and it's copy
foreign_lang_words = []
foreign_lang_words_copy = []
# list with native words and it's copy
native_lang_words = []
native_lang_words_copy = []
# list with indexes of shown words
ind = []
# other stuff
counter1 = 0
counter2 = 0
y1 = 20
y2 = 20
j = 0
r = 0
w = 0

def newStart(topic):
    global foreign_lang_words, native_lang_words, native_lang_words_copy

    def returnToDefault():
        """Returns to default settings"""
        global foreign_lang_words, foreign_lang_words_copy, native_lang_words, native_lang_words_copy
        global ind, counter1, counter2, y1, y2, j, r, w
        foreign_lang_words = []
        foreign_lang_words_copy = []
        native_lang_words = []
        native_lang_words_copy = []
        ind = []
        counter1 = 0
        counter2 = 0
        y1 = 20
        y2 = 20
        j = 0
        r = 0
        w = 0

    returnToDefault()
    try:
        with open(topic + ".dat", "rb") as f:
            lines = pickle.load(f)
        for line in lines:
            words = line.split(" - ")
            foreign_lang_words.append(words[0])
            native_lang_words.append(words[1])
            native_lang_words_copy.append(words[1])
    except:
        tkinter.messagebox.showerror("Error", "Empty file!!!")

def chooseTopic(choice):

    def StartRightDictation(choice, topic):
        if choice == 1:
            manualDictation()
        elif choice == 2:
            keyboardDictation()
        elif choice == 3:
            gameDictation()
        elif choice == 4:
            deleteTopic(topic)
        elif choice == 5:
            showWords(topic)

    root.title("Choose topic")
    root.geometry("250x200")
    topics_frame = Frame(root)
    topics_frame.pack(fill=BOTH, expand=1)

    try:
        topics_file = open("Topics.dat", "rb")
        topics_list = pickle.load(topics_file)
        topics_file.close()
        if len(topics_list) == 0:
            tkinter.messagebox.showerror("Error", "There is no topics found!")
            topics_frame.destroy()
            mainWindow()
        else:
            for topic in topics_list:
                topicbtn = Button(topics_frame, text=topic,
                          command=lambda topic=topic: (topics_frame.destroy(), StartRightDictation(choice, topic)))
                topicbtn.pack(side="top", fill="x")
            backbtn = Button(topics_frame, text="Back", command=lambda: (topics_frame.destroy(), mainWindow()),
                             padx="10", pady="6")
            backbtn.pack(side="bottom", fill="x")
    except FileNotFoundError:
        tkinter.messagebox.showerror("Error", "There is no topics found!")

        topics_frame.destroy()

        mainWindow()

def mainWindow():
    root.title("Alex's dictation")
    root.geometry("300x350")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    choose_label = Label(main_frame, text="Choose what you want to do")
    choose_label.place(x=65, y=20)
    choosebtn1 = Button(main_frame, text="Add new words", command=lambda: (main_frame.destroy(), addWords()),
                        padx="47", pady="6")
    choosebtn1.place(x=55, y=50)

    choosebtn2 = Button(main_frame, text="Delete topic", command=lambda: (main_frame.destroy(), chooseTopic(4)),
                        padx="56", pady="6")
    choosebtn2.place(x=55, y=90)

    choosebtn3 = Button(main_frame, text="Manual dictation", command=lambda: (main_frame.destroy(), chooseTopic(1)),
                        padx="42", pady="6")
    choosebtn3.place(x=55, y=130)

    choosebtn4 = Button(main_frame, text="Keyboard dictation", command=lambda: (main_frame.destroy(), chooseTopic(2)),
                        padx="37", pady="6")
    choosebtn4.place(x=55, y=170)

    choosebtn5 = Button(main_frame, text="Game dictation", command=lambda: (main_frame.destroy(), chooseTopic(3)),
                        padx="46", pady="6")
    choosebtn5.place(x=55, y=210)

    choosebtn6 = Button(main_frame, text="Show words", command=lambda: (main_frame.destroy(), chooseTopic(5)),
                        padx="55", pady="6")
    choosebtn6.place(x=55, y=250)

    choosebtn6 = Button(main_frame, text="Exit", command=lambda: (root.destroy()),
                        padx="77", pady="6")
    choosebtn6.place(x=55, y=290)

def addWords():
    root.title("Adding new words")
    root.geometry("325x200")

    def ui():
        add_words_frame = Frame(root)
        add_words_frame.pack(fill=BOTH, expand=1)
        topic_lbl = Label(add_words_frame, text="Enter the topic:")
        topic_lbl.place(x=110, y=30)
        topic_ent = Entry(add_words_frame)
        topic_ent.place(x=90, y=50)
        word_lbl = Label(add_words_frame, text="Enter foreign word:")
        word_lbl.place(x=10, y=80)
        word_ent = Entry(add_words_frame)
        word_ent.place(x=8, y=100)
        translation_lbl = Label(add_words_frame, text="Enter word`s translation:")
        translation_lbl.place(x=185, y=80)
        translation_ent = Entry(add_words_frame)
        translation_ent.place(x=190, y=100)
        savebtn = Button(add_words_frame, text="Save", command=lambda: saveWord(), padx="10", pady="6")
        savebtn.place(x=105, y=130)
        backbtn = Button(add_words_frame, text="Back", command=lambda: (add_words_frame.destroy(), mainWindow()),
                         padx="10", pady="6")
        backbtn.place(x=160, y=130)

        def saveWord():
            global topics
            extracted_words = []
            if topic_ent.get() == '' or word_ent.get() == '' or translation_ent.get() == '':
                tkinter.messagebox.showerror("Error", "Empty field!!!")
            else:
                try:
                    f = open(topic_ent.get() + ".dat", "rb")
                    try:
                         extracted_words = pickle.load(f)
                         f.close()
                    except:
                        pass
                    f.close()
                except:
                    pass

                f = open(topic_ent.get() + ".dat", "wb")

                try:
                    extracted_words = pickle.load(f)
                    word_with_translation = str(word_ent.get() + " - " + translation_ent.get() + "\n")
                    extracted_words.append(word_with_translation)
                    pickle.dump(extracted_words, f)
                except:
                    extracted_words.append(word_ent.get() + " - " + translation_ent.get() + "\n")
                    pickle.dump(extracted_words, f)
                f.close()
                try:
                    saveTopics()
                except:
                    topics_file = open("Topics.dat", "wb")
                    topics_file.close()
                    saveTopics()
                newWord()

        def saveTopics():
            if topic_ent.get() == '' or word_ent.get() == '' or translation_ent.get() == '':
                tkinter.messagebox.showerror("Error", "Empty field!!!")
            else:
                topics = []
                try:
                    topics_file = open("Topics.dat", "rb")
                    topics = pickle.load(topics_file)
                    topics_file.close()
                except EOFError:
                    pass
                topics_file = open("Topics.dat", "wb")
                if topic_ent.get() not in topics:
                    topics.append(topic_ent.get())
                pickle.dump(topics, topics_file)
                topics_file.close()

        def newWord():
            add_words_frame.destroy()
            ui()
    ui()

def deleteTopic(topic):
    if os.path.isfile(topic + ".dat"):
        answer = tkinter.messagebox.askokcancel("Confirmation", "Are you sure you want to delete this topic?")
        if answer == True:
            topics = []
            topics_file = open("Topics.dat", "rb")
            topics = pickle.load(topics_file)
            topics_file.close()
            topics.remove(topic)
            topics_file = open("Topics.dat", "wb")
            pickle.dump(topics, topics_file)
            topics_file.close()
            os.remove(topic + ".dat")
            tkinter.messagebox.showinfo("Result", "Topic has been deleted successfully!")
        else:
            tkinter.messagebox.showinfo("Result", "The deletion has been cancelled.")
    else:
        tkinter.messagebox.showerror("Error", "File does not exist!")
    mainWindow()

def showWords(topic):
    global foreign_lang_words, native_lang_words, counter1
    root.title("Vocabulary")
    root.geometry("250x350")
    vocab_frame = Frame(root)
    vocab_frame.pack(fill=BOTH, expand=1)

    scrollbar = Scrollbar(vocab_frame)
    words_list = Listbox(vocab_frame, yscrollcommand=scrollbar.set)
    words_list.insert(END, "Topic: " + topic)
    words_list.insert(END, "-" * 50)

    for i in range(len(foreign_lang_words)):
        counter1 += 1
        words_list.insert(END, str(counter1) + ") " + foreign_lang_words[i] + " - " + native_lang_words[i])

    scrollbar.pack(side="right", fill="y")
    scrollbar.config(command=(words_list.yview, words_list.yview()))

    backbtn = Button(vocab_frame, text="Back", command=lambda: (vocab_frame.destroy(), mainWindow()),
                     padx="10", pady="6")
    backbtn.pack(side="bottom", fill="x")

    words_list.pack(expand=1, fill=BOTH)

def manualDictation():
    """Dictation with self-check"""
    global foreign_lang_words, native_lang_words, native_lang_words_copy

    def showNativeWords():
        """Show 1 random word from native language words list"""
        global native_lang_words, native_lang_words_copy, counter1
        try:
            counter1 += 1
            i = random.randint(0, len(native_lang_words)-1)
            ind.append(native_lang_words_copy.index(native_lang_words[i]))
            native_list.insert(END, str(counter1)+") "+native_lang_words[i])
            native_lang_words.remove(native_lang_words[i])

        except ValueError:
            native_list.insert(END, "No words left")

    def showForeignWords():
        """Show translation to foreign language"""
        global ind, foreign_lang_words, counter2, j
        if len(ind) < len(native_lang_words_copy):
            tkinter.messagebox.showerror("Error", "You have not seen all words!" +
                                         "\nWords left in the topic: " + str(len(native_lang_words_copy) - counter1))
        elif counter2 == len(ind):
            tkinter.messagebox.showerror("Error", "You have seen translation of all words!")
        else:
            for index in ind:
                counter2 += 1
                foreign_list.insert(END, str(counter2) + ") " + foreign_lang_words[index])

    root.title("Manual dictation")
    root.geometry("350x350")
    manual_frame = Frame(root)
    manual_frame.pack(fill=BOTH, expand=1)

    scrollbar = Scrollbar(manual_frame)
    native_list = Listbox(manual_frame, yscrollcommand=scrollbar.set)
    foreign_list = Listbox(manual_frame, yscrollcommand=scrollbar.set)
    nextbtn = Button(manual_frame, text="Next word",
                     command=lambda: showNativeWords(), pady="65")
    showtrbtn = Button(manual_frame, text="Show\ntranslation",
                       command=lambda: showForeignWords(), pady="60")
    backbtn = Button(manual_frame, text="Back",
                     command=lambda: (manual_frame.destroy(), mainWindow()), pady="10")

    scrollbar.pack(side="right", fill="y")
    scrollbar.config(command=(native_list.yview, foreign_list.yview()))

    native_list.pack(side="left", fill=BOTH)
    foreign_list.pack(side="left", fill=BOTH)

    nextbtn.pack(side="top", fill=BOTH)
    showtrbtn.pack(side="top", fill=BOTH)
    backbtn.pack(side="top", fill=BOTH)

def keyboardDictation():
    """Dictation with keyboard input"""
    global foreign_lang_words, native_lang_words, native_lang_words_copy, y1, j

    def showNativeWords():
        """Show 1 random word from native language words list"""
        global ind, native_lang_words, native_lang_words_copy, counter1, y1
        try:
            i = random.randint(0, len(native_lang_words) - 1)
            ind.append(native_lang_words_copy.index(native_lang_words[i]))
            counter1 += 1
            my_language_label = Label(keyboard_frame, text=str(counter1) + ") " + native_lang_words[i])
            my_language_label.place(x=10, y=y1)
            native_lang_words.remove(native_lang_words[i])
            jp_ent = Entry(keyboard_frame)
            jp_ent.place(x=150, y=y1)
            checktbtn = Button(keyboard_frame, text="Check", command=lambda: checkWord())
            backbtn = Button(keyboard_frame, text="Back", command=lambda: (keyboard_frame.destroy(), mainWindow()))
            checktbtn.place(x=300, y=y1 - 4)
            backbtn.place(x=350, y=y1 - 4)

        except ValueError:
            fin_label = Label(keyboard_frame, text="No words left")
            fin_label.place(x=10, y=y1)

        def checkWord():
            global ind, y1, j
            try:
                if jp_ent.get() == foreign_lang_words[ind[j]]:
                    cor_label = Label(keyboard_frame, text="Correct")
                    cor_label.place(x=400, y=y1)
                else:
                    incor_label = Label(keyboard_frame, text="Incorrect. Correct word is: "+foreign_lang_words[ind[j]])
                    incor_label.place(x=400, y=y1)
                j += 1
                y1 += 30
                showNativeWords()
            except:
                pass

    root.title("Keyboard dictation")
    root.geometry("650x550")
    keyboard_frame = Frame(root)
    keyboard_frame.pack(fill=BOTH, expand=1)

    showNativeWords()

def gameDictation():
    """Dictation game with 4 variants of answer"""
    global foreign_lang_words, foreign_lang_words_copy, native_lang_words, native_lang_words_copy, y1, j

    root.title("Game dictation")
    root.geometry("315x350")
    game_frame = Frame(root)
    game_frame.pack(fill=BOTH, expand=1)
    if len(native_lang_words) < 4:
        tkinter.messagebox.showerror("Error", "You must have at least 4 words to play!" +
                                     "\nCurrently you have " + str(len(native_lang_words)) + " word(s).")
        game_frame.destroy()
        mainWindow()
    else:

        def showNativeWords():
            global ind, foreign_lang_words, foreign_lang_words_copy, native_lang_words, native_lang_words_copy, j, r, w
            frame = Frame(game_frame)
            frame.pack(fill=BOTH, expand=1)
            wrong_frame = Frame(frame)
            wrong_frame.pack(fill=BOTH, expand=1)
            rate_frame = Frame(wrong_frame)
            rate_frame.pack(fill=BOTH, expand=1)
            task_label = Label(frame, text="Click on the button with right word")
            task_label.place(x=60, y=0)
            try:
                i = random.randint(0, len(native_lang_words) - 1)
                ind.append(native_lang_words_copy.index(native_lang_words[i]))
                my_language_label = Label(frame, text=native_lang_words[i], )
                my_language_label.place(x=155, y=85, anchor='center')
                native_lang_words.remove(native_lang_words[i])
                rate_label = Label(rate_frame, text="Right: "+str(r) + ' ' * 5 + "Wrong: "+str(w))
                rate_label.place(x=105, y=250)
            except ValueError:
                fin_label = Label(frame, text="No words left")
                fin_label.place(x=115, y=60)
                rate_label = Label(rate_frame, text="Right: " + str(r) + ' ' * 5 + "Wrong: " + str(w))
                rate_label.place(x=105, y=250)

            def newPage():
                frame.destroy()
                showNativeWords()

            def showVariants():
                global ind, foreign_lang_words, foreign_lang_words_copy, j
                try:
                    a = random.randint(1, 4)
                    for word in foreign_lang_words:
                        foreign_lang_words_copy.append(word)
                    foreign_lang_words_copy.remove(foreign_lang_words[ind[j]])

                    if a == 1:
                        var_btn1 = Button(game_frame, text=foreign_lang_words[ind[j]],
                                          command=lambda: _right_(), height=2, width=20)
                        var_btn1.place(x=5, y=125)
                        x = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn2 = Button(game_frame, text=foreign_lang_words_copy[x],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn2.place(x=160, y=125)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[x])
                        y = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn3 = Button(game_frame, text=foreign_lang_words_copy[y],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn3.place(x=5, y=170)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[y])
                        z = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn4 = Button(game_frame, text=foreign_lang_words_copy[z],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn4.place(x=160, y=170)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[z])
                    elif a == 2:
                        x = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn1 = Button(game_frame, text=foreign_lang_words_copy[x],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn1.place(x=5, y=125)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[x])
                        var_btn2 = Button(game_frame, text=foreign_lang_words[ind[j]],
                                          command=lambda: _right_(), height=2, width=20)
                        var_btn2.place(x=160, y=125)
                        y = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn3 = Button(game_frame, text=foreign_lang_words_copy[y],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn3.place(x=5, y=170)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[y])
                        z = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn4 = Button(game_frame, text=foreign_lang_words_copy[z],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn4.place(x=160, y=170)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[z])
                    elif a == 3:
                        x = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn1 = Button(game_frame, text=foreign_lang_words_copy[x],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn1.place(x=5, y=125)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[x])
                        y = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn2 = Button(game_frame, text=foreign_lang_words_copy[y],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn2.place(x=160, y=125)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[y])

                        var_btn3 = Button(game_frame, text=foreign_lang_words[ind[j]],
                                          command=lambda: _right_(), height=2, width=20)
                        var_btn3.place(x=5, y=170)
                        z = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn4 = Button(game_frame, text=foreign_lang_words_copy[z],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn4.place(x=160, y=170)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[z])
                    else:
                        x = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn1 = Button(game_frame, text=foreign_lang_words_copy[x],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn1.place(x=5, y=125)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[x])
                        y = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn2 = Button(game_frame, text=foreign_lang_words_copy[y],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn2.place(x=160, y=125)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[y])
                        z = random.randint(0, len(foreign_lang_words_copy) - 1)
                        var_btn3 = Button(game_frame, text=foreign_lang_words_copy[z],
                                          command=lambda: _wrong_(), height=2, width=20)
                        var_btn3.place(x=5, y=170)
                        foreign_lang_words_copy.remove(foreign_lang_words_copy[z])

                        var_btn4 = Button(game_frame, text=foreign_lang_words[ind[j]],
                                          command=lambda: _right_(), height=2, width=20)
                        var_btn4.place(x=160, y=170)

                    j += 1
                except IndexError:
                    pass
            def _right_():
                global r
                r += 1
                wrong_frame.destroy()
                newPage()

            def _wrong_():
                global w
                w += 1
                rate_label = Label(rate_frame, text="Right: " + str(r) + ' ' * 5 + "Wrong: " + str(w))
                rate_label.place(x=105, y=250)
                wrong_label = Label(wrong_frame, text="Wrong...")
                wrong_label.place(x=160, y=40, anchor='center')

            showVariants()
            foreign_lang_words_copy = []
            backbtn = Button(game_frame, text="Back", command=lambda: (game_frame.destroy(), mainWindow()),
                             padx="60", pady="6")
            backbtn.place(x=80, y=275)

        showNativeWords()

mainWindow()

root.resizable(False, False)
root.mainloop()
