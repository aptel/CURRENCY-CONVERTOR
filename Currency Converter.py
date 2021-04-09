import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Currency Converter")
Label_Frame = ttk.LabelFrame(win,text="Welcome to Real Time Currency Converter")
Label_Frame.pack()
label1 = ttk.Label(Label_Frame,text="1 USD = 74.93 Indian Rupee")
label1.grid(row=1,column=0,sticky=tk.W)
label2 = ttk.Label(Label_Frame,text="Date : 2021-03-28")
label2.grid(row=2,column=0,sticky=tk.W)
currency_dict = {'USD'  : [1,1],
'ARS' :[91.832147, 0.010889],
'AUD' : [1.308793,0.764063],
'BHD' : [0.376000,2.659574],
'BWP' : [11.036228,0.090611],
'BRL' : [5.756868,0.173706],
'GBP' : [0.725079,1.379160],
'BND' : [1.345896,0.742999],
'BGN' : [1.658151,0.603081],
'CAD' : [1.261023,0.793007],
'CLP' : [732.753654,0.001365],
'CNY' : [6.541663,0.152866],
'COP' : [3689.877565,0.000271],
'HRK' : [6.423848,0.155670],
'CZK' : [22.106193,0.045236],
'DKK' : [6.305495,0.158592],
'AED' : [3.672500,0.272294],
'EUR' : [0.847799,1.179525],
'HKD' : [7.769331,0.128711],
'HUF' :	[307.420003 ,0.003253],
'ISK' : [127.176954,0.007863],
'INR' : [72.499429,0.013793],
'IDR':	[14433.913671,0.000069],
'IRR':  [42025.318571,0.000024],
'ILS':  [3.330576,0.300248],
'JPY': [109.661582,0.009119],
'KZT': [423.111538,0.002363],
'KWD':  [0.302615,3.304532],
'LYD' : [4.512422,0.221610],
'MYR':	[4.147012,0.241137],
'MUR':  [40.536031,0.024669],
'MXN': [20.585618,0.048578],
'NPR':  [116.542833 ,0.008581],
'NZD': [1.426128,0.701199],
'NOK':[8.582415,0.116517],
'OMR':[0.384500,2.600780],
'PKR' : [154.976602,0.006453],
'PHP':  [48.432249,0.020647],
'PLN':  [3.936141,0.254056],
'QAR':  [3.640000,0.274725],
'RON':	[4.142482,0.241401],
'RUB':  [75.928838,0.013170],
'SAR':	[3.750000,0.266667],
'SGD':	[1.345896,0.742999],
'ZAR':	[14.973796,0.066783],
'KRW':	[1129.112376,0.000886],
'LKR'	:[198.585646,0.005036],
'SEK' : [8.643736,0.115691],
'CHF' : [0.939182,1.064756],
'TWD':[28.631530,0.034927],
'THB' : [30.731895,0.032539],
'TTD':[6.801844,0.147019],
'TRY' : [8.088691,0.123629]

}

combo1_var = tk.StringVar()
var1_combobox = ttk.Combobox(Label_Frame,width=16,textvariable=combo1_var,state='readonly')
var1_combobox['values'] = tuple(currency_dict)
var1_combobox.grid(row=3,column=0,padx=20,pady=20)
var1_combobox.current(0)

combo2_var = tk.StringVar()
var2_combobox = ttk.Combobox(Label_Frame,width=16,textvariable=combo2_var,state='readonly')
var2_combobox['values'] = tuple(currency_dict)
var2_combobox.grid(row=3,column=1,padx=20,pady=20)
var2_combobox.current(21)

entry1_var = tk.IntVar()
entry1 = ttk.Entry(Label_Frame,width=18,textvariable=entry1_var)
entry1.grid(row=4,column=0)

entry2 = ttk.Label(Label_Frame)
entry2.grid(row=4,column=1)

def action(event=None):
    if combo1_var.get()=='USD':
        a = str(combo2_var.get())
        tup = currency_dict.get(a)
        b = int(entry1_var.get())
        answer = str(b*int(tup[0]))
        entry2.configure(text=answer)
        return
    else:
        a = combo1_var.get()
        b = str(combo2_var.get())
        tupusd = tuple(currency_dict.get(a))
        c = int(entry1_var.get())
        answerusd = c*int(tupusd[1])
        tup = currency_dict.get(b)
        sec = tup[0]
        answer = str(answerusd*sec)

        entry2.configure(text=answer)
        return
        
        
button = ttk.Button(Label_Frame,text='Convert',command=action)
button.bind("<Button-1>",action)
button.grid(row=5,column=1)






















win.mainloop()
