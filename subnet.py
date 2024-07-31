import ipaddress
import customtkinter
import tkinter

test = "hello"
#functions
def startCalculate():
    try:
        ip_addrGet = ip_addrSt.get()

        ip_addr = ipaddress.ip_interface(ip_addrGet)
        print(ip_addr)
        net_addr = ip_addr.network
        pref_len = ip_addr.with_prefixlen
        mask = ip_addr.with_netmask
        wildcard = ip_addr.hostmask
        br_addr = net_addr.broadcast_address
        
        
        nettext = "Network Address: " + str(net_addr).split('/')[0]
        brdtext = "Broadcast Address : " + str(br_addr)
        CIDRtext = 'CIDR Notation : ' + pref_len.split('/')[1]
        masktext = "Subnet Mask : " + mask.split('/')[1]
        wildcardtext = "Wildcard Mask : " + str(wildcard)
        showfirsttext = 'First IP : ' + str(list(net_addr.hosts())[0])
        showlasttext = 'Last IP : ' + str(list(net_addr.hosts())[-1])

        showip.configure(text=ip_addr)
        showNetAddr.configure(text = nettext)
        showBrdAddr.configure(text = brdtext)
        showCIDRAddr.configure(text = CIDRtext)
        showMask.configure(text = masktext)
        showWildcard.configure(text= wildcardtext)
        showFirstIP.configure(text = showfirsttext)
        showLastIP.configure(text = showlasttext)
        

    except:
        print("no bueno")
    



#App appearance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Subnet Calculator")

header = customtkinter.CTkLabel(app, text="Subnet Calculator")
header.pack(pady = 10)

title = customtkinter.CTkLabel(app, text='Insert Your IP Address/Mask')
title.pack(pady = 10)

#IP Output
ipaddvar = tkinter.StringVar()
ip_addrSt= customtkinter.CTkEntry(app, width=350, height=40, textvariable=ipaddvar)
ip_addrSt.pack(pady=10)
#Calculate
calculate = customtkinter.CTkButton(app, text='Calculate Subnet', command=startCalculate)
calculate.pack(pady=10)

#calculations
showip = customtkinter.CTkLabel(app, text="")
showip.pack()

showNetAddr = customtkinter.CTkLabel(app, text="")
showBrdAddr = customtkinter.CTkLabel(app, text="")
showCIDRAddr = customtkinter.CTkLabel(app, text="")
showMask = customtkinter.CTkLabel(app, text="")
showWildcard = customtkinter.CTkLabel(app, text="")
showFirstIP = customtkinter.CTkLabel(app, text="")
showLastIP = customtkinter.CTkLabel(app, text="")
showNetAddr.pack(pady=2)
showBrdAddr.pack(pady=2)
showCIDRAddr.pack(pady=2)
showMask.pack(pady=2)
showWildcard.pack(pady=2)
showFirstIP.pack(pady=2)
showLastIP.pack(pady=2)

#run app
app.mainloop()