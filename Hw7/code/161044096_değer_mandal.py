# Python is a imperative and functional programming language,because
# you use many commands. Python is not a functional programming language,
# but it supports some features specific to functional programming.



#       miyase+asım                              ayşe+mustafa
#             |                                      |
# -----------------------------------    -------------------------------
#   |                |            |         |      |              |
#aydilek+ömer  bülent+kezban    dilek  +  aydın  özal+gülden  bahriye+halil
# |     |           |             |          |       |         |     |
#ebru ferdane     hakan          değer      arif   muhammet  arda  ayşenur




# I used some of my family, because, I could do the homework this way.


dict_deger={"dilek":"mother",
            "aydin":"father",
            "miyase":"grandmother",
            "asim":"grandfather",
            "bulent":"uncle",
            "aydilek":"aunt",
            "arif":"brother"}

dict_miyase={"asim":"husband",
             "bulent":"son",
             "aydilek":"daughter",
             "dilek":"daughter",
             "deger":"granddaughter",
             "arif":"grandson"}

dict_asim={"miyase":"wife",
           "bulent":"son",
           "aydilek":"daughter",
           "dilek":"daughter",
           "deger":"granddaughter",
           "arif":"grandson"}

dict_arif={"dilek":"mother",
           "aydin":"father",
           "miyase":"grandmother",
           "asim":"grandfather",
           "bulent":"uncle",
           "aydilek":"aunt",
           "deger":"sister"}

dict_dilek={"miyase":"mother",
            "asim":"father",
            "aydin":"husband",
            "aydilek":"sister",
            "bulent":"brother",
            "deger":"daughter",
            "arif":"son"}



dict_aydin={"dilek":"wife",
            "deger":"daughter",
            "arif":"son"}

dict_bulent={"miyase":"mother",
             "asim":"father",
             "aydilek":"sister",
             "dilek":"sister",
             "deger":"niece",
             "arif":"nephew"}


dict_aydilek={"miyase":"mother",
             "asim":"father",
             "dilek":"sister",
             "bulent":"brother",
             "deger":"niece",
             "arif":"nephew"}

first=input("enter the first name:")
second=input("enter the second name:")

x=0
while(x<2):
    if first=="miyase":
        print(dict_miyase.get(second,"ops1"))
    if first=="asim":
        print(dict_asim.get(second,"ops2"))
    if first=="deger":
        print(dict_deger.get(second,"ops3"))
    if first=="arif":
        print(dict_arif.get(second,"ops4"))
    if first=="dilek":
        print(dict_dilek.get(second,"ops5"))
    if first=="aydin":
        print(dict_aydin.get(second,"ops6"))
    if first=="aydilek":
        print(dict_aydilek.get(second,"ops7"))
    if first=="bulent":
        print(dict_bulent.get(second,"ops8"))

    a=first
    first=second
    second=a
    del a
    x=x+1

















