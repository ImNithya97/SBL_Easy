import os

def current_diectory():
    relpath = os.getcwd()
    # print(os.getcwd())
    curr_dict = relpath
    return curr_dict

# print(current_diectory())

def lib_append_to_Data_list(Ext_era,Ext_sur_name,Ext_fore_name,Ext_rank,Ext_service_number,Ext_decoration,Ext_birth_place,Ext_death_place,Ext_theatre_death,Ext_death_cause,Ext_roll,Ext_unit_name,Ext_other_detail,Ext_Record_url):

    list_details=[]
    #if Code1!=None and Code2!=None:
    list_details.extend([Ext_era,Ext_sur_name,Ext_fore_name,Ext_rank,Ext_service_number,Ext_decoration,Ext_birth_place,Ext_death_place,Ext_theatre_death,Ext_death_cause,Ext_roll,Ext_unit_name,Ext_other_detail,Ext_Record_url])
    #else:

        #list_details.extend([Client,InvoiceNumber,Insurance,PTname,DOS,ServiceCode,MPI,CCN_Number,RemitDate,DEB,PaidAmount,Status,HCPCS_Code,str(FromDate),str(NumServices),SubmittedAmount,AllowedAmount])
    return list_details

# -------------------------------------------------------

# +
from csv import writer

def Write_data_Output(saveloc,List):  
    
    #header= ['Era','Surname','Forename','Rank','Service Number','Decoration','Place of Birth','Theatre of Death','Cause of Death','SNWM Roll','Unit Name','Other Detail','Record Url']
    with open(saveloc+'\InputData.csv','a',newline='') as f_object:

# Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
# Pass the list as an argument into
        # the writerow()
        #writer_object.writerow(header)
        writer_object.writerow(List)
#Close the file object
        f_object.close()



        

