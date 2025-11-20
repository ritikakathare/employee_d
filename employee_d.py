import sys
if len(sys.argv) !=3:
  print("usage: python employee_d.py<EMP_name> <salary> <id> <exp>")
  sys.exit(1)
script_name=sys.argv[0]
EMP_name=sys.argv[1]
salary= sys.argv[2]
id= sys.argv[3]
exp=sys.argv[4]
print("script name:",script_name)
print("Employee name:",EMP_name)
print("Salary:",salary)
print("ID:",id)
print("expiriance:",exp)