def friends():
    
    money_spent = {"Abhiraj" : 990, "Leon" : 290, "Vigyan" : 1100}
    money_due = {"Abhiraj" : "" ,"Leon" : "" , "Vigyan" : ""}
    l1 = []
    x = (money_spent["Abhiraj"] + money_spent["Leon"] + money_spent["Vigyan"])/3
    l1.append(money_spent["Abhiraj"] - x)
    l1.append(money_spent["Leon"] - x)
    l1.append(money_spent["Vigyan"] - x)
    money_due["Abhiraj"] = l1[0]
    money_due["Leon"] = l1[1]
    money_due["Vigyan"] = l1[2]
    print "Money Spent"
    print money_spent
    print
    print "Money that each will get is :- "
    print money_due

friends()
