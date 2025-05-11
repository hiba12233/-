def calculator():
        print("العمليات: +  -  *  /")
            try:
                    num1 = float(input("أدخل الرقم الأول: "))
                            op = input("العملية: ")
                                    num2 = float(input("أدخل الرقم الثاني: "))

                                            if op == "+":
                                                        print(num1 + num2)
                                                                elif op == "-":
                                                                            print(num1 - num2)
                                                                                    elif op == "*":
                                                                                                print(num1 * num2)
                                                                                                        elif op == "/":
                                                                                                                    if num2 != 0:
                                                                                                                                    print(num1 / num2)
                                                                                                                                                else:
                                                                                                                                                                print("خطأ: قسمة على صفر")
                                                                                                                                                                        else:
                                                                                                                                                                                    print("عملية غير صالحة")
                                                                                                                                                                                        except:
                                                                                                                                                                                                print("خطأ في الإدخال")

                                                                                                                                                                                                calculator()
                                                                                                                                                                                            
