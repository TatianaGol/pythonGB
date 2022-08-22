def user_info(first_name, last_name, year, city, email, phone_number):
    print(f"{first_name} {last_name}, {year} года рождения, город проживания - {city}, email: "
          f"{email}, номер телефона: "
          f"{phone_number}")


print(user_info(first_name="Татьяна", last_name="Петрова", year="1992", city="Москва",
                email="tatiana@mail.ru", phone_number="4951234567"))