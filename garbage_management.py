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
        gmp_obj = GMP_Bin(self.garbage)
        gmp_obj.printing_gmp_garbage()

class GMP_Bin: #underground tunnel city corp. bin
   
    def __init__(self,garbage_from_source) :
        self.GMP_garbage= garbage_from_source
        
    def printing_gmp_garbage(self):
        print("****printing all garbage in gmp bins------\n")
        for grbg in self.GMP_garbage:
            print(grbg)
        print("gmp bin garbage prints ends---------------\n")

    def allocation_of_garbage_to_bins(self):
        #allocation all garbage to specific bins here 
        
        for grbg in self.GMP_garbage:
            grbg_name = grbg['garbage_name']
            grbg_amount = grbg['amount']

            if grbg_name == 'Biodegradeable_garbage':
                bio_bin_obj= Bio_bin()
                bio_bin_obj = bio_bin_obj.add_garbage({'garbage_type':grbg_name,'amount':grbg_amount})
            
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

    def add_garbage(self,garbage) :
        self.bio_garbage= garbage
        

    def printing_bio_bin_garbage(self):
        for grbg in self.bio_garbage:
            print(grbg)


class Non_Bio_bin:
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

print("printing bio bin garbage")

bio_bin_obj = Bio_bin()
print(bio_bin_obj.printing_bio_bin_garbage())



#test ends

while(True):
    print("-----Enter any number from below----")
    print("***1 :to check user details Enter ***")
    print("\n***2 :to enter garbage to source bin Enter :***")
    print("\n***3 : To send garbage source to GMP_bin  Enter***")
    print("***\n4 :to Exit Enter ***")

    choice = int(input("choice : "))
    if choice == 1 :
        user1.print_user_details()

    elif choice == 2 :
        print("\nplease select garbage type first")
        garbage_type_selection_and_amount = garbage_type_and_amount_selection()  
        #the garbage amount can be stored using dictionary
        # capacity = input("Now enter source garbage capacity")
        # source_bin_obj = source_bin(selection_and_amount,capacity,"warning message empty")
        source_bin_obj = source_bin(garbage_type_selection_and_amount)
        source_bin_obj.sending_garbage_to_GMP()
        source_bin_obj.printing_all_garbage()

    elif choice ==3:
        pass
    elif choice == 4:
        print("Logging out ------")
        break
    



