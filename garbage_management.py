print("\n welcome to smart garbage maanagement system")


Garbage_types = ['Biodegradeable_garbage','non_Biodegradeable_garbage']
Garbage_sub_types = ['recyclable','non_recyclable']

user_garbage_collection_in_source = []

def garbage_type_and_amount_selection():
    for i in range (2):
        print(f'select {i} for {Garbage_types[i]}')

    select = int(input("Enter any number : "))

    if select == 0:
        amount = int(input("Enter garbage amount : "))
        garbage_name = Garbage_types[select]
        user_garbage_collection_in_source.append({'garbage_name':garbage_name,'amount':amount}) 

    elif select == 1:
        print("Please select any subtypes from here")
        for i in range(2):
            print(f'select {i} for {Garbage_sub_types[i]}')
        select = int(input("Enter any number : "))
        amount = int(input("Enter garbage amount"))
        garbage_name = Garbage_types[select]
        user_garbage_collection_in_source.append({'garbage_name':garbage_name,'amount':amount})

        
    return user_garbage_collection_in_source

#for login mechanism 
garbage_source= ['Household garbage','SME','Industrial garbage','GO','Industrial garbage']

#for login mechanism ends

class user:
    def __init__(self,name,address,warning_msg,total_bill):
        self.name = name
        self.address = address
        self.total_bill=total_bill
        self.warning_msg = warning_msg

    def print_user_details(self):
        print("--------------- Printing user detials -----------\n")
        print(f'{self.name} , {self.address} , {self.total_bill}')

    def total_bill_calculation(self):
        pass

class source_bin:
    def __init__(self,garbage):
        self.garbage=garbage
        self.capacity=10

    def printing_all_garbage(self):
        print("Printing garbage details in source bin ")
        for grbg in self.garbage:
            print(grbg)

    def sending_garbage_to_GMP(self):
        gmp_obj = GMP_Bin()
        gmp_obj.receive_garbage_from_source(self.garbage)
        gmp_obj.printing_gmp_garbage()

class GMP_Bin: #underground tunnel city corp. bin
    def __init__(self) :
        self.GMP_garbage=[]

    def receive_garbage_from_source(self,garbage_from_source):
        self.GMP_garbage.extend(garbage_from_source)
        # test function
        # for grbg in garbage_from_source:
        #     for j in grbg:
        #         self.GMP_garbage.append(j)

    # def printing_gmp_garbage(self):
    #     print("****printing all garbage in gmp bins------\n")
    #     for grbg in self.GMP_garbage:
    #         for j in grbg:
    #             print(j)
    #     print("gmp bin garbage prints ends---------------\n")
                
    def printing_gmp_garbage(self):
        print("****printing all garbage in gmp bins------\n")
        for grbg in self.GMP_garbage:
            # print(grbg['garbage_name'])
            # print(grbg['amount'])
            print(grbg)
        print("gmp bin garbage prints ends---------------\n")

    
    def allocation_of_garbage_to_bins(self):
        bio_bin_obj= Bio_bin()

        #allocation all garbage to specific bins here 
        for grbg in self.GMP_garbage:
            grbg_name = grbg['garbage_name']
            grbg_amount = grbg['amount']
            print("printing from allocation ",grbg_name)

            if grbg_name == 'Biodegradeable_garbage':
                bio_bin_obj.add_garbage({'garbage_type':grbg_name,'amount':grbg_amount})
                
            
            elif grbg_name == 'non_Biodegradeable_garbage':
                non_bio_bin_obj = Non_Bio_bin({'garbage_type':grbg_name,'amount':grbg_amount})

            elif grbg_name == 'recyclable':
                pass
            elif grbg_name == 'non_recyclable':
                pass

class Bio_bin:
    # def __init__(self,garbage) :
    #     self.bio_garbage= garbage
    #     bio_garbage_collection = []
    bio_garbage_collection = []
    def __init__(self):
        self.bio_garbage=[]
    
    def add_garbage(self,garbage):
        self.bio_garbage.append(garbage)

    def printing_bio_bin_garbage(self):
        print("Staring to print bio bin garbae----------->>>>>>")
        for grbg in self.bio_garbage:
            print(grbg)
        print("Bio bin garbage print ends----------->>>>>>>>>>>")


class Non_Bio_bin:
     #make changed like Bio_bin
     def __init__(self,garbage) :
        self.non_bio_garbage= garbage
        non_bio_garbage_collection = []
    

class Recyclable_bin:
     def __init__(self,garbage) :
        self.recyclable_garbage= garbage
        recyclabe_garbage_collection = []

class Non_Recyclable_bin:
     def __init__(self,garbage) :
        self.non_recyclable_garbage= garbage
        non_recyclable_garbage_collection = []



    

class user_billing_calculation:
    #let's start calculating user billing mechanism : 
    pass

class user_billing_history:
    pass

            
user1=user("admin","dhaka","empty","empty")

#test start

#test ends

while(True):
    print("-----Enter any number from below----")
    print("***1 :to check user details Enter ***")
    print("\n***2 :to enter garbage to source bin Enter :***")
    print("\n***3 : To send garbage source to GMP_bin  Enter***")
    print("\n***4 : print all the garbage in bio garbage***")  #for testing

    print("***\n5 :to logout  ***")

    choice = int(input("choice : "))
    if choice == 1 :
        user1.print_user_details()

    elif choice == 2 :
        print("\nplease select garbage type first")
        garbage_type_selection_and_amount = garbage_type_and_amount_selection()  
       
        source_bin_obj = source_bin(garbage_type_selection_and_amount)
        source_bin_obj.sending_garbage_to_GMP()
        

        gmb_bin_obj = GMP_Bin()
        gmb_bin_obj.allocation_of_garbage_to_bins()

    elif choice ==3:
        pass

    elif choice ==4:
        bio_bin_obj = Bio_bin()
        bio_bin_obj.printing_bio_bin_garbage()

    elif choice == 5:
        print("Logging out ------")
        break
    



