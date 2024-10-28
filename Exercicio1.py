def removeespacosbranco():
    str = "Sítio do pica-pau amarelo \n 2023"
    res = [char for char in str if not char.isspace()]
    print(res)


removeespacosbranco()