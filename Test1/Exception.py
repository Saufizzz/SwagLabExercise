ItemsInCarts = 2
# if there are no 2 item in the cart the test failed

# this method will raise exception when the test does not meet the condition
#if ItemsInCarts != 2:
    #raise Exception(" The carts has not been fulfilled ")

if ItemsInCarts != 2:
    pass
# do nothing even if the condition is not met
#assert will require the condition to be true if false the test fail
assert(ItemsInCarts == 2)

#try , except
try: # it will get the error but wont fail the test, it will send control to another block (except)
    with open("filelog.txt") as reader:
        reader.read()
except:
    print("somehow i reached this block because there is failure in try block")

# error that pythonn give whenever defects comes
try: # it will get the error but wont fail the test, it will send control to another block (except)
    with open("filelog.txt") as reader:
        reader.read()
# this will show what python shown as error to the output
except Exception as e:
    print("somehow i reached this block because there is failure in try block")
    print(e)
# this keyword will execute and basically connected to try and except (used only when have try and except block mechanism)
# this executes everytime run test irrespective of errors received
finally:
    print("cleaning up resources")