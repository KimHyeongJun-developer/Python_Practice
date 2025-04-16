print("Welcome to the tip calculator!")
total_bill=input("what was the total bill?")
m_bill = int(total_bill)
tip=input("how much tip would you like to give?\n10, 12, or 15?")
m_tip=(int(tip) + 100) / 100
total_people=input("how many people to split the bill?")
m_people=int(total_people)

pay_for_person= round(m_bill * m_tip / m_people,2)

print(f"each person should pay : {pay_for_person}")
