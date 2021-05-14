import inspect

def parse_function(function:object)->tuple:
    print(function)
    function_name = function.__name__
    params = [locals()[arg] for arg in inspect.getargspec(function).args]

    return (function_name, params)

    



    

        
