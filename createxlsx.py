import openpyxl
import os

nc=int(input("Enter the No of Sheets : "))

if nc%100 == 0:
    nc=nc+1
else:
    nc=nc+100

j=0

for i in range(0,nc,100):
    if i==0:
        pass
    else:
        folder_name=f"files/{j} - {i}" # 0 - 100 
        if os.path.exists(folder_name):
            pass
        else:
            os.makedirs(folder_name)
            p=j
            for k in range(j,i+1,10): # 0 - 10
                if k==j:
                    pass
                else:
                    file_name=f"{folder_name}/{p+1} - {k} .xlsx"
                    wb=openpyxl.Workbook()
                    wb.remove_sheet(wb.active)
                    for q in range(p+1,k+1,1):
                        wb.create_sheet(str(q))
                        wb.save(file_name)
                p=k
    j=i
