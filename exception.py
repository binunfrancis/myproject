def division():
    x=1/0
try:
   division()

except Exception as detail:
    print ("error",detail)