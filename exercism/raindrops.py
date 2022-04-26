drops = [[3, 'Pling'], 
         [5, 'Plang'], 
         [7, 'Plong']]

def convert(number):
    result = [string for factor, string in drops if number % factor == 0]
    return "".join(result) or str(number)