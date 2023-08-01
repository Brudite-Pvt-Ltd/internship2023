d1 = [
        {"name": "gian", "income": 20000, "expenses": 13000},
        {"name": "degisugi", "income": 12000, "expenses": 4000},
        {"name": "nobita", "income": 47000, "expenses": 2500},
        {"name": "suniyo", "income": 17000, "expenses": 10200}
    ]     
d2={x["name"]:x["income"]-x["expenses"] for x in d1}   
for i,j in d2.items():
    print(i,"",j)