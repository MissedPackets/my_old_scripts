d1="e "
q1='"'





# For every time you use a "flag", like /3 or /1 inside 'dialogue', it automatically splits the text and formats it into renpy's turnbased dialogue...


dialogue=".../1/3/1 ...!"
fa2=dialogue.split('/1')#made a new symbol so that it knows where to split and I won't confuse the , or space with a newline to split at.
print(fa2)
op=f'{d1}{q1}'

print(len(fa2))
#for fx in range(len(fa2)):
#    print(f'{op}{fa2[fx]}{q1}')


def func(x):
    for i in fa2:
        if dialogue  == '/3':
            print('oops! There was a split here; but, continue!')
            continue
        elif dialogue== '/1':
            print('oops! There was a split here (#1); but, continue!')
            continue

        else:
            print(i)

func(2)
