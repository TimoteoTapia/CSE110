"""
File: 02teach.py
Author: Timoteo Tapia
"""
#this is my main() function
def main():
    presentation()
    promp_data()
    output_data()

#It displays every saved variable (output) in a order way
def output_data():
    print("\n\nThe ID Card is:")
    print("----------------------------------------")
    print(f"{lastname.upper()}, {name.capitalize()}")
    print(f"{job.title()}")
    print(f"ID: {idnumber}\n")
    print(f"{email}")
    print(f"{phone}\n")
    print("Hair: {:20}Eye: {}".format(hair.capitalize(), eye.capitalize()))
    print("Month: {:19}Training: {}".format(month.capitalize(), training.capitalize()))
    print("----------------------------------------\n")

#it will save the input provided for the user and check it out if the data is valid
def promp_data():
    check_name = True
    check_last = True
    check_id = True
    check_hair = True
    check_eye = True
    check_month = True
    check_training = True
    while check_name:
        first_name = input("First name: ")
        if first_name.isalpha():
            check_name = False
            global name
            name = first_name
        else:
            print("\nInsert a valid value\n")
    while check_last:
        last_name = input("Last name: ")
        if last_name.isalpha():
            check_last = False
            global lastname
            lastname = last_name
        else:
            print("\nInsert a valid value\n")
    email_address = input("Email address: ")
    global email
    email = email_address
    phone_number = input("Phone number: ")
    global phone
    phone = phone_number
    job_title = input("Job title: ")
    global job
    job = job_title
    while check_id:
        id_number = input("ID Number: ")
        if id_number.isdigit():
            check_id = False
            global idnumber
            idnumber = id_number
        else:
            print("\nInsert a valid value\n")
    while check_hair:
        hair_color = input("Hear color: ")
        if hair_color.isalpha():
            check_hair = False
            global hair
            hair = hair_color
        else:
            print("\nInsert a valid value\n")
    while check_eye:
        eye_color= input("Eye color: ")
        if eye_color.isalpha():
            check_eye = False
            global eye
            eye = eye_color
        else:
            print("\nInsert a valid value\n")
    while check_month:
        month_started = input("Month you started to work: ")
        if month_started.isalpha():
            check_month = False
            global month
            month = month_started
        else:
            print("\nInsert a valid value\n")
    while check_training:
        training_completed = input("Have you completed the training (yes/no): ")
        if training_completed.isalpha():
            if training_completed == "yes" or training_completed == "Yes" or training_completed == "no" or training_completed == "No":
                check_training = False
                global training
                training = training_completed
            else:
                print("\nInsert a valid value\n")
        else:
            print("\nInsert a valid value\n")

def presentation():
    print("\nPlease enter the following information\n")

#run my main fucntion
main()