keybnds=('''ESC''', '''F1''', '''F2''', '''F3''', '''F4''', '''F5''', '''F6''', '''F7''', '''F8''', '''F9''', '''F10''', '''F11''', '''F12''', '''PRINT_SCREEN/SYS_RQ''', '''SCROLL_LOCK''', '''PAUSE_BREAK''', '''~_`''', '''1''', '''2''', '''3''', '''4''', '''5''', '''6''', '''7''', '''8''', '''9''', '''0''', '''-''', '''=_+''', '''BACKSPACE''', '''INSERT''', '''HOME''', '''PG_UP''', '''NUM_LOCK''', '''NUM_/''', '''NUM_*''', '''NUM_-''', '''TAB''', '''Q''', '''W''', '''E''', '''R''', '''T''', '''Y''', '''U''', '''I''', '''O''', '''P''', '''[''', ''']''', '''BACKSLASH''', '''DEL''', '''END''', '''PG_DOWN''', '''NUM_7''', '''NUM_8''', '''NUM_9''', '''NUM_+''', '''CAPS_LOCK''', '''A''', '''S''', '''D''', '''F''', '''G''', '''H''', '''J''', '''K''', '''L''', ''';''', '''QUOTATION_MARKS''', '''ENTER''', '''NUM_5''', '''5''', '''6''', '''SHIFT''', '''Z''', '''X''', '''C''', '''V''', '''B''', '''N''', '''M''', ''',''', '''.''','''FRONTSLASH''', '''R_SHIFT''', '''ARROW_UP''', '''NUM_1''', '''NUM_2''', '''NUM_3''', '''NUM_ENTER''', '''CTRL''', '''WIN_HOME''', '''ALT''', '''SPACEBAR''', '''R_ALT''', '''PRINT_PAPER''','''CTRL_2''', '''LEFT_ARROW''', '''DOWN_ARROW''', '''RIGHT_ARROW''', '''NUM_0''', '''NUM_DEL''')

keyta=[">29<", ">3A<", ">3B<", ">3C<", ">3D<", ">3E<", ">3F<", ">40<", ">41<", ">42<", ">43<", ">44<", ">45<", ">46<", ">47<", ">48<", ">35<", ">1E<", ">1F<", ">20<", ">21<", ">22<", ">23<", ">24<", ">25<", ">26<", ">27<", ">2D<", ">2E<", ">2A<", ">49<", ">4A<", ">4B<", ">53<", ">54<", ">55<", ">56<", ">2B<", ">14<", ">1A<", ">08<", ">15<", ">17<", ">1C<", ">18<", ">0C<", ">12<", ">13<", ">2F<", ">30<", ">31<", ">4C<", ">4D<", ">4E<", ">5F<", ">60<", ">64<", ">57<", ">39<", ">04<", ">16<", ">07<", ">09<", ">0A<", ">0B<", ">0D<", ">0E<", ">0F<", ">33<", ">34<", ">28<", ">5C<", ">5D<", ">5E<", "2", ">1D<", ">1B<", ">06<", ">19<", ">05<", ">11<", ">10<", ">36<", ">37<", ">38<", "32", ">52<", ">59<", ">5A<", ">5B<", ">58<", "1", "8", "4", ">2C<", "64", ">65<", "16", ">50<", ">51<", ">4F<", ">62<", ">63<"
]

#print(len(keyta))
#print(len(keybnds))

######variables#####

nm='amazon'#name of macrokey
idx='7fba9a6d-61d1-4973-a68e-41a26309b48e'
usx='jellycat';#user

brc1="{"
brcC="}"




op=(f'''  "Version": "v1.0.1.8",
  "Id": "{idx}",
  "Name": "{nm}",
  "ComPort": "COM5",
  "KeyList": [''')
x=55;
i=22;
keyT=(f'''>{i}<'''); #variable in for loop
ahk_script= ({x}) #corresponding assigned keyboard/letter within for loop



#print()
print(brc1)
print(f'\t{op}')
print(f'\t{brc1}')
bpk = '\\'

#print(len(keybnds))
bax=(len(keybnds))
for i in range(bax):
    #print(keyta[i], (keybnds[i]) );
    p1=(f'''\t"KeyName": "{keybnds[i]}",
      "Enabled": true,
      "KeyTag": "{keyta[i]}",
      "ExecuteLocation": "",
      "KeyState": 1,
      "Task": {brc1}
        "OneLineAhkScript": null,
        "StaticAhkScriptFromFile": "C:\\{bpk}Users\\{bpk}{usx}\\{bpk}Documents\\{bpk}ahkfiles\\{bpk}{keybnds[i]}.ahk",
        "PushKey": null,
        "OpenFile": null,
        "OpenFileArgs": ""''')
    print(f'{p1}')
    print(f'      {brcC}')
    print(f'    \t{brcC},')
    print(f'    \t{brc1}')
print('''    }
  ]
}''')
#print(f'      {brcC}')
#print(f'    \t{brcC},')
#print(f'    \t{brc1}')
