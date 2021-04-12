# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages

def damage_cal(damages):
  for i in range(len(damages)):
    if damages[i]!="Damages not recorded":
      if "M" in damages[i]:
        damages[i]=float(damages[i][:-1])*1000000
      else:
         damages[i]=float(damages[i][:-1])*1000000000
  return damages
# test function by updating damages
damage_cal(damages)

# 2
# Create a Table
def hurricane_dict(names,months,years,max_sustained_winds,areas_affected,deaths,damages):
  hurricane={}
  for i in range(len(names)):
    hurricane[names[i]]={'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]}
  return hurricane

# Create and view the hurricanes dictionary
#print(hurricane_dict(names,months,years,max_sustained_winds,areas_affected,deaths))

# 3
# Organizing by Year
def year_dict():
  year_dictionary={}
  hurricanes=hurricane_dict(names,months,years,max_sustained_winds,areas_affected,deaths,damages)
  for j in hurricanes.values():
    current_year=j["Year"]
    current_cane=[]
    current_cane.append(j)
    if current_year  not in year_dictionary:
      year_dictionary[current_year]=current_cane
    else:
      current_cane.append(j)
      year_dictionary[current_year]=current_cane
  return year_dictionary

# create a new dictionary of hurricanes with year and key
#print(year_dict())



# 4
# Counting Damaged Areas
def count_area():
  area_dictionary={}
  hurricanes=hurricane_dict(names,months,years,max_sustained_winds,areas_affected,deaths,damages)
  for i in hurricanes.values():
    for j in i["Areas Affected"]:
      if j  not in area_dictionary:
        area_dictionary[j]=1
      else:
         area_dictionary[j]+=1
  return area_dictionary


# create dictionary of areas to store the number of hurricanes involved in
#print(count_area())


# 5
# Calculating Maximum Hurricane Count
def find_the_most_affected():
  areas=count_area()
  maxi=0
  for i,j in areas.items():
    if j >maxi:
      most=i
      maxi=j
  return most,maxi


# find most frequently affected area and the number of hurricanes involved in
#print("The most affected area by the hurricanes is {} with the number {} times".format(find_the_most_affected()[0],find_the_most_affected()[1]))

# 6
# Calculating the Deadliest Hurricane

def deadliest():
  hurricanes=hurricane_dict(names,months,years,max_sustained_winds,areas_affected,deaths,damages)
  maxi=0
  for j in hurricanes.values():
    if j["Deaths"]>maxi:
      maxi=j["Deaths"]
      most=j["Name"]
  return maxi,most

# find highest mortality hurricane and the number of deaths

#print("The deadliest hurricane is {} with the number {} ".format(deadliest()[1],deadliest()[0]))

# 7
# Rating Hurricanes by Mortality
def rate_hurricane():
  hurricanes=hurricane_dict(names,months,years,max_sustained_winds,areas_affected,deaths,damages)
  mortality_scale={}
  mortality_scale.update({0:[] ,1:[]
  ,2:[] ,3:[] ,4:[] ,5:[]})
  for i in hurricanes.values():
    if i["Deaths"]==0 :
      mortality_scale[0].append(i)
    elif i["Deaths"]>0 and i["Deaths"]<=100:
      mortality_scale[1].append(i)
    elif i["Deaths"]>100 and i["Deaths"]<=500:
      mortality_scale[2].append(i)
    elif i["Deaths"]>500 and i["Deaths"]<=1000:
      mortality_scale[3].append(i)
    elif i["Deaths"]>1000 and i["Deaths"]<=10000:
      mortality_scale[4].append(i)
    elif i["Deaths"]>10000:
      mortality_scale[5].append(i)
  return mortality_scale

# categorize hurricanes in new dictionary with mortality severity as key
#print(rate_hurricane())

# 8 Calculating Hurricane Maximum Damage
def greatest_damage():
  hurricanes=hurricane_dict(names,months,years,max_sustained_winds,areas_affected,deaths,damages)
  maxi=0
  for j in hurricanes.values():
    if j["Damage"]!="Damages not recorded":
      if j["Damage"]>maxi:
        maxi=j["Damage"]
        most=j["Name"]
  return maxi,most

# find highest damage inducing hurricane and its total cost

#print("The  hurricane which caused the greatest damage is {} with the number {} ".format(greatest_damage()[1],greatest_damage()[0]))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_scale():
  hurricanes=hurricane_dict(names,months,years,max_sustained_winds,areas_affected,deaths,damages)
  damagescale={}
  damagescale.update({0:[] ,1:[]
  ,2:[] ,3:[] ,4:[] ,5:[]})
  for i in hurricanes.values():
    if i["Damage"]!="Damages not recorded":
      if i["Damage"]==0 :
        damagescale[0].append(i)
      elif i["Damage"]>0 and i["Damage"]<=100000000:
        damagescale[1].append(i)
      elif i["Damage"]>100000000 and i["Damage"]<=1000000000:
        damagescale[2].append(i)
      elif i["Damage"]>1000000000 and i["Damage"]<=10000000000:
        damagescale[3].append(i)
      elif i["Damage"]>10000000000 and i["Damage"]<=50000000000:
        damagescale[4].append(i)
      elif i["Damage"]>50000000000:
        damagescale[5].append(i)
  return damagescale

# categorize hurricanes in new dictionary with damage severity as key
print(damage_scale())
