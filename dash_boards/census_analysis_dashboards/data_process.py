import matplotlib.pyplot as plt
from collections import Counter


class Calculate:  
    def __init__(self): 
        with open("adult.data") as file:
            lines = file.readlines()
        self.data = [line.strip().split(", ") for line in lines]

    def genders_total(self):
        """Returns two lists: males and female entries in the dataset."""
        males = []
        females = []     
        for person in self.data:
            if len(person) < 15:
                continue
            try:
                if person[9] == "Male": # Select maried males
                    males.append(person)
                elif person[9] == "Female": # Select maried females
                    females.append(person)                    
            except:
                pass
        return males, females         
        
    def genders_status(self):
        """Returns four lists: single males, married males, single females, 
            and married females."""
        singles_males = []
        mar_males = []   
        singles_females = []
        mar_females = []        
        for person in self.data:   
            if len(person) < 15 :
                continue  
            try:  
                if person[9] == "Male":
                    if person[5] == "Married-civ-spouse":
                        mar_males.append(person)
                    else:
                        singles_males.append(person)
                elif person[9] == "Female":
                    if person[5] == "Married-civ-spouse":
                        mar_females.append(person)
                    else:
                        singles_females.append(person)
            except:
                pass
        return singles_males, mar_males, singles_females, mar_females
                
    def age_martial_status(self):
        """Returns four lists: married females and males, each split by age 
            (above or under 30)."""
        mar_male_abv_30 = []
        mar_male_und_30 = []
        mar_fem_abv_30 = []
        mar_fem_und_30 = []
        for person in self.data:
            if len(person) < 15:
                continue
            try:
                if person[9] == "Male":
                    if int(person[0]) >= 30 and person[5] == "Married-civ-spouse":                           
                        mar_male_abv_30.append(person)
                    elif int(person[0]) < 30 and person[5] == "Married-civ-spouse":
                        mar_male_und_30.append(person)   
                                                  
                elif person[9] == "Female":
                    if int(person[0]) >= 30 and person[5] == "Married-civ-spouse":
                        mar_fem_abv_30.append(person)
                    elif int(person[0]) < 30 and person[5] == "Married-civ-spouse":
                        mar_fem_und_30.append(person)                                            
            except: 
                pass  
        return mar_fem_abv_30, mar_fem_und_30, mar_male_abv_30, mar_male_und_30              
    
    def gender_income(self):
        """Returns four lists: males and females with income conditions, split 
            by age (above or under 30)."""
        male_inc_und_30 = []
        male_inc_abv_30 = []
        female_inc_und_30 = []
        female_inc_abv_30 = []
        for person in self.data:
            if len(person) < 15:
                continue           
            try:
                if person[9] == "Male":
                    if int(person[0]) <= 30 and person[14] == "<=50K":
                        male_inc_und_30.append(person)
                    elif int(person[0]) > 30 and person[14] == ">50K":
                        male_inc_abv_30.append(person)
                if person[9] == "Female":
                    if int(person[0]) <= 30 and person[14] == "<=50K":
                        female_inc_und_30.append(person)
                    elif int(person[0]) > 30 and person[14] == ">50K":
                        female_inc_abv_30.append(person)
            except:
                pass       
        return male_inc_und_30, male_inc_abv_30, female_inc_und_30, female_inc_abv_30   
    
    def get_all_degrees(self):
        """Get a set with all available degrees from that document for later process."""
        degrees = set()
        for person in self.data:
            if len(person) < 15:
                continue
            try:
                degrees.add(person[3])  # index 3 = education
            except:
                pass
        return sorted(degrees)
    
    def race_genders(self):
        """Calculate the number of black and white persons."""
        white_males = []
        white_females = []
        black_males = []
        black_females = []    
        for person in self.data:
            if len(person) < 15:
                continue
            try:
                if person[8] == "White":
                    if person[9] == "Male":
                        white_males.append(person)
                    elif person[9] == "Female":
                        white_females.append(person)
                if person[8] == "Black":
                    if person[9] == "Male":
                        black_males.append(person)
                    elif person[9] == "Female":
                        black_females.append(person)
            except:
                pass
        return white_males, white_females, black_males, black_females    
    
    def degrees(self):
        """Returns lists of people grouped by highest degrees (Doctorate, Prof-school, etc.)."""
        doctorate = []
        prof_school = []
        masters = []
        bachelors = []
        some_college = []
        hs_grad = []
        others = []
        for person in self.data:
            if len(person) < 15:
                continue
            try:
                if person[3] == "Doctorate":
                    doctorate.append(person)
                elif person[3] == "Prof-school":
                    prof_school.append(person)
                elif person[3] == "Masters":
                    masters.append(person)
                elif person[3] == "Bachelors":
                    bachelors.append(person)
                elif person[3] == "Some-college":
                    some_college.append(person)
                elif person[3] == "HS-grad":
                    hs_grad.append(person)
                else:
                    others.append(person)
            except:
                pass
        return doctorate, prof_school, masters, bachelors, some_college, hs_grad, others
                                                             
    def hours_worked(self):
        """Returns six lists: total hours worked by males and females, 
            and full person records for males/females split by age 
            (above or under 40)."""
        worked_hours_males = []
        worked_hours_males_abv_40 = []
        worked_hours_males_undr_40 = []
        worked_hours_females = []
        worked_hours_females_abv_40 = []
        worked_hours_females_undr_40 = []
        for person in self.data:
            if len(person) < 15:
                continue
            try:
                if person[9] == "Male":
                    worked_hours_males.append(int(person[12]))
                    if int(person[0]) >= 40:
                        worked_hours_males_abv_40.append(person)
                    elif int(person[0]) < 40:
                        worked_hours_males_undr_40.append(person)
                elif person[9] == "Female":
                    worked_hours_females.append(int(person[12]))                   
                    if int(person[0]) >= 40:
                        worked_hours_females_abv_40.append(person)
                    elif int(person[0]) < 40:
                        worked_hours_females_undr_40.append(person)
            except:
                pass
        return (worked_hours_males, worked_hours_males_abv_40, worked_hours_males_undr_40, 
        worked_hours_females, worked_hours_females_abv_40, worked_hours_females_undr_40)
        

             
calculate = Calculate() 
males, females  = calculate.genders_total() # 
singles_males, mar_males, singles_females, mar_females = calculate.genders_status()
mar_fem_abv_30, mar_fem_und_30, mar_male_abv_30, mar_male_und_30 = calculate.age_martial_status()
degrees = calculate.get_all_degrees()
print(degrees)
white_males, white_females, black_males, black_females = calculate.race_genders()
doctorate, prof_school, masters, bachelors, some_college, hs_grad, others = calculate.degrees()

(worked_hours_males, worked_hours_males_abv_40, worked_hours_males_undr_40,
worked_hours_females, worked_hours_females_abv_40, worked_hours_females_undr_40) = calculate.hours_worked()


# Calculating percentages of maried man, women, under, above ages
percentage_total_mar_man = (len(mar_males) / len(males)) * 100
percentage_m_man_over_30 = (len(mar_male_abv_30) / len(mar_males)) * 100
percentage_m_man_under_30 = (len(mar_male_und_30) / len(mar_males)) * 100

percentage_total_m_women = (len(mar_females) / len(females)) * 100
percentage_m_women_over_30 = (len(mar_fem_abv_30) / len(mar_females)) * 100
percentage_m_women_under_30 = (len(mar_fem_und_30) / len(mar_females)) * 100

# Calculating worked hour avg by males and females
avg_work_hours_males = (sum(worked_hours_males) / len(males)) 
avg_work_hours_females = (sum(worked_hours_females) / len(females))

print(f"Total man: {len(males)}")
print(f"Singles man: {len(singles_males)}")
print(f"Maried man: {len(mar_males)}")
print(f"Percentage of total maried man: {percentage_total_mar_man:.2f}")
print(f"Maried man under 30: {len(mar_male_und_30)}")
print(f"Maried man above 30: {len(mar_male_abv_30)}")
print(f"Percentage of maried man over 30: {percentage_m_man_over_30:.2f}")
print(f"Percentage of maried man under 30: {percentage_m_man_under_30:.2f}")

print("------------------------------------")

print(f"Total women: {len(females)}")
print(f"Singles women: {len(singles_females)}")
print(f"Maried women: {len(mar_females)}")
print(f"Percentage of total maried women: {percentage_total_m_women:.2f}")
print(f"Maried women above 30: {len(mar_fem_abv_30)}")
print(f"Maried women under 30: {len(mar_fem_und_30)}")
print(f"Percentage of maried woman under 30: {percentage_m_women_over_30:.2f}")
print(f"Percentage of maried woman under 30: {percentage_m_women_under_30:.2f}")

print("------------------------------------")

print(f"Number of black people: {len(black_males + black_females)}")
print(f"Number of white poeple: {len(white_males + white_females)}")
print(f"Number of black males: {len(black_males)}")
print(f"Number of black females = {len(black_females)}")
print(f"Number of white males: {len(white_males)}")
print(f"Number of white females = {len(white_females)}")

print("------------------------------------")

print(f"Doctorates: {len(doctorate)}")
print(f"Prof school: {len(prof_school)}")
print(f"Masters: {len(masters)}")
print(f"Bachelors: {len(bachelors)}")
print(f"Som College: {len(some_college)}")
print(f"HS Grad: {len(hs_grad)}")
print(f"Others: {len(others)}")

print("------------------------------------")

print(f"Avereage worked hour males: {avg_work_hours_males:.2f}")
print(f"Avereage worked hour females: {avg_work_hours_females:.2f}")

