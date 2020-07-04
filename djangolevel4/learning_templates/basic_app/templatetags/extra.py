from django import template

register = template.Library()



"""
Using Decorator we can pass in below our customized cut function. This is one way of calling the customized cut filter function.
"""
@register.filter(name = 'cut')

def cut(value, args):

    """
    # The cut is a django function which can be customized. The function takes value and extra arguments as actual parameter which
    you pass to call this function.
    # value copies the items you passed in context_dict
    # args takes extra arguments that you pass in
    """
    return value.replace(args, "")
    """
    For example If value is Dhruvajyoti and args is ajyoti then it will return Dhruv
    """

"""
This is the second way of calling the customized cut filter function. Below the call to cut function is commented shortcuts
since we already hace called the function by using python decorator.
The first argument 'cut' is the filter name that you will call from others.html.
And the second argument cut is the function call which we have defined here.
"""
#register.filter('cut', cut)
