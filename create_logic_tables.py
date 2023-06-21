"""Creates the permutations of logic tables for nandgame"""

def create_table(size):
    """Generate the output for the table...
    
    As much as I am a glutton for punishment, even I don't want to bother doing
    this manually!
    
    Is this neat...not really. Does it work (and save so much time)?
    
    Hell yes!
    
    Use?
    
    python -c "from create_logic_tables import create_table;\
    create_table(<size>);" > <outputfile>

    There is no error catching...just use it correctly ¯\\\_(ツ)_/¯
    """

    perms = [str(bin(x))[2:].zfill(9) for x in range(2 ** (9))]

    for x in perms:
        total = 0
        for i, y in enumerate(x):
            space = " " * 6
            if i in range(8):
                space += " "
            if y == "1":
                if i in [3, 7, 8]:
                    total += 1
                if i in [2, 6]:
                    total += 2
                if i in [1, 5]:
                    total += 4
                if i in [0, 4]:
                    total += 8
            print(f"|{space}{y}", end="")
        binary_total = str(bin(total)[2:].zfill(5))
        for j, z in enumerate(binary_total):
            space = " " * 7
            if j != 0:
                space += " "
            print(f"|{space}{z}", end="")
        print(f"|{str(total).rjust(7)}|")
