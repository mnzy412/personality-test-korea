from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import *



##필요한 함수 선언

def func_exit(): #윈도우 창을 종료시키는 함수
    window.quit()
    window.destroy()

def caution(): #선택지 고르지 않고 다음버튼 누르면 나오는 메세지 박스
        messagebox.showinfo("알림", "선택지를 골라주세요")

def check(): #선택지를 모두 골랐는지 확인하는 함수
    if (var1.get() != FALSE and var2.get() != FALSE and var3.get() != FALSE and var4.get() != FALSE):
        openResult()
    else:
        caution()
   
def openResult(): #마지막 질문 답변 후 다음버튼 누르면새로운 창을 띄워 결과창 보여줄 때
    def func_foodResult(): #1번 질문지에서 고른 것에 따라 다른 결과 이미지를 띄우기 위함
        if var1.get() == 1:
            photo = PhotoImage(file = "C://Temp//result//food01.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var1.get() == 2:
            photo = PhotoImage(file = "C://Temp//result//food02.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var1.get() == 3:
            photo = PhotoImage(file = "C://Temp//result//food03.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var1.get() == 4:
            photo = PhotoImage(file = "C://Temp//result//food04.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

    def func_tourResult(): #2번 질문지에서 고른 것에 따라 다른 결과 이미지를 띄우기 위함
        if var2.get() == 1:
            photo = PhotoImage(file = "C://Temp//result//tour01.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var2.get() == 2:
            photo = PhotoImage(file = "C://Temp//result//tour02.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var2.get() == 3:
            photo = PhotoImage(file = "C://Temp//result//tour03.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var2.get() == 4:
            photo = PhotoImage(file = "C://Temp//result//tour04.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

    def func_clothResult(): #3번 질문지에서 고른 것에 따라 다른 결과 이미지를 띄우기 위함
        if var3.get() == 1:
            photo = PhotoImage(file = "C://Temp//result//cloth01.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var3.get() == 2:
            photo = PhotoImage(file = "C://Temp//result//cloth02.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var3.get() == 3:
            photo = PhotoImage(file = "C://Temp//result//cloth03.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var3.get() == 4:
            photo = PhotoImage(file = "C://Temp//result//cloth04.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

    def func_playResult(): #4번 질문지에서 고른 것에 따라 다른 결과 이미지를 띄우기 위함
        if var4.get() == 1:
            photo = PhotoImage(file = "C://Temp//result//play01.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var4.get() == 2:
            photo = PhotoImage(file = "C://Temp//result//play02.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo

        if var4.get() == 3:
           photo = PhotoImage(file = "C://Temp//result//play03.gif")
           pLabel.configure(image = photo)
           pLabel.image = photo
    
        if var4.get() == 4:
            photo = PhotoImage(file = "C://Temp//result//play04.gif")
            pLabel.configure(image = photo)
            pLabel.image = photo
        
    top = Toplevel(window)
    label = Label(top)
    top.geometry("700x700")
    top.resizable(width = FALSE, height = FALSE)
    Label.pack

    photo = PhotoImage()
    pLabel = Label(top, image = photo)
    pLabel.pack(expand = 1, anchor = CENTER)

    photo = PhotoImage(file = "C://Temp//result//main_result.gif")
    pLabel.configure(image = photo)
    pLabel.image = photo

    #메뉴창
    mainMenu = Menu(top)
    top.config(menu = mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "결과", menu = fileMenu)
    fileMenu.add_command(label = "한식", command = func_foodResult)
    fileMenu.add_separator()
    fileMenu.add_command(label = "관광지", command = func_tourResult)
    fileMenu.add_separator()
    fileMenu.add_command(label = "전통 옷", command = func_clothResult)
    fileMenu.add_separator()
    fileMenu.add_command(label = "전통놀이", command = func_playResult)
    fileMenu.add_separator()
    fileMenu.add_command(label = "프로그램 종료", command = func_exit)
  

#메인함수---------------------------------
    
window = Tk() #베이스 윈도우 창


window.title('나에게 맞는 한국 전통 문화 테스트')  #창 이름
window.geometry('800x600')   #크기 정해놓기(사진 크기에 맞게 바꾸기)
window.resizable(width = FALSE, height = FALSE) #크기 못바꾸게 함(팀원들과 상의하기)

var1 = IntVar()

notebook = ttk.Notebook(window, width = 800, height = 600) #탭
notebook.pack()


frame1 = Frame(window)
notebook.add(frame1, text ="첫번째 질문")

question1 = Label(frame1, text = '1. 배고픈 당신! 배달 앱으로 주문해서 밥을 먹으려고 하는데... 당신의 선택은?', font =("맑은 고딕", 15)) ## ex ) 여행갈 때 계획을 미리 하고 가나요?
question1.pack(pady = 50)

c1_1 = Radiobutton(frame1, text='1. 음식 종류부터 혜택까지 꼼꼼하게 따져보고 주문한다.', font =("맑은 고딕", 11), variable=var1, value=1)
c1_1.pack(anchor = W)

c1_2 = Radiobutton(frame1, text='2. 과감하게 먹어보지 않은 새로운 메뉴를 주문한다.',font =("맑은 고딕", 11), variable=var1, value=2)
c1_2.pack(anchor = W)

c1_3 = Radiobutton(frame1, text='3. 이미 하루 전에 주문 계획이 다 세워있는 편! 고민 없이 바로 주문한다.',font =("맑은 고딕", 11), variable=var1, value=3)
c1_3.pack(anchor = W)

c1_4 = Radiobutton(frame1, text='4. 일단 이것저것 많이 주문한다. 그러고선 정작 음식이 오면 다 못 먹는 편..',font =("맑은 고딕", 11), variable=var1, value=4)
c1_4.pack(anchor = W)

var2 = IntVar()

frame2 = Frame(window)
notebook.add(frame2, text = "두번째 질문")
question2 = Label(frame2, text = '2. 곧 있을 여름방학을 맞아 여름휴가를 준비하려는 당신... 당신의 선택은?', font =("맑은 고딕", 15)) ## ex ) 여행갈 때 계획을 미리 하고 가나요?
question2.pack(pady = 50)

c21 = Radiobutton(frame2, text='1. 이상적인 휴가를 머릿속으로 떠올리며 행복한 상상에 빠진다.', font =("맑은 고딕", 11), variable=var2, value=1)
c21.pack(anchor = W)

c22 = Radiobutton(frame2, text='2. 배보다 배꼽이 먼저! 일단 여행 갈 때 입을 옷부터 산다.',font =("맑은 고딕", 11), variable=var2, value=2)
c22.pack(anchor = W)

c23 = Radiobutton(frame2, text='3. 여름휴가를 같이 갈 사람을 모집하고 같이 가는 사람들에게 뭐하고 싶은지 물어본다.',font =("맑은 고딕", 11), variable=var2, value=3)
c23.pack(anchor = W)

c24 = Radiobutton(frame2, text='4. 샅샅이 조사해서 갈 곳을 정하고 전체 구성을 기획한다.',font =("맑은 고딕", 11), variable=var2, value=4)
c24.pack(anchor = W)

var3 = IntVar()

frame3 = Frame(window)
notebook.add(frame3, text = "세번째 질문")
question3 = Label(frame3, text = '3.친구가 약속에 늦었을 때... 당신의 반응은?', font =("맑은 고딕", 15)) ## ex ) 여행갈 때 계획을 미리 하고 가나요?
question3.pack(pady = 50)

c31 = Radiobutton(frame3, text='1. 앗! 나도 늦었다!', font =("맑은 고딕", 11), variable=var3, value=1)
c31.pack(anchor = W)

c32 = Radiobutton(frame3, text='2. 오면 된거지! 신경쓰지 않는다.',font =("맑은 고딕", 11), variable=var3, value=2)
c32.pack(anchor = W)

c33 = Radiobutton(frame3, text='3. 눈에는 눈! 이에는 이! 다음에 나도 똑같이 늦는다.',font =("맑은 고딕", 11), variable=var3, value=3)
c33.pack(anchor = W)

c34 = Radiobutton(frame3, text='4. 늦으면 끝이지... 그냥 집에 간다.',font =("맑은 고딕", 11), variable=var3, value=4)
c34.pack(anchor = W)

var4 = IntVar()

frame4 = Frame(window)
notebook.add(frame4, text = "네번째 질문")
question4 = Label(frame4, text = '4. 열심히 공부한 기말 시험을 망쳤을 때... 당신의 반응은?', font =("맑은 고딕", 15)) ## ex ) 여행갈 때 계획을 미리 하고 가나요?
question4.pack(pady = 50)

c41 = Radiobutton(frame4, text='1. 너무 슬퍼서 엉엉 운다.', font =("맑은 고딕", 11), variable=var4, value=1)
c41.pack(anchor = W)

c42 = Radiobutton(frame4, text='2. 끝난 건 끝난 것! 그냥 논다.',font =("맑은 고딕", 11), variable=var4, value=2)
c42.pack(anchor = W)

c43 = Radiobutton(frame4, text='3. 아직 다음 시험이 있다! 열심히 공부한다.',font =("맑은 고딕", 11), variable=var4, value=3)
c43.pack(anchor = W)

c44 = Radiobutton(frame4, text='4. 교수님... 성적 정정 메일을 구구절절 보내본다.',font =("맑은 고딕", 11), variable=var4, value=4)
c44.pack(anchor = W)

btnNext = Button(frame4, text = " 결과 확인하기", command = check ) #버튼 설정
btnNext.place( x =680, y = 320) #해당 좌표에 버튼 배치

window.mainloop()
