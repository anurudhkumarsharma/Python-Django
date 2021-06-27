def cool(original_func):

    def supercool():
        print('i am very cool!')

        original_func()

        print('middle')
        
    return supercool

@cool
def func():
    print('my name is rajat')
func()

