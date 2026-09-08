# Write retry(func, times) that calls another function up to times times until it succeeds, and
# returns the result — functions as arguments, plus basic error handling.

def retry(func, times) :
    for i in range(1, times+1) :
        try :
            return(func())
        except Exception:
            continue
    return "retry again"