def division():
    x=1/0
try:
   division()

except ZeroDivisionError as detail:
    print ("error",detail)