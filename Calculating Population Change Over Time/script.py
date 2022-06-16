city_name = "Istanbul, Turkey"
pop_1927 = 691000
pop_2017 = 15029231
pop_change = pop_2017 - pop_1927

percentage_gr = ((pop_2017 -pop_1927)/pop_1927)*100

annual_gr = percentage_gr / (2017-1927)

def population_growth(year_one, year_two, population_one, population_two):
  growth_rate = ((population_two - population_one)/population_one)*100
  annual_rate = growth_rate / (year_two - year_one)
  return annual_rate, growth_rate



print(annual_gr)
set_one = population_growth(1927,2017,pop_1927, pop_2017)
print(set_one)
report = "The growth rate of Istanbul, Turkey from 1927-2017 was " + str(set_one[1]) + "%. The annual growth rate was "+str(set_one[0]) + "%."
print(report)

set_two = population_growth(1950,2000, 983000, 8831800)
