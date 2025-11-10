while True:
    try:
        Family_Name = {
            "Father": "Jagat Narayan Shukla",
            "Mother": "Parveena Shukla",
            "Daughter": "Bhawani Devi",
            "SON1": "Pundrik Shukla",
            "SON2": "Jishnu Shukla"
        }
        Accesscode= input("Enter Your Access Code is: ")
        if Accesscode == "12345":
            print("Bilkul Sahi Code Diya hai \n Family's Data is", Family_Name)
            break
        else:
            print("Bhaiya Tum Kun Ho")
    except ValueError:
        print("Koi Exception nhi Milega")


    
    