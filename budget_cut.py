'''
Award Budget Cuts
The awards committee of your alma mater (i.e. your college/university)
asked for your assistance with a budget allocation problem theyre
facing. Originally, the committee planned to give N research grants
this year. However, due to spending cutbacks, the budget was reduced
to newBudget dollars and now they need to reallocate the grants.
The committee made a decision that theyd like to impact as few
grant recipients as possible by applying a maximum cap on all grants.
 Every grant initially planned to be higher than cap will now be exactly
  cap dollars. Grants less or equal to cap, obviously, wont be impacted.

Given an array grantsArray of the original grants and the reduced
budget newBudget, write a function findGrantsCap that finds in
the most efficient manner a cap such that the least number of
recipients is impacted and that the new budget constraint is met
(i.e. sum of the N reallocated grants equals to newBudget).

Analyze the time and space complexities of your solution.

'''

grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190

l = "datasource.endpoint_address=dscijk20hhkkz0.crchvegmd3hm.us-west-2.rds.amazonaws.com\ndatasource.endpoint_port=5432\ndatasource.username=dbuser\ndatasource.password=F1sb0gHpf1m2pZ4zCs8k2HRL4rzsmxWIM\n".split('\n')
data = {}
for i in l:
  prop = i.split('=')
  print prop
  if prop[0]:
      data[prop[0]] = prop[1]
print data